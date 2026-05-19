#!/usr/bin/env python3
"""블로그 MD 파일 → 유튜브 쇼츠 영상 생성 (Pexels 이미지 슬라이드쇼)"""

import os
import re
import sys
import subprocess
import tempfile
import requests
from pathlib import Path

import anthropic
from bs4 import BeautifulSoup
from gtts import gTTS
from PIL import Image, ImageDraw, ImageFont, ImageFilter
from io import BytesIO

BLOG_DIR = Path(__file__).parent.parent / "content"
OUTPUT_DIR = Path(__file__).parent.parent / "shorts_output"
OUTPUT_DIR.mkdir(exist_ok=True)

WIDTH, HEIGHT = 1080, 1920
FONT_SIZE = 56
TITLE_FONT_SIZE = 40
LINE_SPACING = 1.6
MAX_CHARS_PER_LINE = 16

PEXELS_API_KEY = "LEZTUwNuGPyL0D2n6ocqyvY7w5wB212AXodp1vyuaJCist1Kvo236VcD"


def extract_text_from_md(md_path: Path) -> tuple[str, str, list[str]]:
    content = md_path.read_text(encoding="utf-8")

    title = ""
    tags = []
    if content.startswith("---"):
        end = content.find("---", 3)
        frontmatter = content[3:end]
        for line in frontmatter.splitlines():
            if line.startswith("title:"):
                title = line.split(":", 1)[1].strip().strip('"')
            if line.startswith("tags:"):
                raw = line.split(":", 1)[1].strip()
                tags = re.findall(r'"([^"]+)"|([^\[\],\s]+)', raw)
                tags = [a or b for a, b in tags]
        content = content[end + 3:]

    content = re.sub(r'\{\{<.*?>}}', '', content, flags=re.DOTALL)
    content = re.sub(r'\{\{%.*?%\}\}', '', content, flags=re.DOTALL)
    soup = BeautifulSoup(content, "html.parser")
    text = soup.get_text(separator=" ")
    text = re.sub(r'\s+', ' ', text).strip()

    return title, text, tags


def generate_script_and_keywords(title: str, body: str, tags: list[str]) -> tuple[str, list[str]]:
    client = anthropic.Anthropic()
    prompt = f"""다음 블로그 글을 유튜브 쇼츠용으로 변환해줘.

아래 형식으로 정확히 출력해:
SCRIPT: (200~250자 한국어 나레이션 스크립트. 구어체, 핵심부터)
KEYWORDS: (Pexels 이미지 검색용 영어 키워드 3개, 쉼표 구분. 이미지로 표현 가능한 구체적인 단어)

제목: {title}
태그: {', '.join(tags[:5])}
본문: {body[:2000]}"""

    message = client.messages.create(
        model="claude-sonnet-4-6",
        max_tokens=600,
        messages=[{"role": "user", "content": prompt}]
    )
    response = message.content[0].text.strip()

    script = ""
    keywords = []
    for line in response.splitlines():
        if line.startswith("SCRIPT:"):
            script = line[7:].strip()
        elif line.startswith("KEYWORDS:"):
            keywords = [k.strip() for k in line[9:].split(",")]

    if not script:
        script = response
    if not keywords:
        keywords = ["korea life", "city", "people"]

    return script, keywords


def generate_audio(script: str, output_path: Path) -> float:
    tts = gTTS(text=script, lang="ko", slow=False)
    tts.save(str(output_path))

    result = subprocess.run(
        ["ffprobe", "-v", "error", "-show_entries", "format=duration",
         "-of", "default=noprint_wrappers=1:nokey=1", str(output_path)],
        capture_output=True, text=True
    )
    return float(result.stdout.strip())


def fetch_pexels_images(keywords: list[str], count: int = 4) -> list[Image.Image]:
    headers = {"Authorization": PEXELS_API_KEY}
    images = []

    for keyword in keywords:
        if len(images) >= count:
            break
        resp = requests.get(
            "https://api.pexels.com/v1/search",
            headers=headers,
            params={"query": keyword, "per_page": 2, "orientation": "portrait"},
            timeout=10
        )
        if resp.status_code != 200:
            continue
        for photo in resp.json().get("photos", []):
            url = photo["src"]["portrait"]
            img_resp = requests.get(url, timeout=15)
            img = Image.open(BytesIO(img_resp.content)).convert("RGB")
            # 1080x1920으로 크롭
            img = crop_to_ratio(img, WIDTH, HEIGHT)
            images.append(img)
            if len(images) >= count:
                break

    # 이미지가 부족하면 반복
    while len(images) < count and images:
        images.append(images[len(images) % len(images)])

    return images[:count]


def crop_to_ratio(img: Image.Image, w: int, h: int) -> Image.Image:
    target_ratio = w / h
    iw, ih = img.size
    current_ratio = iw / ih

    if current_ratio > target_ratio:
        new_w = int(ih * target_ratio)
        left = (iw - new_w) // 2
        img = img.crop((left, 0, left + new_w, ih))
    else:
        new_h = int(iw / target_ratio)
        top = (ih - new_h) // 2
        img = img.crop((0, top, iw, top + new_h))

    return img.resize((w, h), Image.LANCZOS)


def wrap_text(text: str, max_chars: int) -> list[str]:
    lines = []
    while len(text) > max_chars:
        cut = text[:max_chars].rfind(' ')
        if cut < max_chars // 2:
            cut = max_chars
        lines.append(text[:cut].strip())
        text = text[cut:].strip()
    if text:
        lines.append(text)
    return lines


def get_font(size: int):
    font_paths = [
        "/System/Library/Fonts/AppleSDGothicNeo.ttc",
        "/Library/Fonts/AppleGothic.ttf",
        "/System/Library/Fonts/Supplemental/Arial Unicode.ttf",
    ]
    for fp in font_paths:
        if os.path.exists(fp):
            try:
                return ImageFont.truetype(fp, size)
            except Exception:
                continue
    return ImageFont.load_default()


def create_frame(bg_img: Image.Image, script_chunk: str, title: str,
                 show_title: bool, frame_idx: int, total_frames: int) -> Image.Image:
    img = bg_img.copy()

    # 블러 + 어둡게
    img = img.filter(ImageFilter.GaussianBlur(radius=3))
    overlay = Image.new("RGBA", img.size, (0, 0, 0, 140))
    img = img.convert("RGBA")
    img = Image.alpha_composite(img, overlay).convert("RGB")

    draw = ImageDraw.Draw(img)
    font = get_font(FONT_SIZE)
    title_font = get_font(TITLE_FONT_SIZE)
    small_font = get_font(30)

    # 상단: 제목 (첫 프레임만)
    if show_title:
        title_clean = re.sub(r'\[.*?\]\s*', '', title)
        title_lines = wrap_text(title_clean, 18)
        y = 120
        # 반투명 배경
        box_h = len(title_lines[:2]) * 56 + 30
        draw.rectangle([(40, y - 15), (WIDTH - 40, y + box_h)],
                       fill=(0, 0, 0, 160))
        for line in title_lines[:2]:
            draw.text((60, y), line, font=title_font, fill=(99, 179, 237))
            y += 56

    # 하단: 스크립트 자막
    lines = wrap_text(script_chunk, MAX_CHARS_PER_LINE)
    total_h = len(lines) * int(FONT_SIZE * LINE_SPACING)
    y_start = HEIGHT - total_h - 180

    # 자막 배경 박스
    padding = 30
    draw.rectangle(
        [(40, y_start - padding), (WIDTH - 40, y_start + total_h + padding)],
        fill=(0, 0, 0, 190)
    )

    for line in lines:
        # 텍스트 중앙 정렬
        bbox = draw.textbbox((0, 0), line, font=font)
        text_w = bbox[2] - bbox[0]
        x = (WIDTH - text_w) // 2
        draw.text((x + 2, y_start + 2), line, font=font, fill=(0, 0, 0))
        draw.text((x, y_start), line, font=font, fill=(255, 255, 255))
        y_start += int(FONT_SIZE * LINE_SPACING)

    # 진행 바
    bar_y = HEIGHT - 80
    draw.rectangle([(60, bar_y), (WIDTH - 60, bar_y + 4)], fill=(80, 80, 80))
    progress = int((WIDTH - 120) * (frame_idx + 1) / total_frames)
    draw.rectangle([(60, bar_y), (60 + progress, bar_y + 4)], fill=(99, 179, 237))

    # 워터마크
    draw.text((60, HEIGHT - 55), "jonghyunp.me.kr", font=small_font, fill=(180, 180, 180))

    return img


def split_script(script: str, n: int) -> list[str]:
    """스크립트를 n개 구간으로 분할"""
    sentences = re.split(r'(?<=[.!?다요죠네])\s+', script)
    sentences = [s.strip() for s in sentences if s.strip()]

    chunks = []
    per_chunk = max(1, len(sentences) // n)
    for i in range(n):
        start = i * per_chunk
        end = start + per_chunk if i < n - 1 else len(sentences)
        chunks.append(' '.join(sentences[start:end]))

    return [c for c in chunks if c]


def make_shorts(md_path: Path) -> Path:
    print(f"[1/6] 텍스트 추출: {md_path.name}")
    title, body, tags = extract_text_from_md(md_path)
    print(f"      제목: {title}")

    print("[2/6] 스크립트 + 키워드 생성 (Claude API)")
    script, keywords = generate_script_and_keywords(title, body, tags)
    print(f"      스크립트 ({len(script)}자): {script[:80]}...")
    print(f"      키워드: {keywords}")

    with tempfile.TemporaryDirectory() as tmp:
        tmp = Path(tmp)

        print("[3/6] 음성 생성 (gTTS)")
        audio_path = tmp / "audio.mp3"
        duration = generate_audio(script, audio_path)
        print(f"      재생 시간: {duration:.1f}초")

        print("[4/6] Pexels 이미지 다운로드")
        n_images = min(len(keywords), 4)
        images = fetch_pexels_images(keywords, count=n_images)
        print(f"      이미지 {len(images)}장 준비 완료")

        print("[5/6] 프레임 이미지 생성")
        chunks = split_script(script, len(images))
        # 이미지 수와 청크 수 맞추기
        while len(chunks) < len(images):
            chunks.append(chunks[-1])
        chunks = chunks[:len(images)]

        frame_duration = duration / len(images)
        frame_paths = []
        for i, (img, chunk) in enumerate(zip(images, chunks)):
            frame_path = tmp / f"frame_{i:02d}.png"
            frame = create_frame(img, chunk, title,
                                 show_title=(i == 0),
                                 frame_idx=i, total_frames=len(images))
            frame.save(str(frame_path))
            frame_paths.append((frame_path, frame_duration))

        print("[6/6] 영상 합성 (FFmpeg)")
        slug = re.sub(r'[^\w가-힣-]', '-', md_path.stem)
        output_path = OUTPUT_DIR / f"{slug}.mp4"

        # 각 프레임을 개별 클립으로 만들기
        clips = []
        for i, (fp, dur) in enumerate(frame_paths):
            clip_path = tmp / f"clip_{i:02d}.mp4"
            subprocess.run([
                "ffmpeg", "-y",
                "-loop", "1", "-t", str(dur), "-i", str(fp),
                "-c:v", "libx264", "-pix_fmt", "yuv420p",
                "-r", "24", "-vf", f"scale={WIDTH}:{HEIGHT}",
                str(clip_path)
            ], check=True, capture_output=True)
            clips.append(clip_path)

        # 클립 합치기
        concat_list = tmp / "concat.txt"
        concat_list.write_text('\n'.join(f"file '{c}'" for c in clips))

        video_only = tmp / "video_only.mp4"
        subprocess.run([
            "ffmpeg", "-y",
            "-f", "concat", "-safe", "0", "-i", str(concat_list),
            "-c", "copy", str(video_only)
        ], check=True, capture_output=True)

        # 오디오 합치기
        subprocess.run([
            "ffmpeg", "-y",
            "-i", str(video_only),
            "-i", str(audio_path),
            "-c:v", "copy", "-c:a", "aac", "-b:a", "128k",
            "-shortest", str(output_path)
        ], check=True, capture_output=True)

    print(f"\n완료: {output_path}")
    return output_path


if __name__ == "__main__":
    if len(sys.argv) < 2:
        posts = list(BLOG_DIR.glob("life/*.md")) + list(BLOG_DIR.glob("culture/*.md"))
        posts = [p for p in posts if not p.name.startswith("_")]
        posts.sort(key=lambda p: p.stat().st_mtime, reverse=True)
        if not posts:
            print("글을 찾을 수 없습니다.")
            sys.exit(1)
        md_path = posts[0]
        print(f"가장 최근 글 선택: {md_path.name}\n")
    else:
        md_path = Path(sys.argv[1])

    make_shorts(md_path)

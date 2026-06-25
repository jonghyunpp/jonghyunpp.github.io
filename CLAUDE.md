# 블로그 작업 가이드

## 기본 정보
- Hugo + PaperMod 테마, GitHub Pages 배포 (jonghyunp.me.kr)
- 배포: `hugo --minify` → `git add ... && git commit && git push origin main`

## 제목 규칙
- 대괄호 prefix 금지 (`[생활]`, `[Movie]` 등)
- 검색 키워드를 제목 앞에 배치
- 패턴: `핵심 키워드 — 부연 설명 총정리`
- 뉴스: `2026년 N월 N주차 주요 뉴스 정리`

## frontmatter 필수 항목
```yaml
title: "키워드 앞에 오는 제목"
date: YYYY-MM-DD
draft: false
categories: ["생활"]  # 생활 / 뉴스 / 문화 / 여행
tags: ["태그1", "태그2"]
summary: "검색 미리보기용 1-2줄 요약. 핵심 수치·혜택 포함."
ShowToc: false
ShowReadingTime: false
```

## 카테고리 색상 (--cat-rgb)
| 카테고리 | RGB |
|---|---|
| 뉴스 (news) | 29,158,117 |
| 생활 (life) | 55,138,221 |
| 문화 (culture) | 220,38,38 |
| 여행 (travel) | 186,117,23 |

## 인포그래픽
`{{< rawhtml >}}`로 인라인 HTML/CSS 삽입. 이미지 파일 불필요.
색상은 `rgba(R,G,B, alpha)` 하드코딩 (카테고리 RGB 값 사용).

### 스탯 카드
```html
<div style="display:flex;gap:10px;flex-wrap:wrap;margin:1.5em 0;">
  <div style="flex:1;min-width:110px;border:1.5px solid rgba(R,G,B,0.2);border-radius:10px;padding:14px 12px;text-align:center;background:rgba(R,G,B,0.03);">
    <div style="font-size:0.7rem;color:rgb(R,G,B);font-weight:700;margin-bottom:5px;">라벨</div>
    <div style="font-size:0.95rem;font-weight:800;">값</div>
    <div style="font-size:0.68rem;color:#6b7280;margin-top:2px;">부연</div>
  </div>
</div>
```

### 상황별 카드
```html
<div style="flex:1;min-width:160px;border:1.5px solid rgba(R,G,B,0.25);border-radius:12px;padding:16px;background:rgba(R,G,B,0.03);">
  <div style="font-size:0.72rem;font-weight:700;color:rgb(R,G,B);margin-bottom:8px;">라벨</div>
  <div style="font-weight:700;margin-bottom:7px;font-size:0.9rem;">제목</div>
  <div style="font-size:0.82rem;color:#6b7280;line-height:1.7;">내용</div>
</div>
```

### 팁 카드 (아코디언)
```html
<div style="border:1.5px solid rgba(R,G,B,0.2);border-radius:10px;overflow:hidden;">
  <div style="background:rgba(R,G,B,0.08);padding:11px 16px;display:flex;align-items:center;gap:10px;border-bottom:1px solid rgba(R,G,B,0.15);">
    <span style="font-weight:800;color:rgb(R,G,B);">①</span>
    <span style="font-weight:700;font-size:0.9rem;">제목</span>
  </div>
  <div style="padding:11px 16px;font-size:0.85rem;color:#4b5563;line-height:1.65;">내용</div>
</div>
```

## 표 스타일링
- 마크다운 표: 자동 파스텔 적용됨
- rawhtml 표: `display: table !important` 필수

## 쿠팡 파트너스 광고
"함께 읽으면 좋은 글" 바로 앞에 카테고리/주제별 배너 반드시 삽입.
모든 배너는 `Math.min(window.innerWidth-32, 900)` 반응형 width 사용.

| 숏코드 | ID | 설명 | 적용 대상 |
|---|---|---|---|
| `{{< coupang >}}` | 997882 | 생활용품 | 생활 카테고리 (기본) |
| `{{< coupang-interest >}}` | 997901 | 고객 관심 기반 | 금융/재테크 글 |
| `{{< coupang-digital >}}` | 997903 | 가전디지털 | 뉴스 카테고리 |
| `{{< coupang-kitchen >}}` | 997885 | 주방용품 | 요리/주방 관련 글 |
| `{{< coupang-fashion >}}` | 997899 | 패션의류/잡화 | 패션/뷰티 관련 글 |
| `{{< coupang-only >}}` | 997902 | 쿠팡온리 | 쇼핑/리뷰 관련 글 |
| `{{< coupang-car >}}` | 997904 | 자동차용품 | 뉴스 카테고리 (3종 순환) |
| `{{< coupang-sports >}}` | 997905 | 스포츠레저 | 뉴스 카테고리 (3종 순환) |

뉴스 카테고리: `coupang-digital` → `coupang-car` → `coupang-sports` 순으로 글마다 순환.

## 내부 링크
게시글 끝 주석 바로 위에 추가:
```markdown
**함께 읽으면 좋은 글**
- [제목](/카테고리/슬러그/)
```
같은 카테고리 기존 글과 반드시 연결.

## SEO
- 구글 집중 전략 (네이버는 독립 블로그 VIEW 탭 구조적 한계)
- Google Search Console + Naver Search Advisor 등록 완료
- GA: G-HG1LWJWS1R 연결 완료

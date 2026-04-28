---
title: "[정책/지원] 고유가 피해지원금 총정리 — 나는 얼마 받나? 어떻게 신청하나?"
date: 2026-04-27
draft: false
categories: ["생활"]
tags: ["고유가지원금", "피해지원금", "정부지원금", "민생지원", "생활정보"]
description: "오늘부터 신청 시작! 대상·금액·신청방법 한 번에 정리했습니다"
ShowToc: false
ShowReadingTime: false
---

{{< rawhtml >}}
<style>
.lf { font-family: inherit; margin: 0; }
.lf-lead { font-size: 14px; line-height: 1.85; color: var(--primary); margin-bottom: 2rem; }

/* 섹션 헤더 — nw 스타일 통일 */
.lf-section { margin-bottom: 2rem; }
.lf-section-header {
  display: flex; align-items: center; gap: 8px;
  font-size: 11px; font-weight: 500; letter-spacing: 0.07em; text-transform: uppercase;
  color: #059669;
  padding-bottom: 0.75rem; border-bottom: 0.5px solid var(--border); margin-bottom: 0;
}
.lf-section-header::before {
  content: ''; display: inline-block; width: 10px; height: 2px;
  background: #059669; border-radius: 1px; flex-shrink: 0;
}

/* 반응형 테이블 — overflow-x 스크롤 방식 */
.lf-table-scroll { overflow-x: auto; -webkit-overflow-scrolling: touch; margin: 12px 0; }
.lf-table-scroll-inner { border-radius: 8px; border: 0.5px solid var(--border); overflow: hidden; display: inline-block; min-width: 100%; }
.lf-table { width: 100%; border-collapse: collapse; font-size: 12px; white-space: nowrap; }
.lf-table th {
  background: var(--code-bg); color: var(--secondary);
  padding: 8px 14px; text-align: left; font-weight: 500; font-size: 11px;
  border-bottom: 0.5px solid var(--border);
}
.lf-table th.center, .lf-table td.center { text-align: center; }
.lf-table td {
  padding: 9px 14px; border-bottom: 0.5px solid var(--border);
  background: var(--entry); color: var(--primary); vertical-align: middle;
}
.lf-table tr:last-child td { border-bottom: none; }
.lf-table .amount { font-weight: 600; color: #059669; }
.lf-table .dim { color: var(--secondary); }

/* 계층 뱃지 */
.lf-cat { font-size: 10px; font-weight: 600; padding: 2px 7px; border-radius: 3px; display: inline-block; }
.lf-cat-basic { background: rgba(124,58,237,0.1); color: #7c3aed; }
.lf-cat-next  { background: rgba(37,99,235,0.1);  color: #2563eb; }
.lf-cat-gen   { background: rgba(5,150,105,0.1);  color: #059669; }

/* 팁 박스 */
.lf-tip {
  font-size: 12px; color: var(--secondary); line-height: 1.65;
  margin-top: 8px; padding: 8px 12px;
  background: rgba(5,150,105,0.07); border-left: 2px solid #059669; border-radius: 0 6px 6px 0;
}
.lf-tip.blue  { background: rgba(37,99,235,0.07);  border-left-color: #2563eb; }
.lf-tip.red   { background: rgba(244,63,94,0.07);  border-left-color: #f43f5e; }

/* 신청방법 그리드 */
.lf-method-grid { display: grid; grid-template-columns: 1fr 1fr; gap: 10px; margin: 12px 0; }
@media (max-width: 520px) { .lf-method-grid { grid-template-columns: 1fr; } }
.lf-method-card {
  border: 0.5px solid var(--border); border-radius: 8px;
  padding: 14px 16px; background: var(--entry);
}
.lf-method-card-title { font-size: 12px; font-weight: 600; color: var(--primary); margin-bottom: 8px; }
.lf-method-card ul { margin: 0; padding-left: 16px; }
.lf-method-card ul li { font-size: 12px; color: var(--secondary); line-height: 1.85; }

/* FAQ */
.lf-faq { border: 0.5px solid var(--border); border-radius: 8px; overflow: hidden; margin: 12px 0; }
.lf-faq-item { padding: 12px 16px; border-bottom: 0.5px solid var(--border); }
.lf-faq-item:last-child { border-bottom: none; }
.lf-faq-q { font-size: 12px; font-weight: 600; color: var(--primary); margin-bottom: 5px; }
.lf-faq-a { font-size: 12px; color: var(--secondary); line-height: 1.7; }

/* 링크 버튼 */
.lf-links { display: flex; flex-wrap: wrap; gap: 8px; margin: 12px 0; }
.lf-link-btn {
  display: inline-block; padding: 7px 14px; border-radius: 6px;
  font-size: 12px; font-weight: 600; text-decoration: none;
  border: 0.5px solid var(--border); color: var(--primary); background: var(--entry);
}
.lf-link-btn.primary { background: #059669; color: #fff; border-color: #059669; }

.lf-disclaimer { font-size: 11px; color: var(--secondary); text-align: center; margin-top: 1.5rem; line-height: 1.6; }
</style>

<div class="lf">

  <p class="lf-lead">
    오늘(4월 27일)부터 <strong>고유가 피해지원금</strong> 1차 신청이 시작됐습니다.<br>
    중동 전쟁으로 유가가 급등하면서 주유비·식료품비·전기료까지 생활비 부담이 커지자 정부가 내놓은 지원책입니다. 신청 안 하면 못 받으니, 지금 바로 확인해 보세요.
  </p>

  <!-- 지급 대상 -->
  <div class="lf-section">
    <div class="lf-section-header">📋 지급 대상 — 소득 하위 70%</div>
    <div class="lf-table-scroll">
      <div class="lf-table-scroll-inner">
        <table class="lf-table">
          <thead>
            <tr><th>가구 유형</th><th>월 소득 기준 (참고)</th><th class="center">비고</th></tr>
          </thead>
          <tbody>
            <tr><td>1인 가구</td><td>약 385만 원 이하</td><td class="center amount">대상 ✓</td></tr>
            <tr><td>2인 가구</td><td>약 630만 원 이하</td><td class="center amount">대상 ✓</td></tr>
            <tr><td>3인 가구</td><td>약 810만 원 이하</td><td class="center amount">대상 ✓</td></tr>
            <tr><td>4인 가구</td><td>약 990만 원 이하</td><td class="center amount">대상 ✓</td></tr>
          </tbody>
        </table>
      </div>
    </div>
    <div class="lf-tip blue">📌 정확한 대상 여부는 <strong>카카오톡 '국민비서'</strong> 또는 <strong>정부24</strong>에서 확인하세요. 기준은 건강보험료 납부액이며, 소득 상위 30%와 외국인(일부 예외)은 제외됩니다.</div>
  </div>

  <!-- 지급 금액 -->
  <div class="lf-section">
    <div class="lf-section-header">💵 지급 금액 — 계층·지역별 1인당</div>
    <div class="lf-table-scroll">
      <div class="lf-table-scroll-inner">
        <table class="lf-table">
          <thead>
            <tr>
              <th>계층</th>
              <th class="center">수도권</th>
              <th class="center">비수도권</th>
              <th class="center">인구감소 우대</th>
              <th class="center">인구감소 특별</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td><span class="lf-cat lf-cat-basic">기초생활수급자</span></td>
              <td class="center amount">55만 원</td>
              <td class="center amount">60만 원</td>
              <td class="center dim">—</td>
              <td class="center dim">—</td>
            </tr>
            <tr>
              <td><span class="lf-cat lf-cat-next">차상위·한부모</span></td>
              <td class="center amount">45만 원</td>
              <td class="center amount">50만 원</td>
              <td class="center dim">—</td>
              <td class="center dim">—</td>
            </tr>
            <tr>
              <td><span class="lf-cat lf-cat-gen">일반 가구</span></td>
              <td class="center amount">10만 원</td>
              <td class="center amount">15만 원</td>
              <td class="center amount">20만 원</td>
              <td class="center amount">25만 원</td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
    <div class="lf-tip">💡 <strong>예시:</strong> 비수도권 거주 기초수급자 4인 가족 → 60만 원 × 4명 = <strong>최대 240만 원</strong> 수령 가능. 가구원 수만큼 합산 지급됩니다.</div>
  </div>

  <!-- 신청 일정 -->
  <div class="lf-section">
    <div class="lf-section-header">📅 신청 일정</div>
    <div class="lf-table-scroll">
      <div class="lf-table-scroll-inner">
        <table class="lf-table">
          <thead>
            <tr><th>구분</th><th>대상</th><th>신청 기간</th><th class="center">마감</th></tr>
          </thead>
          <tbody>
            <tr>
              <td style="font-weight:600;">1차</td>
              <td>기초생활수급자 · 차상위계층 · 한부모가족<br><span style="font-size:11px;color:var(--secondary);">※ 1차 신청 시 2차 신청 불가</span></td>
              <td>4월 27일(월) ~ 5월 8일(금)</td>
              <td class="center">오후 6시</td>
            </tr>
            <tr>
              <td style="font-weight:600;">2차</td>
              <td>일반 가구 + 1차 미신청자 전체</td>
              <td>5월 18일(월) ~ 7월 3일(금)</td>
              <td class="center">오후 6시</td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
    <div class="lf-tip red">⚠️ <strong>사용 기한:</strong> 1·2차 모두 <strong>2026년 8월 31일(월)까지</strong> 사용해야 합니다. 남은 금액은 자동 소멸됩니다.</div>
  </div>

  <!-- 신청 방법 -->
  <div class="lf-section">
    <div class="lf-section-header">📱 신청 방법</div>
    <div class="lf-method-grid">
      <div class="lf-method-card">
        <div class="lf-method-card-title">💳 신용·체크카드로 받으려면</div>
        <ul>
          <li>각 카드사 홈페이지·앱·콜센터</li>
          <li>카카오뱅크 / 토스 / 카카오페이 앱</li>
          <li>네이버페이 앱</li>
        </ul>
      </div>
      <div class="lf-method-card">
        <div class="lf-method-card-title">🏪 지역사랑상품권으로 받으려면</div>
        <ul>
          <li>제로페이, 경기지역화폐 등 각 지방 앱</li>
        </ul>
        <div style="height:10px;"></div>
        <div class="lf-method-card-title">🏢 오프라인 신청</div>
        <ul>
          <li>주민센터 · 은행 영업점 방문</li>
          <li>거동 불편 시 '찾아가는 신청' 요청</li>
        </ul>
      </div>
    </div>
    <div class="lf-tip blue">📌 요일제 신청이 적용될 수 있습니다. 신청 전 거주지 주민센터 또는 정부24에서 본인 신청 가능 일정을 먼저 확인하세요.</div>
  </div>

  <!-- 사용처 -->
  <div class="lf-section">
    <div class="lf-section-header">🛍️ 사용처</div>
    <div class="lf-table-scroll">
      <div class="lf-table-scroll-inner">
        <table class="lf-table">
          <thead>
            <tr><th>수령 수단</th><th>사용 가능</th><th>사용 불가</th></tr>
          </thead>
          <tbody>
            <tr>
              <td>지역사랑상품권</td>
              <td>주소지 관할 지역 내 가맹점</td>
              <td>관할 지역 외</td>
            </tr>
            <tr>
              <td>신용·체크·선불카드</td>
              <td>연 매출 30억 원 이하 소상공인 매장</td>
              <td>유흥업소·사행업종·대형마트·백화점</td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
    <div class="lf-tip">💡 사용 지역은 신청자 본인의 주소지 관할 지역입니다. 이사 시 변경 신청 가능합니다.</div>
  </div>

  <!-- FAQ -->
  <div class="lf-section">
    <div class="lf-section-header">❓ 자주 묻는 질문</div>
    <div class="lf-faq">
      <div class="lf-faq-item">
        <div class="lf-faq-q">Q. 부모님이 소득 하위 70%인데, 피부양자인 나도 받나요?</div>
        <div class="lf-faq-a">네. 부모님이 대상이라면 피부양자로 등록된 자녀도 함께 지급받습니다.</div>
      </div>
      <div class="lf-faq-item">
        <div class="lf-faq-q">Q. 미성년 자녀 지원금은 누가 신청하나요?</div>
        <div class="lf-faq-a">주민등록 세대주가 신청합니다.</div>
      </div>
      <div class="lf-faq-item">
        <div class="lf-faq-q">Q. 1차 신청을 못 했으면 못 받나요?</div>
        <div class="lf-faq-a">아닙니다. 기초수급자·차상위·한부모 가구도 2차(5월 18일~7월 3일) 기간에 신청하면 받을 수 있습니다.</div>
      </div>
      <div class="lf-faq-item">
        <div class="lf-faq-q">Q. 스미싱 문자 주의!</div>
        <div class="lf-faq-a">정부 및 카드사는 <strong>URL이 포함된 문자메시지를 보내지 않습니다.</strong> URL이 포함된 문자는 스미싱이니 절대 클릭하지 마세요.</div>
      </div>
    </div>
  </div>

  <!-- 빠른 링크 -->
  <div class="lf-section">
    <div class="lf-section-header">🔗 빠른 신청 링크</div>
    <div class="lf-links">
      <a class="lf-link-btn primary" href="https://www.gov.kr" target="_blank" rel="noopener">정부24 바로가기</a>
      <a class="lf-link-btn" href="https://www.mois.go.kr" target="_blank" rel="noopener">행정안전부 공식 안내</a>
      <a class="lf-link-btn" href="https://pf.kakao.com/_xmVxnxb" target="_blank" rel="noopener">카카오톡 국민비서 구삐</a>
    </div>
  </div>

  <p class="lf-disclaimer">본 포스트는 행정안전부 공식 자료를 바탕으로 작성되었습니다. 정확한 지급 금액과 대상 여부는 정부24 또는 거주지 주민센터에서 확인하시기 바랍니다.</p>
</div>
{{< /rawhtml >}}

# Fashion House Practical Guides (V2.0)
> **Subtitle**: The Field Manual for Design, Operations, and Review
> **Usage**: 에이전트와 인간 실무자가 "어떻게 일해야 하는가"에 대한 구체적 지침입니다.

---

## Part 1. 설계 파트 (Design & Costing)
> **Goal**: "예산을 준수하는 목적성 있는 디자인" + **"카테고리 챔피언 발굴"**

### 1.1 카테고리 챔피언 전략 (The Champion Strategy)
사업 계획서에 의거, 각 카테고리별 '절대 강자' 상품을 육성한다.
- **Selection**: 재구매율 30% 이상 & 반품률 5% 미만인 상품.
- **Action**:
    - **Champion Edition**: 매 시즌 스펙 업그레이드 (Carry-over).
    - **Variation**: 챔피언 상품의 핏을 기반으로 소재/컬러만 변경하여 실패 확률 0% 도전.

### 1.2 디자인 프로세스 (Design Loop)
1.  **Input 접수**: `Product_Dev_Request.md` 확인.
    *   *Check*: 타겟 원가(Target Cost)와 필수 개선 요건(Pain Points) 파악.
2.  **Visual Prompting**:
    *   Gemini 3.0 Pro를 사용하여 디자인 시안 생성.
    *   **Rule**: "Kitsch Street" 무드와 "Essential" 스펙을 동시에 만족해야 함.
3.  **Costing Negotiation (협상)**:
    *   디자인 초안 → Hephaestus (GLM-4 Plus) 자동 원가 계산.
    *   *Note*: GLM API 한도 도달 시 `Antigravity (Gemini 3 Pro)`로 자동 전환. (Resilience Protocol)
    *   **Over Budget 시**:
        *   1순위: 부자재 삭제 (금속 → 플라스틱/삭제).
        *   2순위: 공임 절감 (절개선 축소).
        *   3순위: 요척 절감 (패턴 모듈화).

---

## Part 2. 운영 파트 (Launch & Ops)
> **Goal**: "팬덤을 열광시키는 결핍 마케팅" + **"글로벌 확장(GTM)"**

### 2.1 글로벌 GTM 프로세스 (Global Go-to-Market)
- **Target Market**: 일본, 대만, 중국 (D2C 채널 중심).
- **Localization**:
    - **Content**: 상세페이지 및 SNS 콘텐츠 현지 언어/문화 최적화.
    - **Pricing**: 현지 물류비 및 관세 반영한 국가별 가격 정책 수립.
- **Timeline**: 국내 런칭 D+1주 후 글로벌 순차 오픈.

### 2.2 런칭 전략 (Scarcity Launch)
1.  **물량 배분**:
    *   **1st Drop**: 전체 발주량의 30%. (조기 품절 목표)
    *   **Waitlist**: 품절 시 "재입고 알림 신청" 페이지로 전환 → 수요 데이터 수집.
2.  **타겟팅 (Clustering)**:
    *   **VIP (상위 10%)**: 런칭 1시간 전 '시크릿 링크' 발송.
    *   **Churned (이탈 고객)**: 개선된 포인트("이제 안 늘어납니다")를 강조한 '초대장' 발송.

---

## Part 3. IP 비즈니스 파트 (New Growth)
> **Goal**: "패션을 넘어 굿즈와 콘텐츠로"

### 3.1 IP 확장 가이드
- **Character**: 'KiKi' 캐릭터를 활용한 라이프스타일 굿즈 개발.
- **Licensing**: 타 브랜드(F&B, Tech)와의 콜라보레이션 제안서 작성.
- **Rule**: 모든 IP 제품은 "Wacky Willy Universe" 세계관을 반영해야 함.

---

## Part 4. 리뷰 파트 (Data Analysis)
> **Goal**: "매월 시장의 맥박(Pulse)을 짚고 즉각 반응한다"

### 4.1 월간 분석 기준 (Monthly Pulse)
| 지표 (Metric) | 기준 (Threshold) | 의미 (Meaning) |
| :--- | :--- | :--- |
| **재구매율 (Retention)** | **30% 이상** | **CHAMPION**. 카테고리 대표 상품으로 지정. |
| **MoM 성장률** | **+10% 이상** | **TRENDING**. 해당 카테고리/컬러 스팟 기획 즉시 착수. |
| **초기 판매속도 (Velocity)** | **일평균 50장↑** | **HIT**. 리오더 발주 및 파생 모델(Variation) 개발. |
| **반품률 (Return Rate)** | **15% 이상** | **WARNING**. 즉시 판매 중지 후 전수 검사 (QC). |

### 4.2 산출물 생성
분석이 끝나면 반드시 다음 두 문서를 업데이트해야 합니다.
1.  **`Monthly_Drop_Plan.md`**: 다음 달 드롭할 아이템 라인업 및 물량 계획.
2.  **`Spot_Dev_Request.md`**: 3주 내 입고 가능한 스팟 상품 개발 의뢰서.

---

## Appendix. 표준 산출물 양식 (Artifact Templates)

### [Template] 글로벌 런칭 계획 (Global Launch Plan)
```markdown
# [Season] Global GTM Strategy
## Target Region: [Japan/Taiwan/China]
- **Platform**: [D2C/Musinsa Global/Zozo]
- **Key Message**: [Localized Copy]
- **Influencer Strategy**: [List of Local Creators]
```

### [Template] 스팟 개발 의뢰서 (Spot Request)
```markdown
# [Month] Spot Product Request
## Base Item: [Existing SKU]
- **Modification**: [Color Change / Graphic Change]
- **Target Date**: [D+21]
- **Reason**: [Trending Keyword / Competitor Hit]
```

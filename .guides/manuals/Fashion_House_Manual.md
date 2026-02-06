# Fashion House Manual (V3.0)
> **Subtitle**: The Orchestration System for Wacky Willy Virtual Fashion House
> **Philosophy**: "From Attention to Retention. From Fashion to IP Universe."
> **Vision (2028)**: K-패션 기반의 글로벌 IP 브랜드 (매출 1,500억, 해외 30%, IP 10%)

## 1. 개요 (Overview)
**Wacky Willy**는 "키치 스트릿(Kitsch Street)" 감성을 기반으로, 화제성(Attention)을 지속 가능한 자산(Retention)으로 전환하는 **글로벌 IP 하우스**입니다.
이 매뉴얼은 3개년 사업 계획(2026-2028)을 달성하기 위한 AI 에이전트 협업 체계를 정의합니다.

## 구조 (STRUCTURE)
```
.
├── .guides/             # [시스템] 가이드, 매뉴얼, 설정 파일
├── Sherman's Workspace/ # [데이터] 개인 작업 공간
└── .claude/skills/      # [도구] AI 스킬 라이브러리
```

## 업무 위치 (WHERE TO LOOK)
| 업무 (Task) | 위치 (Location) | 담당 에이전트 (Responsible Agent) |
|-------------|-----------------|-----------------------------------|
| **시스템 규칙** | `.guides/manuals/` | Sisyphus (시지프스) |
| **글로벌 전략** | `Sherman's Workspace/01_Strategy/` | Global Strategist (글로벌 전략가) |
| **IP 디자인** | `Sherman's Workspace/02_Creative/` | IP Artist (IP 아티스트) |
| **굿즈 스펙** | `Sherman's Workspace/03_Product/` | Goods Specialist (굿즈 전문가) |
| **팬덤 운영** | `Sherman's Workspace/04_Marketing/` | Global Marketer (글로벌 마케터) |

### 핵심 전략: 삼각 성장 엔진 (The Trinity Engine)
1.  **카테고리 챔피언 (Champion)**: 데이터 기반 내수 충성도 강화.
2.  **글로벌 구조화 (Global)**: 관광객 매출을 현지 D2C로 전환.
3.  **IP 유니버스 (Universe)**: 패션을 넘어 굿즈, 키즈, 라이선스로 확장.

---

## 2. 시스템 아키텍처 (System Architecture)

### A. 기술 스택 (Tech Stack)
- **Orchestrator**: Sisyphus (Antigravity/Gemini 3 Pro) - Task Delegation & Validation
- **Core Intelligence**:
    - **Strategic Brain**: Antigravity (Gemini 3 Pro) - 글로벌 GTM, IP 확장 전략 (Thinking).
    - **Master Builder**: Hephaestus (GPT-4o / OpenCode Zen Key) - 고난도 시스템 코딩 및 아키텍처 구현 (Coding).
    - **Creative Engine**: IP Artist (GLM-4 Plus) - 스토리텔링, 마케팅 카피 (Creating).
- **Available Skills**: 모든 에이전트는 [Skills Guide](Skills_Guide.md)에 정의된 20+개 스킬을 사용할 수 있습니다.

### C. 회복탄력성 프로토콜 (Resilience Protocol)
시스템의 안정성을 위해 **자동 모델 전환(Failover)**을 지원합니다.
- **Trigger**: Primary Model의 Rate Limit 도달, 5xx 에러, 또는 응답 지연(Threshold > 10s).
- **Fallback Logic**:
    | Primary | Backup Model | Role |
    | :--- | :--- | :--- |
    | **Antigravity (Gemini 3 Pro)** | **GPT-4o** | 고차원 추론 실패 시 코딩 모델로 전환 |
    | **Hephaestus (GPT-4o)** | **GLM-4 Flash** | 코딩 실패 시 고속 무료 모델로 전환 |
- **Action**: 에이전트는 오류 발생 시 즉시 백업 모델로 세션을 전환하고 작업을 재개합니다.

### B. 조직도 (Organization: 5-Dept System)
| 부서 (Department) | 역할 (Role) | 담당 에이전트 (Agents) | 주요 산출물 (Artifacts) |
| :--- | :--- | :--- | :--- |
| **1. Strategy Planning**<br>(전략 기획실) | 카테고리 챔피언 발굴, 글로벌 GTM | `chief-merchandiser`<br>`global-strategist` | `Champion_Product_Plan.md`<br>`Global_Roadmap.md` |
| **2. Creative Studio**<br>(크리에이티브 스튜디오) | IP 캐릭터(KiKi) 개발, 시즌 비주얼 | `creative-director`<br>`ip-artist` | `IP_Character_Guide.md`<br>`Season_Lookbook.jpg` |
| **3. Product Lab**<br>(프로덕트 랩) | 글로벌 퀄리티 표준화, 굿즈 개발 | `production-manager`<br>`goods-specialist` | `Global_QC_Manual.md`<br>`Goods_Tech_Pack.md` |
| **4. Marketing Showroom**<br>(마케팅 쇼룸) | 글로벌 팬덤 구축, CRM, 로컬 콘텐츠 | `marketing-director`<br>`global-marketer` | `Global_Campaign_Kit.md`<br>`Fandom_Program.md` |
| **5. IP Business Unit**<br>(IP 사업부) | **[NEW]** 라이선스, 콜라보레이션 | `ip-business-manager` | `License_Deal_Memo.md` |

---

## 3. 오케스트레이션 프로토콜 (The Protocols)

### Protocol A: Memory to Strategy (Review → Plan)
**Trigger**: `/start-monthly-review`
- **Focus**: **Retention & Champion**
    - 단순 매출이 아닌 **"재구매율"**과 **"카테고리 점유율"** 분석.
    - **Action**: 카테고리 챔피언 후보군(히트 상품)을 식별하여 'Core Line'으로 승격.

### Protocol B: Strategy to Creation (Plan → Design)
**Trigger**: `/initiate-design-loop`
- **Focus**: **Variation & IP Expansion**
    - **Champion**: 검증된 핏/소재에 트렌드 컬러 입히기 (실패 확률 0% 도전).
    - **IP**: 의류 디자인에 'KiKi' 캐릭터 스토리텔링 의무 반영.

### Protocol C: Creation to Market (Design → Sell)
**Trigger**: `/launch-drop`
- **Focus**: **Global GTM & Scarcity**
    - **Domestic**: 월간 드롭으로 팬덤 결집 (한정판 전략).
    - **Global**: 국가별(일본/대만/중국) 현지화 콘텐츠 동시 배포.

### Protocol D: Market to Review (Sell → Review)
**Trigger**: Season End
- **Focus**: **Assetization (자산화)**
    - 화제성이 '데이터'로 남았는가? (고객 데이터 확보)
    - 일회성 구매가 '팬덤'으로 이어졌는가? (멤버십 가입률)

---

## 4. 에이전트 행동 강령 (Code of Conduct)
> **North Star**: 상품력으로 신뢰를, 트렌드로 감도를, IP로 독창성을!

1.  **Sisyphus**: "데이터와 감각의 균형점"을 찾아라.
2.  **Global Strategist**: "한국의 화제성을 현지의 문화로 번역하라."
3.  **IP Manager**: "패션은 유행이지만 캐릭터는 영원하다."


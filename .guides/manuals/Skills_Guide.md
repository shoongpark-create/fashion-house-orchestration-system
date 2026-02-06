# 🛠️ Wacky Willy AI Skills Guide

이 문서는 와키윌리 패션 하우스의 에이전트들이 사용하는 **AI 스킬(Skills)**의 상세 설명서입니다.
각 스킬은 특정 업무를 자동화하거나 고도화하기 위해 설계된 도구 모음입니다.

---

## 1. 개요 (Overview)

스킬 라이브러리는 5개의 핵심 영역으로 구성됩니다.

| 영역 (Category) | 경로 | 설명 | 주요 스킬 |
| :--- | :--- | :--- | :--- |
| **🧠 Strategy** | `strategy/` | 시장 분석, 세그먼테이션, 성과 리뷰 | `season-review-analyzer`, `sales-analyzer` |
| **🎨 Creative** | `creative/` | 이미지/영상 생성, 프롬프트 엔지니어링 | `kie-image-generator`, `video-production` |
| **🧵 Product** | `product/` | 원가 계산, 작업지시서, QC | `costing`, `techpack-generator` |
| **📢 Marketing** | `marketing/` | 채널 전략, 메시지 설계, 카피라이팅 | `channel-roadmap`, `hook-formulas` |
| **🔧 Tools** | `tools/` | 문서 처리(PDF/PPT), 인증 관리 | `pdf`, `pptx`, `auth-manager` |

---

## 2. Creative Skills (크리에이티브)

### 🎨 Kie Image Generator
Kie.ai의 13개 이상 최신 모델을 활용하여 고품질 패션 이미지를 생성합니다.

*   **위치**: `.claude/skills/creative/kie-image-generator/`
*   **주요 모델**:
    *   `gpt4o-image`: 텍스트 렌더링, 사실적 묘사 (약 $0.25)
    *   `flux-kontext-pro`: 예술적 스타일, 빠른 속도 (약 $0.15)
    *   `nano-banana`: 초현실적 물리 표현 (약 $0.10)
    *   `seedream-v4`: 초고속 4K 생성 (약 $0.18)
*   **사용법**:
    ```bash
    # 기본 생성 (인터랙티브 모드)
    python scripts/generate_image.py "neon street style hoodie"

    # 모델 지정 생성
    python scripts/generate_image.py "k-pop idol airport fashion" --model flux-kontext-pro
    ```

### 🎬 Video Production
패션 필름 및 숏폼 영상을 기획하고 생성 가이드를 제공합니다.

*   **위치**: `.claude/skills/creative/video-production/`
*   **기능**: 시나리오 작성, 샷 리스트(Shot List) 구성, AI 영상 생성 프롬프트 도출.

---

## 3. Strategy Skills (전략)

### 📊 Season Review Analyzer
지난 시즌의 판매 데이터와 고객 반응(VOC)을 분석하여 다음 시즌 전략을 도출합니다.

*   **위치**: `.claude/skills/strategy/season-review-analyzer/`
*   **Trigger**: `/start-monthly-review`, "시즌 분석 시작"
*   **입력**: 판매 데이터(CSV), 리뷰 데이터(Text)
*   **출력**: `Season_Strategy.md`, `Product_Dev_Request.md`
*   **실행**:
    ```bash
    python .claude/skills/strategy/season-review-analyzer/analyze.py --mode monthly
    ```

### 📈 Sales Analyzer
판매 데이터를 다각도로 분석하여 인사이트를 제공합니다.

*   **위치**: `.claude/skills/strategy/sales-analyzer/`
*   **기능**: 주간/월간 베스트셀러 추출, 카테고리별 점유율 분석.

---

## 4. Product Skills (상품)

### 💰 Costing (원가 계산)
원부자재 및 공임 데이터를 기반으로 예상 원가와 마진율을 계산합니다.

*   **위치**: `.claude/skills/product/costing/`
*   **기능**: BOM(Bill of Materials) 기반 원가 산출, 타겟 판가 설정 시뮬레이션.

### 📝 Techpack Generator
디자인 정보를 공장 전달용 작업지시서(PDF)로 변환합니다.

*   **위치**: `.claude/skills/product/techpack-generator/`
*   **연동**: `tools/pdf` 스킬을 사용하여 문서를 생성합니다.

---

## 5. Marketing Skills (마케팅)

### 🗺️ Channel Roadmap
브랜드 단계별 최적의 마케팅 채널 믹스를 제안합니다.

*   **위치**: `.claude/skills/marketing/channel-roadmap/`
*   **기능**: 인지도(Awareness) -> 전환(Conversion) 단계별 채널 전략 수립.

### 🎣 Hook Formulas
클릭을 유도하는 카피라이팅 템플릿과 공식을 제공합니다.

*   **위치**: `.claude/skills/marketing/hook-formulas/`
*   **용도**: SNS 캡션, 광고 헤드라인, 이메일 제목 작성.

---

## 6. Tools (유틸리티)

### 📄 PDF Toolkit
패션 비즈니스 리포트 및 룩북 PDF를 생성하고 분석합니다.

*   **위치**: `.claude/skills/tools/pdf/`
*   **기능**: Markdown -> PDF 변환, 룩북 병합, 리포트 데이터 추출.

### 📊 PPTX Generator
시즌 기획서 및 발표 자료(PPT)를 자동으로 생성합니다.

*   **위치**: `.claude/skills/tools/pptx/`
*   **기능**: 텍스트 개요를 슬라이드 형태로 변환.

### 🔐 Auth Manager
외부 API(Kie.ai, Z.ai, Google 등)의 인증 토큰을 관리합니다.

*   **위치**: `.claude/skills/tools/auth-manager/`
*   **기능**: `.env` 파일 로드 및 검증, 토큰 갱신.

---

## 7. 스킬 개발 가이드 (How to Add Skills)

새로운 스킬을 추가하려면 다음 구조를 따르세요.

1.  **폴더 생성**: `.claude/skills/[category]/[skill-name]/`
2.  **설명서 작성**: `SKILL.md` (필수) - 스킬의 목적, 사용법, 입출력 정의.
3.  **스크립트 작성**: Python 또는 Node.js 실행 파일.
4.  **등록**: 에이전트가 사용할 수 있도록 `agents_config.yaml` 또는 에이전트 프롬프트에 언급.

# 와키윌리 패션 하우스 (WACKY WILLY FASHION HOUSE)

**생성일:** 2026-02-02
**시스템:** 가상 패션 하우스 오케스트레이션 V2

## 개요 (OVERVIEW)
와키윌리(Wacky Willy)는 "키치 스트릿(Kitsch Street)"과 "IP 유니버스"를 결합한 글로벌 라이프스타일 브랜드입니다.
이 저장소는 **인피니티 루프 프로토콜(Infinity Loop Protocol)**과 **삼각 성장 엔진(Trinity Growth Engine)**(챔피언 - 글로벌 - IP)에 의해 운영되는 AI 패션 하우스입니다.

## 구조 (STRUCTURE)
```
.
├── .guides/             # [시스템] 가이드, 매뉴얼, 설정 파일
│   ├── setup/           # 설치 및 초기 설정 가이드
│   ├── manuals/         # 업무 매뉴얼 (헌법)
│   └── config/          # 에이전트 설정 파일
├── Sherman's Workspace/ # [데이터] 개인 작업 공간 (Git 제외)
│   ├── 01_Strategy/
│   ├── 02_Creative/
│   ├── 03_Product/
│   ├── 04_Marketing/
│   └── 05_Archive/
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

## 핵심 프로토콜 (KEY PROTOCOLS)
1.  **리뷰에서 전략으로 (Review to Strategy)**: `/start-monthly-review` (챔피언 발굴)
2.  **전략에서 창조로 (Strategy to Creation)**: `/initiate-design-loop` (디자인 & IP 확장)
3.  **창조에서 시장으로 (Creation to Market)**: `/launch-drop` (글로벌 한정판 드롭)
4.  **시장에서 리뷰로 (Market to Review)**: 월간 마감 (리텐션 분석)

## 명령어 (COMMANDS)
```bash
# 가상환경 활성화
source .venv/bin/activate

# 월간 리뷰 실행 (챔피언 발굴)
python .claude/skills/strategy/season-review-analyzer/analyze.py --mode monthly

# IP 캐릭터 생성 (크리에이티브)
python .claude/skills/creative/kie-image-generator/scripts/generate_image.py "KiKi Character 3D"
```

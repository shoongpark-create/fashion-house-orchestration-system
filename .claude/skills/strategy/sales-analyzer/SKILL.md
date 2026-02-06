# Sales Analyzer Skill (판매 분석)

## Overview
주간/월간 판매 데이터를 분석하여 브랜드별 성과, BEST 상품, 채널별 매출, 성장/하락 트렌드를 도출하는 스킬입니다.

## Trigger
- 판매 데이터 분석 요청 시
- "판매 분석", "매출 분석", "BEST 상품 분석" 키워드 포함 시
- Data 폴더의 판매 데이터 파일 분석 요청 시

## Related Skills
- `strategy/brand-comparison`: 복수 브랜드 비교 분석 (이 스킬의 결과를 사용)

## Workflow
```
┌─────────────────────────────────────────────────────────────┐
│  1. 단일 브랜드 분석 (sales-analyzer)                        │
│     └─ 개별 브랜드의 BEST 10, 채널, 카테고리 분석             │
│                          ↓                                  │
│  2. 복수 브랜드 비교 (brand-comparison)                      │
│     └─ 시장 포지션, 강약점, 전략 인사이트 도출                │
└─────────────────────────────────────────────────────────────┘
```

## Inputs
| 항목 | 설명 | 필수 |
|------|------|------|
| `file_path` | 판매 데이터 파일 경로 (.xlsx, .xlsb) | ✅ |
| `brand` | 분석 대상 브랜드 (기본: 와키윌리) | ❌ |
| `period` | 분석 기간 (주간/월간) | ❌ |
| `compare_all` | 전체 브랜드 비교 분석 여부 (기본: false) | ❌ |

## Data Structure
### 예상 데이터 형식 (BEST 10_WB 시트)
```
행 5: 브랜드명, 기간매출
행 6: 점유율, 순위 (1~10)
행 7: 유니, 사진
행 8: 품번
행 9: 품명
행 10: TAG가
행 11: 판매수량
행 12: TAG금액
행 13: 판매금액
행 14: 온라인
행 15: 오프라인
행 16: 면세
행 17: 기타
행 18: 매출비중
행 19: 전주금액
행 20: 전주대비
행 21: 전주순위
행 22: 랭킹증감
행 23: 전체할인율
행 24: 정상할인율
```

### 브랜드별 컬럼 위치
| 브랜드 | 시작 컬럼 | 종료 컬럼 |
|--------|----------|----------|
| 커버낫 | 4 (E) | 13 (N) |
| 와키윌리 | 18 (S) | 27 (AB) |
| 리(LEE) | 32 (AG) | 41 (AP) |

## Analysis Process

### 1. 데이터 로드
```python
import pandas as pd
df = pd.read_excel(file_path, sheet_name='BEST 10_WB', header=None)
```

### 2. 브랜드별 기간 매출 추출
```python
brands = {
    '커버낫': {'col': 4, '매출': df.iloc[5, 4]},
    '와키윌리': {'col': 18, '매출': df.iloc[5, 18]},
    '리(LEE)': {'col': 32, '매출': df.iloc[5, 32]}
}
```

### 3. BEST 10 상품 추출
```python
for i, col in enumerate(range(start_col, start_col + 10)):
    품번 = df.iloc[8, col]
    품명 = df.iloc[9, col]
    TAG가 = df.iloc[10, col]
    판매수량 = df.iloc[11, col]
    판매금액 = df.iloc[13, col]
    온라인 = df.iloc[14, col]
    오프라인 = df.iloc[15, col]
    면세 = df.iloc[16, col]
    전주대비 = df.iloc[20, col]
    할인율 = df.iloc[23, col]
```

### 4. 채널별 분석
- 온라인 비중 = Σ온라인 / Σ판매금액
- 오프라인 비중 = Σ오프라인 / Σ판매금액
- 면세 비중 = Σ면세 / Σ판매금액

### 5. 카테고리 분류
```python
categories = {
    '아우터': ['다운', '점퍼', '자켓', '코트', '푸퍼'],
    '상의': ['후드', '맨투맨', '티셔츠', '니트', '스웻'],
    '하의': ['팬츠', '조거', '진', '쇼츠'],
    '액세서리': ['모자', '가방', '양말']
}
```

### 6. 성장/하락 분석
- 성장: 전주대비 > 0
- 하락: 전주대비 < 0

## Outputs

### 분석 보고서 템플릿
```markdown
# 판매 분석 리포트
**기간**: {period}
**분석일**: {date}

## 1. 브랜드별 매출 현황
| 브랜드 | 매출 | 점유율 |
|--------|------|--------|
| {brand} | {sales}원 | {share}% |

## 2. BEST 10 상품
| 순위 | 품명 | TAG가 | 판매수량 | 판매금액 | 전주대비 |
|------|------|-------|---------|----------|----------|
| {rank} | {name} | ₩{tag_price} | {qty}개 | {sales}원 | {wow}% |

## 3. 채널별 매출
- 오프라인: {offline_share}%
- 면세점: {dutyfree_share}%
- 온라인: {online_share}%

## 4. 카테고리별 분석
| 카테고리 | 매출 비중 | 판매수량 |
|----------|----------|----------|
| {category} | {share}% | {qty}개 |

## 5. 핵심 인사이트

### 성장 상품
{growth_items}

### 하락 상품
{decline_items}

### 전략적 시사점
{insights}
```

## Insights Generation Rules

### 시즌 전환 감지
- 다운/패딩 하락 + 가벼운 상의 상승 → "시즌 전환 시점"
- 반대 패턴 → "겨울 시즌 진입"

### IP 상품 분석
- 키키/캐릭터 포함 상품 성장 → "IP 인지도 상승"
- 로고 상품 강세 → "브랜드 충성도 확인"

### 채널 분석
- 온라인 < 20% → "온라인 채널 강화 필요"
- 면세 > 20% → "인바운드 수요 활성화"

### 할인율 분석
- 평균 할인율 > 40% → "마진 관리 주의"
- 정상 할인율 < 30% → "브랜드 파워 양호"

## Related Skills
- `strategy/pipeline-framework`: 상품 파이프라인 연동
- `strategy/segmentation-framework`: 고객 세그먼트별 분석
- `marketing/channel-roadmap`: 채널 전략 수립

## Dependencies
- pandas
- openpyxl (xlsx 읽기)
- pyxlsb (xlsb 읽기, 선택사항)

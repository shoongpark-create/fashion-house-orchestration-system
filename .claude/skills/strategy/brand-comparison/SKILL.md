# Brand Comparison Skill (브랜드 비교 분석)

## Overview
여러 브랜드의 주간/월간 판매 데이터를 비교 분석하여 시장 포지션, 채널 전략, 강약점을 도출하는 스킬입니다.

## Trigger
- "브랜드 비교", "경쟁사 분석", "세 브랜드 분석" 키워드 포함 시
- 전체 브랜드 현황 파악 요청 시

## Dependencies
- `strategy/sales-analyzer`: 개별 브랜드 분석 선행 필요

## Workflow

### Phase 1: 개별 브랜드 분석
각 브랜드별로 `sales-analyzer` 스킬을 순차 실행
```
1. 커버낫 분석 → covernat_analysis.json
2. 리(LEE) 분석 → lee_analysis.json
3. 와키윌리 분석 → wackywilly_analysis.json
```

### Phase 2: 비교 분석
개별 분석 결과를 종합하여 비교 인사이트 도출

## Inputs
| 항목 | 설명 | 필수 |
|------|------|------|
| `file_path` | 판매 데이터 파일 경로 (.xlsx) | ✅ |
| `brands` | 분석 대상 브랜드 목록 (기본: 커버낫, 와키윌리, 리) | ❌ |
| `focus_brand` | 포커스 브랜드 (기본: 와키윌리) | ❌ |

## Analysis Dimensions

### 1. 매출 구조 비교
- 기간 매출 및 점유율
- BEST 10 매출 집중도
- 전주 대비 성장률

### 2. 채널 전략 비교
| 채널 | 분석 포인트 |
|------|------------|
| 오프라인 | 의존도, 매장 효율 |
| 온라인 | D2C 비중, 성장성 |
| 면세 | 인바운드 수요, 관광 시즌성 |

### 3. 가격 포지셔닝
- 평균 TAG가 비교
- 평균 할인율 비교
- 실구매가 분석

### 4. 상품 카테고리 비교
- 카테고리별 강점/약점
- 히트 상품 유무
- 시즌 상품 비중

### 5. 트렌드 분석
- 성장 상품 공통점
- 하락 상품 공통점
- 시즌 전환 패턴

## Comparison Metrics

### 정량 지표
```python
metrics = {
    '매출': {
        '기간매출': float,
        '점유율': float,
        'BEST10_비중': float
    },
    '채널': {
        '오프라인': float,
        '온라인': float,
        '면세': float
    },
    '가격': {
        '평균TAG가': int,
        '평균할인율': float,
        '실구매가': int
    },
    '성장': {
        '성장상품수': int,
        '하락상품수': int,
        '최고성장률': float
    }
}
```

### 정성 지표
- 브랜드 포지셔닝 (볼륨/가치/차별화)
- 채널 전략 유형 (오프라인 중심/균형/온라인 중심)
- 상품 전략 유형 (카테고리 독점/로고 플레이/IP 차별화)

## Output Structure

### 1. Executive Summary
- 핵심 메시지 (1문장)
- 브랜드별 한줄 요약
- 시장 현황 테이블

### 2. 브랜드별 상세 분석
각 브랜드마다:
- 개요 테이블
- 채널 믹스 시각화
- BEST 10 테이블
- 강점/약점 테이블

### 3. 비교 분석
- 매출 구조 비교
- 채널 전략 비교
- 가격 포지셔닝
- 상품 카테고리 비교

### 4. 트렌드 분석
- 급성장 상품 TOP 5 (전체)
- 급하락 상품 TOP 5 (전체)
- 공통 트렌드

### 5. 전략적 인사이트
- 공통 트렌드
- 브랜드별 차별화 전략
- 포커스 브랜드 실행 권고안

### 6. 결론
- 시장 현황 요약
- 핵심 메시지

## Insight Generation Rules

### 시장 지위 판단
```python
if 점유율 >= 40%:
    position = "시장 리더"
elif 점유율 >= 25%:
    position = "강력한 2위"
else:
    position = "도전자"
```

### 채널 전략 유형
```python
if 오프라인 >= 70%:
    channel_type = "오프라인 의존"
elif 온라인 >= 30%:
    channel_type = "온라인 강세"
elif abs(오프라인 - 면세) < 15:
    channel_type = "균형형"
```

### 브랜드 파워 판단
```python
if 평균할인율 < 30%:
    brand_power = "강함 (가격 유지력)"
elif 평균할인율 > 40%:
    brand_power = "약함 (할인 의존)"
else:
    brand_power = "보통"
```

### 포커스 브랜드 권고안 생성
```python
recommendations = []

if 온라인비중 < 15%:
    recommendations.append({
        '우선순위': '긴급',
        '액션': '온라인 채널 강화',
        '목표': f'{온라인비중}% → 20%'
    })

if 성장상품수 < 하락상품수:
    recommendations.append({
        '우선순위': '단기',
        '액션': '시즌 상품 조기 노출',
        '목표': '다운 의존도 탈피'
    })
```

## Related Skills
- `strategy/sales-analyzer`: 개별 브랜드 분석
- `strategy/pipeline-framework`: 상품 파이프라인 연동
- `marketing/channel-roadmap`: 채널 전략 수립

## Output Files
```
01_Strategy/reports/
├── weekly_brand_comparison_{week}_{year}.md  # 비교 보고서
├── brand_analysis_커버낫_{date}.json          # 개별 분석 데이터
├── brand_analysis_와키윌리_{date}.json
└── brand_analysis_리_{date}.json
```

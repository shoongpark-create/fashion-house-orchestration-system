# QC Checklist Skill (품질 검사)

## Overview
생산 단계별 품질 검사 체크리스트를 생성하고 관리하는 스킬입니다.

## Trigger
- 샘플 검수가 필요할 때
- 벌크 생산 전 품질 기준 설정이 필요할 때
- 입고 검품 기준이 필요할 때

## Inputs
| 항목 | 설명 | 필수 |
|------|------|------|
| `item_category` | 상품 카테고리 (TOP/BOTTOM/ACC) | ✅ |
| `tech_pack_path` | 테크팩 문서 경로 | ✅ |
| `qc_stage` | 검사 단계 (SAMPLE/PRE-PRODUCTION/INLINE/FINAL) | ✅ |

## QC Stages

### 1. Sample QC (샘플 검수)
- 디자인 의도 부합 여부
- 핏/실루엣 확인
- 컬러 매칭 (Pantone 기준)
- 봉제 품질 기초 점검

### 2. Pre-Production QC (생산 전 검수)
- 원부자재 품질 확인
- 사이즈 스펙 검증 (허용 오차 ±1cm)
- 라벨/케어라벨 정확성

### 3. Inline QC (생산 중 검수)
- 공정별 품질 모니터링
- 불량률 추적 (목표: <2%)
- 즉시 시정 조치

### 4. Final QC (최종 검수)
- AQL 2.5 기준 랜덤 샘플링
- 외관/봉제/기능 종합 점검
- 포장 상태 확인

## Outputs
```markdown
## QC Checklist: {item_name}
**Stage**: {qc_stage}
**Date**: YYYY-MM-DD
**Inspector**:

### Inspection Items
| # | Category | Check Point | Standard | Result | Note |
|---|----------|-------------|----------|--------|------|
| 1 | 외관 | 오염/얼룩 | 없음 | ⬜ PASS / ⬜ FAIL | |
| 2 | 외관 | 봉제 불량 | 없음 | ⬜ PASS / ⬜ FAIL | |
| 3 | 치수 | 가슴둘레 | XX±1cm | ⬜ PASS / ⬜ FAIL | |
| ... | | | | | |

### Summary
- Total Items: XX
- Pass: XX
- Fail: XX
- Pass Rate: XX%

### Decision
⬜ APPROVED  ⬜ CONDITIONAL  ⬜ REJECTED

### Corrective Actions Required
1.
2.
```

## Defect Categories
| 등급 | 정의 | 예시 |
|------|------|------|
| **Critical** | 안전/법규 위반 | 날카로운 부자재, 잘못된 케어라벨 |
| **Major** | 판매 불가 | 구멍, 심한 오염, 치수 불량 |
| **Minor** | 경미한 결함 | 작은 올 풀림, 미세 오염 |

## Rules
- Critical 불량 발견 시 즉시 생산 중단 권고
- 모든 검사 결과는 사진 증빙 첨부
- 불합격 시 재검사 필수

## Related Skills
- `product/costing`: 원가에 영향을 주는 품질 이슈 연동
- `product/techpack-generator`: 테크팩 기준 참조

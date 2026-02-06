# Costing Skill (원가 계산)

## Overview
상품의 원가를 산출하고 타겟 마진 달성 여부를 검증하는 스킬입니다.

## Trigger
- 디자인 시안이 완성되어 Pre-Costing이 필요할 때
- 생산 전 Final Costing 확정이 필요할 때

## Inputs
| 항목 | 설명 | 필수 |
|------|------|------|
| `design_spec` | 디자인 스펙 문서 경로 | ✅ |
| `target_cost` | 타겟 원가 (KRW) | ✅ |
| `target_margin` | 목표 마진율 (%) | ✅ |
| `quantity` | 예상 생산 수량 | ✅ |

## Process
1. **자재비 산출 (Material Cost)**
   - 원단: 사용량 × 단가
   - 부자재: 지퍼, 버튼, 라벨 등
   - 포장재: 택, 행거, 폴리백

2. **가공비 산출 (Labor Cost)**
   - 봉제비: 난이도 × 기본 공임
   - 후가공: 워싱, 프린트, 자수 등

3. **간접비 배분 (Overhead)**
   - 물류비, 검품비, 관리비

4. **마진 검증**
   - 판매가 역산 = 원가 ÷ (1 - 마진율)
   - 시장가 대비 경쟁력 평가

## Outputs
```markdown
## Costing Report: {item_name}

### Summary
- **Total Cost**: ₩XX,XXX
- **Target Cost**: ₩XX,XXX
- **Status**: ✅ PASS / ❌ OVER BUDGET

### Cost Breakdown
| Category | Amount | % |
|----------|--------|---|
| Material | ₩XX,XXX | XX% |
| Labor | ₩XX,XXX | XX% |
| Overhead | ₩XX,XXX | XX% |

### Margin Analysis
- Suggested Retail Price: ₩XXX,XXX
- Gross Margin: XX%
```

## Rules
- 추정치 사용 금지. 공급업체 견적 기반으로만 산출
- 타겟 원가 초과 시 자동으로 VE(Value Engineering) 제안
- 모든 금액은 KRW 기준, 소수점 이하 절사

## Related Skills
- `product/qc-checklist`: 품질 검사 체크리스트
- `strategy/pipeline-framework`: 상품 파이프라인 관리

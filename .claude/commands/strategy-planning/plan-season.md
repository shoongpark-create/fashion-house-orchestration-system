---
name: plan-season
description: 26SS 시즌의 전체적인 머천다이징 계획(Merchandising Plan)을 수립합니다.
usage: /plan-season [season_keyword]
---

# /plan-season

시즌 기획 프로세스를 자동으로 실행합니다. 트렌드 분석부터 SKU 계획까지 한 번에 연결합니다.

## Steps

1.  **Trend Discovery**
    -   **Agent**: `market-researcher`
    -   **Action**: 입력된 키워드(또는 26SS) 기반 마이크로 트렌드 분석
    -   **Output**: Trend Brief

2.  **Concept Definition**
    -   **Agent**: `chief-merchandiser`
    -   **Action**: 트렌드를 브랜드(Kitsch Street)에 맞게 재해석하여 시즌 테마 정의
    -   **Output**: Season Concept Note

3.  **Line Sheet Planning**
    -   **Agent**: `collection-planner`
    -   **Action**: 카테고리별 아이템 구성 및 물량(SKU) 계획 수립
    -   **Output**: Preliminary Line Sheet (Table)

## Example
```bash
/plan-season "Y2K Grunge"
```

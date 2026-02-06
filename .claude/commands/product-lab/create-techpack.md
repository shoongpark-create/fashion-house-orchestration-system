---
name: create-techpack
description: 디자인을 생산 가능한 형태의 기술 문서(Tech Pack)로 변환합니다.
usage: /create-techpack [design_image_path]
---

# /create-techpack

`production-manager` (GLM-4.7)가 이미지를 분석(또는 텍스트 설명을 기반으로)하여 공장용 작업지시서를 작성합니다.

## Steps

1.  **Spec Definition**
    -   **Agent**: `production-manager`
    -   **Action**: BOM(소요량) 산출 및 원부자재 스펙 정의
    -   **Output**: BOM Table

2.  **Measurement Setting**
    -   **Agent**: `production-manager`
    -   **Action**: 기준 사이즈(Sample Size) 및 그레이딩 편차 설정
    -   **Output**: Size Spec Sheet

3.  **Costing**
    -   **Agent**: `production-manager`
    -   **Action**: 예상 공임 및 원가 산출 (Target Costing)
    -   **Output**: Cost Sheet

## Example
```bash
/create-techpack "planning/delivery_26SS/design_draft_01.png"
```

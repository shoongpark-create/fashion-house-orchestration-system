---
name: design-drop
description: 기획된 아이템을 시각화(Visualizing)하고 디자인 드래프트를 생성합니다.
usage: /design-drop [item_name]
---

# /design-drop

텍스트로 된 기획안을 눈에 보이는 '옷'으로 만듭니다. `kie-image-generator`의 Fashion Mode를 적극 활용합니다.

## Steps

1.  **Visual Direction**
    -   **Agent**: `creative-director`
    -   **Action**: 해당 아이템에 적합한 무드, 조명, 앵글 설정 (Art Direction)
    -   **Output**: Image Prompt Brief

2.  **Design Draft Generation**
    -   **Agent**: `fashion-designer`
    -   **Action**: `kie-image-generator`를 호출하여 실제 이미지 생성
    -   **Mode**: 
        -   `--fashion-mode lookbook`: 모델 착용 컷 (Vibe 확인용)
        -   `--fashion-mode flat`: 도식화 (디테일 확인용)
    -   **Output**: Design Images (PNG)

## Example
```bash
/design-drop "Neon Pink Oversized Hoodie"
```

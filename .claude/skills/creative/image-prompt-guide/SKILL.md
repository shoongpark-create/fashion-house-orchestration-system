---
name: image-prompt-guide
description: 패션 이미지(Lookbook, Flat, Detail) 생성을 위한 프롬프트 가이드 (Fashion Edition)
version: 2.0.0
author: Wacky Willy Fashion House
tags:
  - image
  - prompt
  - fashion
  - lookbook
---

# Fashion Image Prompt Guide

AI 이미지 생성기(`kie-image-generator`)를 활용해 고퀄리티 패션 이미지를 생성하기 위한 전문 프롬프트 가이드입니다.

## Prompt Structure (Fashion Optimized)

```
[Item/Subject] + [Fabric/Detail] + [Style/Vibe] + [Lighting/Environment] + [Angle] + [Quality]
```

### Key Elements
1.  **Item**: 카테고리 (Hoodie, Cargo Pants), 핏 (Oversized, Cropped)
2.  **Fabric**: 소재감 (Heavyweight Cotton, Nylon Metal, Distressed Denim)
3.  **Detail**: 디테일 (Raw edge, Neon piping, Puff print, Embroidery)
4.  **Vibe**: 무드 (Kitsch, Grunge, Y2K, High-end Street)

## Prompt Templates by Mode

### 1. Lookbook Mode (화보)
*   **Goal**: 모델 착용 컷, 브랜드 무드 전달
*   **Prompt**:
    ```
    "Fashion editorial photography of a cool Gen Z model wearing [Neon Pink Oversized Hoodie],
    standing in [Seoul street alleyway at night],
    neon sign lighting, cinematic color grading,
    confident pose, Kitsch street style,
    shot on Hasselblad, 8k resolution, depth of field"
    ```

### 2. Ghost Mode (누끼)
*   **Goal**: 제품 디테일 확인, 쇼핑몰 상세페이지용
*   **Prompt**:
    ```
    "Invisible ghost mannequin shot of [Neon Pink Oversized Hoodie],
    front view, clean white background,
    studio lighting, soft shadows,
    high detailed fabric texture, 30s cotton french terry,
    e-commerce photography, 4k"
    ```

### 3. Flat Mode (도식화)
*   **Goal**: 작업지시서용, 디자인 구조 확인
*   **Prompt**:
    ```
    "Technical flat sketch of [Oversized Hoodie],
    black and white line drawing, vector style,
    front and back view, minimal, clean lines,
    blueprint aesthetic, fashion design illustration"
    ```

### 4. Detail Mode (질감)
*   **Goal**: 소재 및 봉제 디테일 확인
*   **Prompt**:
    ```
    "Macro close-up shot of [Neon Pink Hoodie fabric],
    focus on [Raw edge stitching detail],
    extreme detail of cotton texture,
    soft lighting, 4k texture, realistic"
    ```

## Fashion Keywords Dictionary

### Fabric & Texture
*   **Cotton**: French Terry, Jersey, Heavyweight (쭈리, 싱글, 고중량)
*   **Synthetic**: Nylon Washer, Mesh, Ripstop (나일론, 메쉬, 립스탑)
*   **Denim**: Washed, Raw, Distressed (워싱, 생지, 데미지)
*   **Knits**: Cable, Ribbed, Mohair (케이블, 골지, 모헤어)

### Details
*   **Stitch**: Contrast stitch, Zigzag, Overlock (배색 스티치)
*   **Print**: Puff, Rubber, Crack, Digital (발포, 라바, 크랙, 전사)
*   **Hardware**: YKK Zipper, Eyelet, Stopper (지퍼, 아일렛, 스토퍼)

## Negative Prompts (Avoid)
```
"low quality, blurry, distorted, ugly face,
bad proportions, watermark, text, logo,
extra limbs, mutated hands, plastic skin"
```

## Usage
이 스킬은 `creative-director`와 `fashion-designer`가 `/design-drop` 명령 실행 시 참조합니다.

---
name: pptx
description: 패션 캠페인 및 시즌 기획서(PPT) 제작 도구
version: 2.0.0
author: Wacky Willy Fashion House
tags:
  - presentation
  - fashion
  - campaign
  - deck
---

# Fashion Presentation Toolkit

마케팅 캠페인 덱(Deck), 시즌 기획서, 브랜드 소개서를 PPTX로 자동 생성하는 도구입니다.

## Fashion Deck Templates

### 1. Season Concept Deck
*   **Slide 1 (Title)**: "26SS Wacky Chaos Collection"
*   **Slide 2 (Moodboard)**: 키 비주얼 및 컬러 팔레트 이미지
*   **Slide 3 (Line Sheet)**: SKU 구성표 및 가격 정책
*   **Slide 4 (Schedule)**: Drop 1, Drop 2 발매 일정

### 2. Campaign Proposal
*   **Target**: Gen Z / Alpha
*   **Key Message**: "Unpredictable Fun"
*   **Channel Mix**: Instagram (Teasing) → Pop-up (Experience) → TikTok (Viral)

## HTML to PPTX (Fashion Style)

```html
<style>
  :root {
    --brand-neon: #FF00FF; /* Wacky Pink */
    --brand-black: #111111;
  }
  h1 { font-family: 'Helvetica Neue', sans-serif; color: var(--brand-neon); }
</style>
<div class="slide">
  <h1>26SS DROP 1</h1>
  <img src="lookbook_hero.jpg" />
  <p>Launch Date: 2026.03.01</p>
</div>
```

## File Storage (Naming Convention)

*   **Campaign Deck**: `reports/presentations/campaign-26ss-{date}.pptx`
*   **Brand Intro**: `reports/presentations/brand-intro-wacky-willy.pptx`

## Usage
이 스킬은 `marketing-director`와 `chief-merchandiser`가 시즌 기획 발표 자료 생성 시 사용합니다.

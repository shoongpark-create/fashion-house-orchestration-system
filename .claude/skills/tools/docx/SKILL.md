---
name: docx
description: 패션 브랜드 가이드라인 및 기획서 문서(DOCX) 생성 도구
version: 2.0.0
author: Wacky Willy Fashion House
tags:
  - document
  - word
  - fashion
  - guidelines
---

# Fashion Document Toolkit

브랜드 가이드라인(VMD/Tone&Manner)과 캠페인 기획서를 Word 문서로 생성합니다.

## Document Templates

### 1. Brand Guideline (VMD Manual)
*   **Logo**: 최소 사이즈, 금지 규정 (Clear Space)
*   **Color**: Neon Pink (#FF00FF), Acid Green (#CCFF00)
*   **Typography**: 헤드라인(Bold Sans), 본문(Monospace)

### 2. Campaign Brief
*   **Objective**: 신규 고객 유입 30% 증대
*   **Target**: Gen Z (18-24)
*   **Key Message**: "Unpredictable Fun"
*   **Budget**: Total 5,000만원 (Media 60%, Production 40%)

## Template Variables

```python
replacements = {
    "{{BrandName}}": "Wacky Willy",
    "{{Season}}": "26SS",
    "{{Item}}": "Pajama Set",
    "{{Manager}}": "Marketing Director"
}
```

## File Storage

*   **Brand Guide**: `reports/documents/brand-guide-v2.docx`
*   **Brief**: `reports/documents/brief-26ss-campaign.docx`

## Usage
이 스킬은 `brand-manager`가 가이드라인 배포 시 사용합니다.

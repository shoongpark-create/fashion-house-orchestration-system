---
name: pipeline-framework
description: 패션 런칭 캠페인 파이프라인 설계 프레임워크 (Fashion Edition)
version: 2.0.0
author: Wacky Willy Fashion House
tags:
  - campaign
  - pipeline
  - fashion
  - orchestration
---

# Fashion Launch Pipeline Framework

신상품 런칭(Drop)을 위한 표준 파이프라인입니다.

## Pipeline Overview

```
[Phase 1: Teasing] (D-14)
    ↓
Lookbook 공개, 기대평 이벤트, 알림 신청
    ↓
[Phase 2: Main Drop] (D-Day)
    ↓
자사몰/무신사 오픈, 인플루언서 착용샷 업로드
    ↓
[Phase 3: Sustain] (D+7)
    ↓
고객 리뷰 확산, 베스트셀러 랭킹 마케팅
```

## Agent Mapping

| Phase | Primary Agents | Output |
|-------|---------------|--------|
| **Plan** | `chief-merchandiser` | Line Sheet |
| **Design** | `creative-director` | Lookbook |
| **Prod** | `production-manager` | Tech Pack |
| **Mkt** | `marketing-director` | Campaign Brief |

## Usage
이 스킬은 `campaign-director`가 런칭 스케줄링 시 사용합니다.

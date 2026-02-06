---
name: auth-manager
description: 외부 API 인증 관리 도구 (Fashion Edition)
version: 2.0.0
author: Wacky Willy Fashion House
tags:
  - auth
  - security
  - api
---

# Auth Manager

Wacky Willy 시스템이 사용하는 외부 서비스(Z.ai, Kie.ai, Playwright 등)의 인증 정보를 안전하게 관리합니다.

## Supported Services

| Service | Env Var | Description |
|---------|---------|-------------|
| **Z.ai (GLM)** | `ZHIPUAI_API_KEY` | Coding Plan (GLM-4.7) for Tech Pack |
| **Kie.ai** | `KIE_API_KEY` | Image/Video Generation for Lookbook |
| **Gemini** | `GEMINI_API_KEY` | Orchestration Brain |

## Usage
`.env` 파일을 통해 로드됩니다.

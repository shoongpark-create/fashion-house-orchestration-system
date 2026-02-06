# 🛠️ Wacky Willy System Installation & Setup Guide

이 가이드는 **Antigravity CLI**와 **Oh-My-OpenCode** 플러그인을 기반으로, **Google Gemini Pro 구독 계정**과 **Z.ai GLM API**를 연동하여 시스템을 구축하는 방법을 설명합니다.

---

## 1. 사전 준비 (Prerequisites)

시스템 구동을 위해 다음 계정 및 API Key가 필수적으로 필요합니다.

### 🔑 1) Gemini Pro 구독 계정 (for Antigravity)
Antigravity CLI는 **API Key 방식이 아닌**, **Google 구독 계정 연동** 방식으로 Gemini Pro 모델에 접근합니다.

**준비 단계:**
1.  [Google One AI Premium](https://one.google.com/explore-plan/gemini-advanced) 접속
2.  **Gemini Advanced** 플랜 구독 (월 $19.99, Gemini Pro 모델 무제한 사용)
3.  구독한 **Google 계정 이메일 주소**를 준비하세요.
    *   예시: `your-email@gmail.com`

**중요:** Antigravity는 이 구독 계정으로 **자동 로그인**하여 Gemini Pro를 호출합니다. API Key는 불필요합니다.

### 🔑 2) Z.ai API Key (for Hephaestus/GLM)
GLM-4 Plus 모델은 **Z.ai의 API를 직접 호출**하는 방식입니다.

**준비 단계:**
1.  [Z.ai Console](https://www.z.ai/) 접속
2.  회원가입 후 **API Key 발급** (대시보드 → API 관리)
3.  GLM-4 Plus 모델 사용 권한이 활성화되어 있는지 확인
4.  발급받은 API Key를 복사해두세요.
    *   형식: `zai_xxxxxxxxxxxxxxxx`

### 💻 소프트웨어 요구사항
*   Python 3.10 이상
*   Git
*   Oh-My-OpenCode (Obsidian Plugin or Standalone CLI)
*   **Antigravity CLI** (구글 계정 연동 기능 포함)

---

## 2. 설치 (Installation)

터미널(Terminal)을 열고 다음 단계를 순서대로 진행하세요.

### 1) 프로젝트 클론
```bash
# 프로젝트 폴더로 이동 (예시 경로)
cd "/Users/sherman/Library/Mobile Documents/iCloud~md~obsidian/Documents/Sherman/00. Inbox/09. Opencode"
```

### 2) 가상환경 설정
Python 패키지 충돌 방지를 위해 가상환경을 사용합니다.
```bash
# 가상환경 생성
python3 -m venv .venv

# 가상환경 활성화
source .venv/bin/activate
```

### 3) 의존성 설치
```bash
pip install -r requirements.txt
```
*(만약 `requirements.txt`가 없다면, `pip install google-generativeai zhipuai` 등을 통해 필요한 라이브러리를 설치하세요.)*

---

## 3. 환경 설정 (Configuration)

### 1) Antigravity CLI 계정 연동
Antigravity는 Google 구독 계정을 통해 Gemini Pro에 접근합니다.

**설정 방법:**
```bash
# Antigravity CLI 계정 로그인
antigravity auth login

# 브라우저가 자동으로 열리면, Gemini Advanced 구독 계정으로 로그인
# 로그인 완료 후 터미널로 돌아와 확인
antigravity auth status
```

**예상 출력:**
```
✅ Logged in as: your-email@gmail.com
✅ Gemini Pro Access: Active
```

### 2) Z.ai API Key 등록
GLM-4 Plus(유료/고성능) 및 GLM-4 Flash(무료/고속) 모델 접근을 위해 API Key를 등록합니다.
이 키 하나로 **Hephaestus**와 **Creative Agents** 모두 작동합니다.

**설정 방법:**
프로젝트 루트에 `.env` 파일을 생성하고 아래 내용을 입력하세요.

```bash
# .env file

# Z.ai API Key (통합 키)
Z_AI_API_KEY="zai_xxxxxxxxxxxxxxxx"

# Oh-My-OpenCode 모델 매핑 설정
# hephaestus -> glm-4-flash (Free)
# ip_artist -> glm-4-plus (High Performance)
OMO_MODEL_MAPPING="hephaestus:glm-4-flash,ip_artist:glm-4-plus"
```

---

## 4. 연결 점검 (Verification)

4대 에이전트가 정상적으로 모델과 연결되었는지 확인합니다.

### 🧪 방법 1: Antigravity CLI 직접 테스트
```bash
# Sisyphus (Antigravity) Check
antigravity chat "Hello Sisyphus, status report."
```

### 🧪 방법 2: Python 스크립트로 통합 점검 (Final)
아래 코드를 `test_connection.py`로 저장하고 실행하세요.

```python
import os
import subprocess
from dotenv import load_dotenv

load_dotenv()

def check_agents():
    print("🔌 Wacky Willy System Connection Check (V3.4)...\n")

    # 1. Antigravity (Google Gemini Pro)
    print("1️⃣ Testing Antigravity (Sisyphus/Prometheus/Atlas)...")
    try:
        result = subprocess.run(["antigravity", "auth", "status"], capture_output=True, text=True)
        if "Active" in result.stdout:
            print("   ✅ Gemini Pro Connected! (Google Subscription)\n")
        else:
            print("   ❌ Login Required (Run: 'antigravity auth login')\n")
    except:
        print("   ❌ CLI Error.\n")

    # 2. Z.ai (Hephaestus & Creative Agents)
    print("2️⃣ Testing Z.ai Agents (Hephaestus/IP Artist)...")
    z_key = os.getenv("Z_AI_API_KEY")
    
    if z_key and z_key.startswith("zai_"):
        print(f"   ✅ Z.ai API Key Detected! ({z_key[:6]}...)")
        print("   ✅ Hephaestus: Ready (Model: GLM-4-Flash / Free)")
        print("   ✅ IP Artist : Ready (Model: GLM-4-Plus)\n")
    else:
        print("   ❌ Missing Z_AI_API_KEY in .env")
        print("      -> Hephaestus & Creative Agents will fail.\n")

    print("=" * 50)
    print("✨ System Ready! if all green.")

if __name__ == "__main__":
    check_agents()
```

**실행 명령어:**
```bash
python test_connection.py
```

---

## 5. 문제 해결 (Troubleshooting)

### ❌ "Antigravity: Not authenticated"
**원인:** Google 계정 로그인이 필요합니다.
**해결:**
```bash
antigravity auth login
# 브라우저에서 Gemini Advanced 구독 계정으로 로그인
```

### ❌ "Z.ai API: 401 Unauthorized"
**원인:** API Key가 잘못되었거나 만료되었습니다.
**해결:**
1. [Z.ai Console](https://www.z.ai/)에서 키를 재발급하세요.
2. `.env` 파일의 `Z_AI_API_KEY` 값을 업데이트하세요.

### ❌ "Gemini Pro Access: Inactive"
**원인:** Google One AI Premium 구독이 활성화되지 않았습니다.
**해결:**
1. [Google One 구독 관리](https://one.google.com/storage)에서 플랜을 확인하세요.
2. Gemini Advanced가 포함된 플랜인지 확인하세요.

### ❌ Rate Limit 에러
**원인:** 
- **Gemini**: 구독 계정은 제한이 거의 없으나, 동시 요청 수 제한이 있을 수 있습니다.
- **Z.ai**: 무료 티어 사용량 초과.
**해결:** 잠시 대기 후 재시도하거나, Z.ai 유료 플랜으로 업그레이드하세요.

---

## 6. 다음 단계 (Next Steps)

✅ 설치와 연결이 완료되었다면, 이제 시스템을 사용할 준비가 끝났습니다!

**초보자 가이드로 이동:**
```bash
# Onboarding Guide 읽기
cat 00_System/Onboarding_Guide.md
```

**첫 명령어 실행:**
```bash
# Sisyphus에게 월간 리뷰 시작 명령
/start-monthly-review
```

**시스템 구성 확인:**
```bash
# 4대 에이전트 역할 확인
cat 00_System/agents_config.yaml
```

---

**🎉 환영합니다! 이제 당신은 AI 패션 하우스의 총괄 디렉터입니다.**

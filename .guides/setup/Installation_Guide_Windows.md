# 🪟 Wacky Willy System Installation Guide (For Windows)

이 가이드는 **Windows 10/11** 환경에서 **PowerShell**을 사용하여 시스템을 구축하는 방법을 설명합니다.
Mac/Linux 사용자는 `Installation_Guide.md`를 참고하세요.

---

## 1. 사전 준비 (Prerequisites)

### ✅ 필수 프로그램 설치
1.  **Python 3.10 이상**
    *   [Python 공식 홈페이지](https://www.python.org/downloads/windows/)에서 다운로드.
    *   🚨 **설치 시 주의사항**: 설치 화면 하단의 **"Add Python to PATH"** 체크박스를 **반드시** 선택해야 합니다.
2.  **Git for Windows**
    *   [Git 다운로드](https://git-scm.com/download/win) 및 설치.
3.  **VS Code (권장)** 또는 **Obsidian**

### 🔑 계정 및 키 준비
1.  **Google 계정 (Gemini Pro)**
    *   Antigravity용. Google One AI Premium 구독이 필요합니다.
2.  **OpenCode Zen API Key**
    *   Hephaestus용. `sk-`로 시작하는 키를 준비하세요.

---

## 2. 설치 (Installation)

**PowerShell**을 관리자 권한으로 실행하거나, VS Code 내의 터미널을 사용하세요.

### 1) 프로젝트 폴더로 이동
```powershell
# 예시 경로 (본인의 폴더 경로에 맞게 수정하세요)
# 팁: 폴더를 터미널로 드래그하면 경로가 자동 입력됩니다.
cd "C:\Users\Sherman\Documents\Opencode"
```

### 2) 가상환경(Virtual Environment) 설정
Windows에서는 보안 정책 때문에 스크립트 실행 권한 설정이 필요할 수 있습니다.

```powershell
# 1. 가상환경 생성
python -m venv .venv

# 2. 실행 권한 부여 (오류 발생 시 실행)
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser

# 3. 가상환경 활성화 (경로 주의: 백슬래시 \)
.\.venv\Scripts\Activate.ps1
```
*(터미널 앞부분에 `(.venv)`가 초록색으로 표시되면 성공입니다.)*

### 3) 라이브러리 설치
```powershell
pip install -r requirements.txt
```

---

## 3. 환경 설정 (Configuration)

API Key를 등록합니다. Windows 메모장(Notepad)을 사용하여 생성합니다.

### 1) .env 파일 생성
아래 명령어를 입력하면 메모장이 열립니다. 내용을 붙여넣고 저장하세요.

```powershell
notepad .env
```

**붙여넣을 내용:**
```ini
# .env file

# 1. OpenCode Zen API Key (Hephaestus-Local용)
OPENCODE_API_KEY="sk-여기에_키를_붙여넣으세요"
OPENAI_API_KEY="sk-여기에_키를_붙여넣으세요"

# 2. System Configuration
# 로컬 에이전트와 GPT-4o 연결 매핑
OMO_MODEL_MAPPING="Hephaestus-Local:gpt-4o,ip_artist:gpt-4o"
PYTHONPATH=.
```

### 2) Antigravity 로그인 (Google 구독)
```powershell
antigravity auth login
```
*   브라우저가 열리면 Google 계정으로 로그인하고 권한을 허용하세요.

---

## 4. 연결 점검 (Verification)

### 🧪 연결 테스트
시스템이 정상 작동하는지 확인합니다.

```powershell
python test_connection.py
```

**정상 결과 예시:**
```text
🔌 Wacky Willy System Connection Check...

1️⃣ Testing Antigravity...
   ✅ Gemini Pro Connected!

2️⃣ Testing Z.ai / OpenCode Zen...
   ✅ Z.ai API Key Detected! (또는 OpenCode Key 확인)
   ✅ Hephaestus: Ready (Model: GPT-4o)
```

---

## 5. 자주 발생하는 오류 (Troubleshooting)

### ❌ "이 시스템에서 스크립트를 실행할 수 없으므로..." 오류
*   **해결**: 위 '2. 설치' 단계의 `Set-ExecutionPolicy` 명령어를 실행했는지 확인하세요.

### ❌ "python은 내부 또는 외부 명령이 아닙니다"
*   **해결**: Python 설치 시 **"Add Python to PATH"**를 체크하지 않은 경우입니다. Python을 삭제하고 다시 설치하며 체크박스를 선택하세요.

### ❌ Hephaestus가 결제를 요구함
*   **해결**:
    1.  Obsidian 플러그인 설정에서 **"Reload Agents"** 클릭.
    2.  에이전트 목록에서 `Hephaestus`가 아닌 **`Hephaestus-Local`**을 선택해서 사용하세요.

---
**이제 Windows에서도 Wacky Willy 패션 하우스를 운영할 준비가 되었습니다!**

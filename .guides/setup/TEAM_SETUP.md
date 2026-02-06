# 🚀 Wacky Willy Team Setup Guide

팀원 여러분 환영합니다! 이 가이드를 따라 **3분 안에** 업무 환경을 세팅하세요.

---

## 1. 프로젝트 가져오기 (Clone)

터미널을 열고 저장소를 클론합니다.

```bash
git clone [저장소_URL]
cd [프로젝트_폴더명]
```

## 1.5 작업 공간 만들기 (중요!)

이 저장소에는 시스템 설정만 들어있습니다. 본인의 작업 폴더를 생성하세요.

```bash
# 예: Gildong's Workspace
mkdir "My_Workspace"
```
*   생성한 폴더 안에 필요한 업무 폴더(`01_Strategy` 등)를 만들어 사용하세요.
*   (자세한 구조는 `.guides/Fashion_House_Manual.md` 참고)

---

## 2. 필수 프로그램 설치 (Python)

*   **Windows**: [설치 가이드 보기](Installation_Guide_Windows.md)
*   **Mac**: [설치 가이드 보기](Installation_Guide.md)

**가상환경 생성 및 실행 (공통):**
```bash
# 가상환경 만들기
python3 -m venv .venv

# 켜기 (Mac)
source .venv/bin/activate

# 켜기 (Windows)
.\.venv\Scripts\Activate.ps1

# 라이브러리 설치
pip install -r requirements.txt
```

---

## 3. 비밀 열쇠 설정 (.env)

API 키 설정을 위해 템플릿 파일을 복사합니다.

```bash
# 템플릿 복사
cp .env.example .env
```

이제 `.env` 파일을 열고(`code .env` 또는 메모장) **API 키를 입력**하세요.
*   **OPENCODE_API_KEY**: 팀장님에게 받은 키 (`sk-...`) 입력.
*   나머지는 기본값 유지.

---

## 4. Antigravity 로그인 (Google 계정)

Google Gemini Pro 모델을 쓰기 위해 로그인이 필요합니다.

```bash
antigravity auth login
```
*   브라우저가 뜨면 **Google 계정**으로 로그인하세요.

---

## 5. 최종 점검

모든 게 잘 됐는지 테스트해봅시다.

```bash
python test_connection.py
```

초록색 체크(✅)가 뜨면 성공입니다!
이제 **Sisyphus**에게 말을 걸어보세요.

> "Sisyphus, 오늘 일정 브리핑해줘."

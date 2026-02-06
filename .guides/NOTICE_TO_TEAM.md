# 📢 [공지] Wacky Willy 시스템 배포 및 설치 안내

팀원 여러분, 와키윌리 AI 패션 하우스 시스템(V3.3)이 배포되었습니다.
아래 순서대로 설치하여 개인 작업 환경을 세팅해 주세요.

## ✅ 1. 사전 준비물
1.  **GitHub 계정** (저장소 접근 권한 필요)
2.  **OpenCode Zen API Key** (`sk-xxx`) - 팀장에게 별도 문의
3.  **Google 계정** (Gemini 구독 계정 - Antigravity 로그인용)

## 🚀 2. 설치 방법 (3분 소요)

**Step 1. 터미널(Terminal) 열기**
*   Windows: PowerShell (관리자 권한 권장)
*   Mac: Terminal

**Step 2. 저장소 클론 (Clone)**
```bash
git clone https://github.com/shoongpark-create/fashion-house-orchestration-system
cd fashion-house-orchestration-system
```

**Step 3. 설정 가이드 실행**
다운로드된 폴더 안의 **`.guides/setup/TEAM_SETUP.md`** 파일을 열어서 그대로 따라 하세요.
*   가상환경 생성 (`python -m venv ...`)
*   API Key 입력 (`cp .env.example .env`)
*   로그인 (`antigravity auth login`)

## 💡 3. 참고 문서
설치가 완료되면 아래 문서들을 확인하세요.

*   **시스템 매뉴얼**: `.guides/manuals/Fashion_House_Manual.md`
    *   전체 시스템 구조와 에이전트 역할 정의
*   **스킬 사용법**: `.guides/manuals/Skills_Guide.md`
    *   이미지 생성, 데이터 분석 등 구체적인 도구 사용법

## ❓ 문의사항
설치 중 문제가 발생하면 Sisyphus에게 물어보세요!
> "Sisyphus, 시스템 점검해줘."

---
**[팀장님 체크리스트]**
1.  GitHub 저장소가 **Private**인 경우, 팀원들을 **Collaborator**로 초대했는지 확인하세요.
2.  `sk-`로 시작하는 **API Key**를 팀원들에게 보안 채널(DM 등)로 전달해 주세요.

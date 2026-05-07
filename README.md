# 투자 시나리오 생성 웹앱 (Python + Streamlit + OpenAI)

종목과 투자 논리를 입력하면 **Bull / Base / Bear 시나리오**와 **핵심 변수**를 자동 생성하는 초보자용 웹앱입니다.

## 1) 프로젝트 구조

```bash
.
├── app.py
├── requirements.txt
├── .env.example
└── src
    ├── prompts.py
    └── scenario_generator.py
```

## 2) 사전 준비

- Python 3.10+
- OpenAI API 키

## 3) 실행 방법 (초보자 기준)

### Step 1. 프로젝트 폴더로 이동
```bash
cd /workspace/master
```

### Step 2. 가상환경 만들기
```bash
python -m venv .venv
```

### Step 3. 가상환경 활성화
- macOS/Linux
```bash
source .venv/bin/activate
```
- Windows(PowerShell)
```powershell
.venv\Scripts\Activate.ps1
```

### Step 4. 패키지 설치
```bash
pip install -r requirements.txt
```

### Step 5. 환경변수 파일 만들기
`.env.example`을 복사해 `.env`를 만들고 API 키를 넣으세요.

```bash
cp .env.example .env
```

`.env` 파일 내용:
```env
OPENAI_API_KEY=여기에_본인_API_키
```

### Step 6. 앱 실행
```bash
streamlit run app.py
```

브라우저가 열리면 아래 순서로 사용하세요:
1. 종목 입력
2. 투자 논리 입력
3. 시나리오 생성 버튼 클릭
4. Bull/Base/Bear + 핵심 변수 확인

## 4) 자주 나는 오류

- `OPENAI_API_KEY가 설정되어 있지 않습니다.`
  - `.env` 파일 위치/키 값을 확인하세요.
- `ModuleNotFoundError`
  - 가상환경 활성화 후 `pip install -r requirements.txt`를 다시 실행하세요.

## 5) 확장 아이디어

- 결과를 표/차트로 시각화
- 과거 시나리오 저장(SQLite)
- 기업 실적 요약 자동 첨부

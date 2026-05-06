# Investment Committee Agent (Beginner-Friendly)

초보자가 단계별로 에이전트를 생성/검토하도록 만든 템플릿입니다.

## 실행 예시

```bash
python -m app.main --step 1 --ticker 005930
python -m app.main --step 2 --ticker 005930
python -m app.main --step 3 --ticker 005930
python -m app.main --step 4 --ticker 005930
python -m app.main --step 5 --ticker 005930
```

## 단계 설명

1. DataAgent: 종목 정규화 + 기본 데이터 구성
2. FinancialAgent: 규칙 기반 재무 점수화
3. ReportAgent: 리포트 요약/편향 체크
4. DebateAgent: 거장 관점 토론 결과 정리
5. CIOAgent: 최종 의견 + 목표주가(베어/베이스/불)

## 참고

- 삼성전자(`005930`)는 학습용 mock 데이터가 포함되어 즉시 시연 가능합니다.
- 투자판단 책임은 사용자에게 있습니다.

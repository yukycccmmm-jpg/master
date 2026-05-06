from __future__ import annotations

from datetime import date

from app.schemas import CompanyData, FinancialSnapshot


class DataAgent:
    """Step 1: 데이터 수집/정규화 담당 (학습용 mock 포함)."""

    def run(self, ticker: str) -> CompanyData:
        normalized = ticker.strip().upper()

        if normalized in {"005930", "KRX:005930", "SAMSUNG", "SAMSUNGELECTRONICS"}:
            return CompanyData(
                ticker="005930.KS",
                as_of_date=date.today(),
                business_summary="메모리/파운드리/모바일/가전 포트폴리오를 보유한 한국 대표 IT 기업",
                peers=["TSM", "MU", "SK하이닉스", "AAPL"],
                reports=[],
                financials=FinancialSnapshot(
                    revenue=258.0,
                    operating_income=15.0,
                    free_cash_flow=12.0,
                    total_debt=95.0,
                ),
            )

        return CompanyData(
            ticker=normalized,
            as_of_date=date.today(),
            business_summary="데이터 소스 연동 전: 사업 요약 미수집 상태",
            peers=[],
            reports=[],
            financials=FinancialSnapshot(),
        )

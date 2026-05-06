from __future__ import annotations

from app.schemas import CompanyData, FinancialAnalysis


class FinancialAgent:
    """Step 2: 기본 재무평가.

    초보자용 규칙 기반 점수화(0~100).
    """

    def run(self, data: CompanyData) -> FinancialAnalysis:
        score = 50
        strengths, weaknesses, red_flags = [], [], []

        f = data.financials
        if f.revenue and f.revenue > 200:
            score += 10
            strengths.append("매출 규모가 크고 방어력이 있음")
        else:
            weaknesses.append("매출 규모/가시성 확인 필요")

        if f.free_cash_flow and f.free_cash_flow > 0:
            score += 10
            strengths.append("현금창출력이 플러스")
        else:
            red_flags.append("FCF 데이터 부재 또는 음수 가능성")

        if f.total_debt and f.total_debt > 120:
            score -= 8
            red_flags.append("부채 부담 점검 필요")
        else:
            strengths.append("과도한 부채 신호는 제한적")

        score = max(0, min(100, score))
        return FinancialAnalysis(score, strengths, weaknesses, red_flags)

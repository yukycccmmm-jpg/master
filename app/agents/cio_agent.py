from __future__ import annotations

from dataclasses import dataclass

from app.agents.debate_agent import DebateResult
from app.agents.financial_agent import FinancialAnalysis
from app.schemas import CommitteeDecision


@dataclass
class CIOResult:
    decision: CommitteeDecision
    rationale: list[str]


class CIOAgent:
    def run(self, fin: FinancialAnalysis, debate: DebateResult) -> CIOResult:
        base = 90000.0
        if fin.score_financial >= 65:
            base *= 1.05
        elif fin.score_financial < 45:
            base *= 0.92

        bear = round(base * 0.85, 0)
        bull = round(base * 1.15, 0)
        rating = "HOLD" if fin.score_financial < 70 else "BUY"
        decision = CommitteeDecision(rating, bear, round(base, 0), bull, 0.68)
        rationale = [debate.summary, "단일 숫자보다 시나리오 목표주가를 우선"]
        return CIOResult(decision, rationale)

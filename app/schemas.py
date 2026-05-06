from __future__ import annotations

from dataclasses import asdict, dataclass, field
from datetime import date
from typing import List, Literal, Optional


@dataclass
class FinancialSnapshot:
    revenue: Optional[float] = None
    operating_income: Optional[float] = None
    free_cash_flow: Optional[float] = None
    total_debt: Optional[float] = None


@dataclass
class CompanyData:
    ticker: str
    as_of_date: date
    business_summary: str
    peers: List[str] = field(default_factory=list)
    reports: List[str] = field(default_factory=list)
    financials: FinancialSnapshot = field(default_factory=FinancialSnapshot)

    def to_dict(self) -> dict:
        data = asdict(self)
        data["as_of_date"] = self.as_of_date.isoformat()
        return data


@dataclass
class FinancialAnalysis:
    score_financial: int
    strengths: List[str]
    weaknesses: List[str]
    red_flags: List[str]


@dataclass
class CommitteeDecision:
    rating: Literal["BUY", "HOLD", "SELL"]
    bear_target: float
    base_target: float
    bull_target: float
    confidence: float

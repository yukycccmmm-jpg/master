from __future__ import annotations

from dataclasses import dataclass
from typing import List

from app.agents.financial_agent import FinancialAnalysis
from app.agents.report_agent import ReportAnalysis
from app.schemas import CompanyData


@dataclass
class DebateResult:
    buffett_view: str
    graham_view: str
    fisher_view: str
    dalio_view: str
    summary: str
    risks: List[str]


class DebateAgent:
    def run(self, data: CompanyData, fin: FinancialAnalysis, rep: ReportAnalysis) -> DebateResult:
        buffett = "반도체/파운드리 생태계와 브랜드는 강점이나, 가격이 안전마진을 주는지는 별도 점검 필요"
        graham = "PBR/PER이 업황 저점 대비 얼마나 선반영됐는지 확인 전에는 보수적 접근"
        fisher = "AI 메모리(HBM)와 고부가 제품 믹스 개선은 중장기 성장 포인트"
        dalio = "금리·달러·글로벌 경기 사이클과 반도체 재고순환이 핵심 변수"

        summary = f"재무점수 {fin.score_financial}/100 기준: 장기경쟁력 긍정, 단기 업황/밸류 민감."
        risks = [*fin.red_flags, *rep.bias_check]
        return DebateResult(buffett, graham, fisher, dalio, summary, risks)

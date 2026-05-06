from __future__ import annotations

from dataclasses import dataclass
from typing import List

from app.schemas import CompanyData


@dataclass
class ReportAnalysis:
    consensus_points: List[str]
    disagreements: List[str]
    bias_check: List[str]


class ReportAgent:
    def run(self, data: CompanyData) -> ReportAnalysis:
        if not data.reports:
            return ReportAnalysis(
                consensus_points=["리포트 원문 미수집으로 공통의견 제한"],
                disagreements=["목표 멀티플/메모리 업황 가정 차이 확인 필요"],
                bias_check=["데이터 공백으로 과도한 낙관/비관 판정 보류"],
            )
        return ReportAnalysis(
            consensus_points=["메모리 업황 회복 기대 반영"],
            disagreements=["HBM 점유율 및 ASP 전망치 차이"],
            bias_check=["업황 회복 속도 가정이 낙관적일 수 있음"],
        )

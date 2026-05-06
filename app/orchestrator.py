from __future__ import annotations

from dataclasses import asdict, dataclass
from typing import Any, Dict

from app.agents.cio_agent import CIOAgent
from app.agents.data_agent import DataAgent
from app.agents.debate_agent import DebateAgent
from app.agents.financial_agent import FinancialAgent
from app.agents.report_agent import ReportAgent


@dataclass
class Orchestrator:
    data_agent: DataAgent
    financial_agent: FinancialAgent
    report_agent: ReportAgent
    debate_agent: DebateAgent
    cio_agent: CIOAgent

    def run_step(self, step: int, ticker: str) -> Dict[str, Any]:
        data = self.data_agent.run(ticker)
        if step == 1:
            return {"step": 1, "name": "DataAgent", "result": data.to_dict()}
        if step == 2:
            return {"step": 2, "name": "FinancialAgent", "result": asdict(self.financial_agent.run(data))}
        if step == 3:
            return {"step": 3, "name": "ReportAgent", "result": asdict(self.report_agent.run(data))}
        if step == 4:
            fin = self.financial_agent.run(data)
            rep = self.report_agent.run(data)
            return {"step": 4, "name": "DebateAgent", "result": asdict(self.debate_agent.run(data, fin, rep))}
        if step == 5:
            fin = self.financial_agent.run(data)
            rep = self.report_agent.run(data)
            debate = self.debate_agent.run(data, fin, rep)
            cio = self.cio_agent.run(fin, debate)
            return {
                "step": 5,
                "name": "CIOAgent",
                "company": data.to_dict(),
                "financial": asdict(fin),
                "report": asdict(rep),
                "debate": asdict(debate),
                "final": {"decision": asdict(cio.decision), "rationale": cio.rationale},
            }
        return {"error": "step must be 1..5"}

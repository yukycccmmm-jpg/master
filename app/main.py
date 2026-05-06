from __future__ import annotations

import argparse
import json

from app.agents.cio_agent import CIOAgent
from app.agents.data_agent import DataAgent
from app.agents.debate_agent import DebateAgent
from app.agents.financial_agent import FinancialAgent
from app.agents.report_agent import ReportAgent
from app.orchestrator import Orchestrator


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Investment Agent Step Runner")
    parser.add_argument("--step", type=int, required=True, help="실행할 단계 번호(1~5)")
    parser.add_argument("--ticker", type=str, required=True, help="종목 티커")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    orchestrator = Orchestrator(DataAgent(), FinancialAgent(), ReportAgent(), DebateAgent(), CIOAgent())
    output = orchestrator.run_step(step=args.step, ticker=args.ticker)
    print(json.dumps(output, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()

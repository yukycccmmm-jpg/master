"""OpenAI client wrapper and response parsing for scenario generation."""

from __future__ import annotations

import json
import os
from dataclasses import dataclass
from typing import Any

from openai import OpenAI

from src.prompts import SYSTEM_PROMPT, build_user_prompt


@dataclass
class ScenarioRequest:
    ticker: str
    thesis: str
    model: str = "gpt-4.1-mini"


class ScenarioGenerator:
    """Generates investment scenarios using the OpenAI Responses API."""

    def __init__(self, api_key: str | None = None) -> None:
        self.api_key = api_key or os.getenv("OPENAI_API_KEY")
        if not self.api_key:
            raise ValueError("OPENAI_API_KEY가 설정되어 있지 않습니다.")
        self.client = OpenAI(api_key=self.api_key)

    def generate(self, req: ScenarioRequest) -> dict[str, Any]:
        user_prompt = build_user_prompt(ticker=req.ticker, thesis=req.thesis)

        response = self.client.responses.create(
            model=req.model,
            input=[
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": user_prompt},
            ],
            text={"format": {"type": "json_object"}},
        )

        raw = response.output_text
        return json.loads(raw)

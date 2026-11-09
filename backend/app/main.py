from pathlib import Path
from typing import Literal

from fastapi import FastAPI
from pydantic import BaseModel

from backend.app.costs import read_cost_records, summarize_costs


SAMPLE_COSTS_PATH = Path(__file__).resolve().parents[2] / "data" / "sample_costs.csv"


class ServiceCost(BaseModel):
    service: str
    cost_usd: str


class CostSummary(BaseModel):
    currency: Literal["USD"]
    source: Literal["synthetic_sample"]
    total_cost_usd: str
    services: list[ServiceCost]


app = FastAPI(title="Cloud Cost Guardian API", version="0.1.0")


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}


@app.get("/api/v1/costs/summary", response_model=CostSummary)
def get_cost_summary() -> dict[str, object]:
    records = read_cost_records(SAMPLE_COSTS_PATH)
    return summarize_costs(records)

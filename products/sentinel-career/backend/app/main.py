from typing import List, Optional

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, ConfigDict, Field

from products.sentinel_career.backend.app.api.career_health import calculate_career_health

app = FastAPI(title="Sentinel Career API")


class ATSResultData(BaseModel):
    model_config = ConfigDict(extra="forbid")

    ats_score: Optional[float] = None
    interview_probability: Optional[float] = None
    keywords_found: List[str] = Field(default_factory=list)
    keywords_missing: List[str] = Field(default_factory=list)
    summary: str = ""
    market_readiness: Optional[float] = None


class ATSResultRequest(BaseModel):
    model_config = ConfigDict(extra="forbid")

    data: ATSResultData


@app.get("/health")
async def health_check() -> dict[str, str]:
    return {"status": "ok"}


@app.post("/api/v1/career-health/calculate")
async def calculate_career_health_endpoint(payload: ATSResultRequest):
    try:
        result = calculate_career_health(payload.model_dump())
    except ValueError as exc:
        raise HTTPException(status_code=422, detail=str(exc)) from exc
    except Exception as exc:  # pragma: no cover
        raise HTTPException(status_code=500, detail="Erro interno do servidor") from exc

    if result is None:
        raise HTTPException(status_code=500, detail="Resposta vazia do serviço de cálculo")

    if result.get("status") == "ERROR":
        recommendations = result.get("recommendations")
        detail = (
            recommendations[0]
            if isinstance(recommendations, list) and recommendations
            else "Erro ao calcular o Career Health"
        )
        raise HTTPException(status_code=422, detail=detail)

    return result

from fastapi import APIRouter
from pydantic import BaseModel

from backend.modules.nikto.module import run_nikto_api

router = APIRouter()


class NiktoRequest(BaseModel):
    target: str


@router.post("/nikto")
def run_nikto_scan(payload: NiktoRequest):

    return run_nikto_api(
        payload.target
    )

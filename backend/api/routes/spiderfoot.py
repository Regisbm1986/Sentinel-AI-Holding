from fastapi import APIRouter
from pydantic import BaseModel
import subprocess
import os

router = APIRouter()


class SpiderFootRequest(BaseModel):
    target: str


@router.get("/spiderfoot")
def spiderfoot_status():

    return {
        "module": "spiderfoot",
        "status": "ready"
    }


@router.post("/spiderfoot")
def run_spiderfoot_scan(payload: SpiderFootRequest):

    sf_script = os.path.expanduser("~/spiderfoot/sf.py")

    if not os.path.exists(sf_script):
        return {
            "status": "error",
            "error": "SpiderFoot não encontrado"
        }

    cmd = [
        "/home/sentineladmin/sentinel-os/venv/bin/python",
        sf_script,
        "-t", "ALL",
        "-u", "all",
        "-q",
        "-s", payload.target
    ]

    try:

        result = subprocess.run(
            cmd,
            capture_output=True,
            text=True
        )

        return {
            "status": "success",
            "target": payload.target,
            "command": cmd,
            "output": result.stdout[:5000],
            "stderr": result.stderr[:2000]
        }

    except Exception as e:

        return {
            "status": "error",
            "error": str(e)
        }

from fastapi import APIRouter
from agents.log_analysis import analyze_log

router = APIRouter()

@router.post("/analyze_log")
def analyze():
    return analyze_log()

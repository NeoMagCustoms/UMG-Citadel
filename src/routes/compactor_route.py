/src/routes/compactor_route.py
`````python
from fastapi import APIRouter
from agents.memory_compactor import compact_memory

router = APIRouter()

@router.post("/compact_memory")
def trigger_compaction():
    return compact_memory()

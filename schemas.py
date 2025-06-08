from pydantic import BaseModel
from typing import Optional

class STask_add(BaseModel):
    name: str
    description: Optional[str] = None

class STask_get(STask_add):
    id: int

class STask_id(BaseModel):
    ok: bool=True
    task_id:int
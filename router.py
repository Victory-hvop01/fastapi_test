from typing import Annotated

from fastapi import APIRouter, Depends

from repository import TaskRepository
from schemas import STask_add, STask_id

router=APIRouter(prefix="/tasks")

@router.post("")
async def add_task(task:Annotated[STask_add, Depends()]) -> STask_id:
    task_id=await TaskRepository.add_one(task)
    return {"ok":True,"task_id":task_id}

@router.get("")
async def get_tasks() -> STask_add:
    tasks=await TaskRepository.get_all()
    return {"tasks":tasks}
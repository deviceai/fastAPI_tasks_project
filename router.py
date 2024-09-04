from typing import Annotated
from fastapi import APIRouter, Depends
from schemas import STaskAdd, STask, STaskId
from repository import TasksRepository

router = APIRouter(
    prefix="/tasks",
    tags=["My tasks"]
)


@router.post("")
async def add_task(
        task: Annotated[STaskAdd, Depends()]
) -> STaskId:
    task_id = await TasksRepository.add_one(task)
    return {"ok": True, "task_id": task_id}


@router.get("")
async def get_tasks() -> list[STask]:
    tasks = await TasksRepository.find_all()
    return tasks

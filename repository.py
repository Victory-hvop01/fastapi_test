from database import new_ses, TasksOrm
from schemas import STask_get, STask_add
from sqlalchemy import select

class TaskRepository:
    @classmethod
    async def add_one(cls, data:STask_add):
        async with new_ses() as session:
            task_dict=data.model_dump()
            task=TasksOrm(**task_dict)
            session.add(task)
            await session.flush()
            await session.commit()
            return task.id

    @classmethod
    async def get_all(cls) ->list[STask_get]:
        async with new_ses() as session:
            query=select(TasksOrm)
            result=await session.execute(query)
            task_models=result.scalars().all()
            task_schemas=[STask_get.model_validate(task) for task in task_models]
            return task_models


from fastapi import FastAPI
import uvicorn
from contextlib import asynccontextmanager
from database import create_table
from router import router as tasks_router

@asynccontextmanager
async def lifespan(app:FastAPI):
    await create_table()
    print("База очищена")
    await create_table()
    print("База готова")
    yield
    print("Выключение")
app = FastAPI(lifespan=lifespan)
app.include_router(tasks_router)

if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)


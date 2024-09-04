from database import create_tables, delete_tables
from fastapi import FastAPI
from contextlib import asynccontextmanager
from router import router as task_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    await delete_tables()
    print("Database is empty!")
    await create_tables()
    print("Database is ready!")
    yield

app = FastAPI(lifespan=lifespan)
app.include_router(task_router)





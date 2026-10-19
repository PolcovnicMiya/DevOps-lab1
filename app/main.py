import logging
import os
from contextlib import asynccontextmanager

from fastapi import FastAPI
from pydantic import BaseModel


class StudentInfo(BaseModel):
    name: str
    surname: str
    group: str
    student_id: str


def student_info() -> StudentInfo:
    return StudentInfo(
        name=os.getenv("STUDENT_NAME", "Alexandr"),
        surname=os.getenv("STUDENT_SURNAME", "Sgibnev"),
        group=os.getenv("STUDENT_GROUP", "IT2-2314"),
        student_id=os.getenv("STUDENT_ID", "37882"),
    )


@asynccontextmanager
async def lifespan(application: FastAPI):
    info = student_info()
    logging.getLogger("uvicorn.error").info(
        "Student: %s %s | Group: %s | Student ID: %s",
        info.name, info.surname, info.group, info.student_id,
    )
    yield


app = FastAPI(
    title="Alexandr Sgibnev DevOps Application",
    lifespan=lifespan,
    docs_url=None,
    redoc_url=None,
    openapi_url=None,
)


@app.get("/")
def root():
    return {
        "message": "Application is running successfully!",
        "course": "DevOps",
        "student": student_info().model_dump(),
    }

from fastapi import FastAPI
from .schemas import *
from .routers import authentication, classroom_student, classroom, course, exam, exam_result, grade, parent, users, student
from . import models
from .database import engine
import json
from fastapi.middleware.cors import CORSMiddleware

# models.Base.metadata.create_all(bind=engine)                # This creates tables in database from models

app = FastAPI()


app.include_router(classroom_student.router)
app.include_router(classroom.router)
app.include_router(course.router)
app.include_router(exam_result.router)
app.include_router(grade.router)
app.include_router(parent.router)
app.include_router(exam.router)
app.include_router(users.router)
app.include_router(student.router)
app.include_router(authentication.router)

@app.get("/")
def root():
    return {"message": "test connection1234"}

#CORS code below

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

#PAGINATION CODE 


with open('app/news.json') as f:
    data = json.load(f)

data_length = len(data)

@app.get("/json")
def read_json(page_num:int = 1, page_size: int = 10):
    start = (page_num - 1) * page_size
    end = start + page_size
    response = { 
        "data": data[start:end],
        "total": data_length,
        "count": page_size,
        "pagination": {}
    }
    
    if end >= data_length:
        response["pagination"]["next"] = None

        if page_num > 1:
            response["pagination"]["previous"] = f"/posts?page_num={page_num-1}&page_size={page_size}"
        else:
            response["pagination"]["previous"] = None
    else:
        if page_num > 1:
            response["pagination"]["previous"] = f"/posts?page_num={page_num-1}&page_size={page_size}"
        else:
            response["pagination"]["previous"] = None

        response["pagination"]["next"] = f"/posts?page_num={page_num+1}&page_size={page_size}"

        return response
from sqlite3 import Date
from pydantic import BaseModel, EmailStr
from datetime import date, time,datetime
from typing import Optional

#Users
class User(BaseModel):
    username: str
    user_type: str
    password: str
    email: EmailStr
    mobile: int

class User_response(BaseModel):

    username: str
    user_type: str
    email: str
    mobile: int
    created_at: datetime

    class Config:
        orm_mode = True

#Student

class Student(BaseModel):

    first_name: str
    last_name: str
    dob: date


#Exam
class Exam(BaseModel):
    name: str
    start_date: date

#Grade
class Grade(BaseModel):
    description: str
    name: str

#Course
class Course(BaseModel):
    description: str
    name: str

#Exam_result
class Exam_result(BaseModel):
    marks: int


#Exam Result Model
class Exam_result(BaseModel):
    exam_res_id: int
    marks: int
    course_id: int
    exam_id: int
    date: str
    student_id: int
    teacher_id: int

# Classroom  model
class classroom(BaseModel):
    remarks: str
    section: str
    status: bool
    date: str

#Classroom Student
class classroom_student(BaseModel):
    classroom_stu_id: int
    classroom_id: int
    student_id: int


#parent
class parent(BaseModel):
    first_name: str
    last_name: str

#User-login for jwt

class UserLogin(BaseModel):
    email: EmailStr
    password: str


#Token

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    id: Optional[str] = None
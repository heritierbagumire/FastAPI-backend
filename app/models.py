from sqlalchemy import Column, ForeignKey, Integer, String ,Boolean, DateTime
from sqlalchemy.sql.expression import null, text
from .database import Base
from sqlalchemy.sql.sqltypes import TIMESTAMP


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, nullable = False, autoincrement=True)
    username = Column(String, nullable = False, unique=True)
    user_type = Column(String, nullable = False)
    password = Column(String, nullable = False)
    email = Column(String, nullable = False, unique=True)
    mobile = Column(Integer, nullable = False, unique=True)
    created_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default = text('now()'))

class Students(Base):
    __tablename__ = "students"

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    dob = Column(DateTime, nullable=False)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    users_id = Column(Integer, ForeignKey("users.id", ondelete='CASCADE'), nullable = False)

class Teacher(Base):
    __tablename__ = "teachers"

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    dob = Column(DateTime, nullable=False)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    users_id = Column(Integer, ForeignKey("users.id", ondelete='CASCADE'), nullable = False)

class Parents(Base):
    __tablename__ = "parents"

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    dob = Column(DateTime, nullable=False)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    users_id = Column(Integer, ForeignKey("users.id", ondelete='CASCADE'), nullable = False)
    student_id = Column(Integer, ForeignKey("students.id", ondelete='CASCADE'), nullable = False)

class Address(Base):
    __tablename__ = "address"

    id = Column(Integer, primary_key=True, nullable=False, autoincrement = True)
    address_line1 = Column(String, nullable=False)
    address_line2 = Column(String, nullable=False)
    City = Column(String, nullable=False)
    State = Column(String, nullable=False)
    Country = Column(String, nullable=False)
    pincode = Column(Integer, nullable=False)
    users_id = Column(Integer, ForeignKey("users.id", ondelete='CASCADE'), nullable = False)

class Attendance(Base):
    __tablename__ = "attendance"

    id = Column(Integer, primary_key=True, nullable = False, autoincrement = True)
    total = Column(Integer, nullable = False)
    remarks = Column(String, nullable = False)
    Status = Column(String, nullable = False)
    students_id = Column(Integer, ForeignKey("students.id", ondelete='CASCADE'), nullable = False)

class Classroom(Base):
    __tablename__ = "classroom"

    id = Column(Integer, primary_key = True, nullable = False, autoincrement = True)
    section = Column(String, nullable = False)
    students_id = Column(Integer, ForeignKey("students.id", ondelete='CASCADE'), nullable = False)

class Course(Base):
    __tablename__ = "course"

    id = Column(Integer, primary_key = True, nullable = False, autoincrement = True)
    name = Column(String, nullable = False)
    description = Column(String, nullable = False)
    students_id = Column(Integer, ForeignKey("students.id", ondelete='CASCADE'), nullable = False)

class Exam(Base):
    __tablename__ = "exam"

    id = Column(Integer, primary_key = True, nullable = False, autoincrement = True)
    name = Column(String, nullable = False)
    Subject = Column(String, nullable = False)

class Exam_result(Base):
    __tablename__ = "exam_result"

    id = Column(Integer, primary_key = True, nullable = False, autoincrement = True)
    marks = Column(Integer, nullable = False)
    students_id = Column(Integer, ForeignKey("students.id", ondelete='CASCADE'), nullable = False)
    teacher_id = Column(Integer, ForeignKey("teachers.id", ondelete='CASCADE'), nullable = False)

class Grade(Base):
    __tablename__ = "grade"

    id = Column(Integer, primary_key = True , nullable = False , autoincrement = True)
    g_class = Column(String, nullable = False)
    students_id = Column(Integer, ForeignKey("students.id", ondelete='CASCADE'), nullable = False)
    exam_result = Column(Integer, ForeignKey("exam_result.id", ondelete='CASCADE'), nullable = False)
from fastapi import APIRouter
from config.db import conn
from config.db import session
from sqlalchemy import select
from schemas.course import Course
from models.course import courses
from typing import List
from sqlalchemy import func, select

course = APIRouter()

@course.get(
    "/courses/get_all_courses",
    tags=["courses"],
    response_model=List[Course],
    description="Get a list of all courses",
)
def get_all_courses():
    return conn.execute(courses.select()).fetchall()

@course.get(
    "/courses/get_course_detail/{Course_ID}", 
    tags=["courses"], 
    response_model=List[Course],
    description="Get details of a course",
)
def get_course_detail(Course_ID:str):
    return conn.execute(courses.select().where(courses.c.Course_ID == Course_ID)).fetchall()

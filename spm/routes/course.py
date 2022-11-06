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
    "/courses/get_course_by_id/{Course_ID}", 
    tags=["courses"], 
    response_model=List[Course],
    description="Get details of a course by id",
)
def get_course_by_id(Course_ID:str):
    return conn.execute(courses.select().where(courses.c.Course_ID == Course_ID)).fetchall()

@course.get(
    "/courses/get_course_by_name/{search_course_name}", 
    tags=["courses"], 
    description="Get details of a course by name",
)
def get_course_by_name(search_course_name:str):
    search_course_name = search_course_name.lower()
    statement = courses.select().where(func.lower(courses.c.Course_Name).contains(search_course_name))
    return conn.execute(statement).fetchall()


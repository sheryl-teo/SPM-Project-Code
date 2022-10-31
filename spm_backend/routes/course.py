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
    # return conn.execute(text('SELECT course_name FROM course')).fetchall()
    return conn.execute(courses.select()).fetchall()


# @course.get("/courses/course_count", tags=["courses"], response_model=CourseCount)
# def course_count():
#     result = conn.execute(select([func.count()]).select_from(courses))
#     return {"total": tuple(result)[0][0]}


@course.get(
    "/courses/get_course_detail/{Course_ID}", 
    tags=["courses"], 
    response_model=List[Course],
    description="Get details of a course",
)
def get_course_detail(Course_ID:str):
    return conn.execute(courses.select().where(courses.c.Course_ID == Course_ID)).fetchall()


####not a core functionality####
# @course.put(
#     "/courses/retire_course/{Course_ID}", 
#     tags=["courses"], 
#     response_model=List[Course],
#     description="Soft delete a specified course",
# )
# def retire_course(Course_ID:str):
#     conn.execute(courses.update().where(courses.c.Course_ID == Course_ID).values(Course_Status = "Retired"))
#     return conn.execute(courses.select().where(courses.c.Course_ID == Course_ID)).fetchall()

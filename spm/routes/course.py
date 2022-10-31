from fastapi import APIRouter
from config.db import conn
from config.db import session
from sqlalchemy import select
from schemas.course import Course, CourseCount
from models.course import courses
from typing import List
from sqlalchemy import func, select

course = APIRouter()

@course.get(
    "/courses",
    tags=["courses"],
    response_model=List[Course],
    description="Get a list of all users",
)
def get_users():
    return conn.execute(courses.select()).fetchall()



@course.get("/courses/count", tags=["courses"], response_model=CourseCount)
def get_users_count():
    result = conn.execute(select([func.count()]).select_from(courses))
    return {"total": tuple(result)[0][0]}


# Change to Course ID to prevent errors due to spaces.
@course.get(
    "/courses/{Course_Name}", 
    tags=["courses"], 
    response_model=List[Course],
    description="Get a specified course",
)
def get_a_course(Course_Name:str):
    """Returns courses with the course name.

    Args:
        Course_Name (str): Course name

    Returns:
        _type_: _description_
        Supposed to be a list of either tuples or objects. 
    """
    statement = select(Course).filter_by(Couse_Name=Course_Name)
    return session.execute(statement).all()
    # return conn.execute(courses.select().where(courses.c.Course_Name == Course_Name)).fetchall()

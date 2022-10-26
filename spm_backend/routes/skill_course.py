# from fastapi import APIRouter
# from config.db import conn
# from schemas.skill_course import Skill_course
# from models.skill_course import skill_courses
# from typing import List
# from sqlalchemy import func, select

# skill_course = APIRouter()

# @skill_course.get(
#     "/skill_courses/{Course_ID}",
#     tags=["skill_courses"],
#     response_model=List[Skill_course],
#     description="Get a list of all skills in course",
# )
# def get_skill_course(Course_ID: str):
#     return conn.execute(skill_courses.select().where(skill_courses.c.Course_ID == {Course_ID})).fetchall()

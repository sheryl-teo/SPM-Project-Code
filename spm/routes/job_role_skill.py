from fastapi import APIRouter
from config.db import conn
from schemas.job_role_skill import Job_role_skill
from models.job_role_skill import job_role_skills
from typing import List
from sqlalchemy import func, select

job_role_skill = APIRouter()

# Get all skill course relationships
@job_role_skill.get(
    "/job_role_skills",
    tags=["skills"],
    response_model=List[Job_role_skill],
    description="Get a list of all skill course relationships.",
)
def get_all_skill_course():
    return conn.execute(job_role_skills.select()).fetchall()

# Create
@skill_course.post(
    "/skill_course/create",
    tags=["skills"],
    response_model=List[Skill_course],
    description="Create a new skill course relationship.",
)
async def create_skill(skill_course: dict):
    """Create a new skill course relationship.
    Course_Id: str
    Skill_Id: str
    soft_delete: bool
    Args:
        skill_course (dict): JSON dictionary, containing Course_Id, Skill_Id, soft_delete

    Returns:
        _type_: _description_
    """
    skill_course['Skill_ID'] = skill_course['Skill_ID'].capitalize()
    skill_course['Course_ID'] = skill_course['Course_ID'].capitalize()
    skill_course['soft_delete'] = False

    # Error handling: 
    search_skill_ID = skill_course['Skill_ID']
    search_course_ID = skill_course['Course_ID']

    # errors = [error_2(search_skill_ID), error_3(search_skill_ID)]
    # errors_list = [e for e in errors if e != None]
    # if len(errors_list) == 0:
    #     statement = skills.insert([skill])
    #     return conn.execute(statement)
    # else:
    #     return {'errors': errors_list}

    statement = skill_courses.insert([skill_course])
    conn.execute(statement)

# Read 

# Get all skills in a course
@skill_course.get(
    "/skill_courses/skills_in_course/{Course_ID}",
    tags=["skill_courses"],
    response_model=List[Skill_course],
    description="Get a list of all skills in course",
)
def get_skill_course(Course_ID: str):
    Course_ID = Course_ID.capitalize()
    return conn.execute(skill_courses.select().where(skill_courses.c.Course_ID == {Course_ID} & skill_courses.c.soft_delete == False)).fetchall()

# Get courses for each skill
@skill_course.get(
    "/skill_courses/courses_in_skill/{Skill_ID}",
    tags=["skill_courses"],
    response_model=List[Skill_course],
    description="Get a list of all skills in course",
)
def get_skill_course(Skill_ID: str):
    Skill_ID = Skill_ID.capitalize()
    return conn.execute(skill_courses.select().where(skill_courses.c.Skill_ID == {Skill_ID} & skill_courses.c.soft_delete == False)).fetchall()

# Soft delete course skill relationship
@skill_course.post(
    "/skill_course/create",
    tags=["skills"],
    response_model=List[Skill_course],
    description="Create a new skill course relationship.",
)
async def update_soft_delete(skill_course: dict):
    """Create a new skill course relationship.
    Course_Id: str
    Skill_Id: str
    soft_delete: bool
    Args:
        skill_course (dict): JSON dictionary, containing Course_Id, Skill_Id

    Returns:
        _type_: _description_
    """
    skill_course['Skill_ID'] = skill_course['Skill_ID'].capitalize()
    skill_course['Course_ID'] = skill_course['Course_ID'].capitalize()

    # Error handling: 
    search_skill_ID = skill_course['Skill_ID']
    search_course_ID = skill_course['Course_ID']

    # errors = [error_2(search_skill_ID), error_3(search_skill_ID)]
    # errors_list = [e for e in errors if e != None]
    # if len(errors_list) == 0:
    #     statement = skills.insert([skill])
    #     return conn.execute(statement)
    # else:
    #     return {'errors': errors_list}

    statement = skill_courses.update().where(skill_courses.c.Skill_ID==skill_course['Skill_ID'] & skill_courses.c.Course_ID==skill_course['Course_ID']).values(soft_delete=skill_course['soft_delete'])
    conn.execute(statement)

    
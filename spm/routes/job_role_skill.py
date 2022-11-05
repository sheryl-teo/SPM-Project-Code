from fastapi import APIRouter
from config.db import conn
from schemas.job_role_skill import Job_role_skill
from models.job_role_skill import job_role_skills
from models.skill import skills
from models.job_role import job_roles
from typing import List
from sqlalchemy import func, select

from routes.job_role import error1 as jobrole_error1
from routes.job_role import error3 as jobrole_error3

from routes.skill import error1 as skill_error1
from routes.skill import error3 as skill_error3
jobrole_skill = APIRouter()

# Get all skill course relationships
@jobrole_skill.get(
    "/jobrole_skills",
    tags=["skills"],
    response_model=List[Job_role_skill],
    description="Get a list of all skill course relationships.",
)
def get_all_jobrole_skill():
    return conn.execute(job_role_skills.select()).fetchall()

# Create
@jobrole_skill.post(
    "/jobrole_skills/create",
    tags=["skills"],
    description="Create a new job role skill relationship.",
)
async def create_jobrole_skill(jobrole_skill: Job_role_skill):
    jobrole_skill['Job_Role_ID'] = jobrole_skill['Job_Role_ID'].upper()
    jobrole_skill['Skill_ID'] = jobrole_skill['Skill_ID'].upper()
    jobrole_skill['Active'] = False

    # Error handling: 
    search_jobrole_ID = jobrole_skill['Job_Role_ID']
    search_skill_ID = jobrole_skill['Skill_ID']

    errors = [jobrole_error1(search_jobrole_ID), jobrole_error3(search_jobrole_ID), skill_error1(search_skill_ID), skill_error3(search_skill_ID)]
    errors_list = [e for e in errors if e != None]
    if len(errors_list) == 0:
        statement = job_role_skills.insert([jobrole_skill])
        return conn.execute(statement)
    else:
        return {'errors': errors_list}

# Read 

@jobrole_skill.get(
    "/jobrole_skills/read/jobrole/{search_jobrole}",
    tags=["skill_courses"],
    description="Get a list of all skills for a role",
)
def get_skill_course(search_jobrole: str):
    search_jobrole = search_jobrole.upper()
    errors = [jobrole_error1(search_jobrole), jobrole_error3(search_jobrole)]
    errors_list = [e for e in errors if e != None]
    if len(errors_list) == 0:
        return conn.execute(job_role_skills.select().where(job_role_skills.c.Job_Role_ID == search_jobrole & job_role_skills.c.Active == True)).fetchall()
    else:
        return {'errors': errors_list}


@jobrole_skill.get(
    "/jobrole_skills/read/skill/{search_skill}",
    tags=["skill_courses"],
    description="Get a list of all roles with a skill",
)
def get_skill_course(search_skill: str):
    search_skill = search_skill.upper()
    errors = [skill_error1(search_skill), skill_error3(search_skill)]
    errors_list = [e for e in errors if e != None]
    if len(errors_list) == 0:
        return conn.execute(job_role_skills.select().where(job_role_skills.c.Job_Role_ID == search_skill & job_role_skills.c.Active == True)).fetchall()
    else:
        return {'errors': errors_list}

# Soft delete course skill relationship
@jobrole_skill.post(
    "/jobrole_skills/delete/soft",
    tags=["skills"],
    description="Soft delete skill course relationship.",
)
async def update_soft_delete(jobrole_skill: Job_role_skill):
    jobrole_skill['Job_Role_ID'] = jobrole_skill['Job_Role_ID'].upper()
    jobrole_skill['Skill_ID'] = jobrole_skill['Skill_ID'].upper()
    jobrole_skill['Active'] = 0

    # Error handling: 
    search_jobrole_ID = jobrole_skill['Job_Role_ID']
    search_skill_ID = jobrole_skill['Skill_ID']

    errors = [jobrole_error1(search_jobrole_ID), jobrole_error3(search_jobrole_ID), skill_error1(search_skill_ID), skill_error3(search_skill_ID)]
    errors_list = [e for e in errors if e != None]
    if len(errors_list) == 0:
        statement = job_role_skills.update().where(job_role_skills.c.Skill_ID==jobrole_skill['Skill_ID'] & job_role_skills.c.Job_Role_ID==jobrole_skill['Job_Role_ID']).values(Active=jobrole_skill['Active'])
        conn.execute(statement)
    else:
        return {'errors': errors_list}

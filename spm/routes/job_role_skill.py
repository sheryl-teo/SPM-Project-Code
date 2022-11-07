from fastapi import APIRouter
from config.db import conn
from schemas.job_role_skill import Job_role_skill
from models.job_role_skill import job_role_skills
from schemas.skill import Skill
from models.skill import skills
from schemas.job_role import Job_role
from models.job_role import job_roles
from typing import List
from sqlalchemy import func, select

from routes.job_role import error_1 as jobrole_error1
from routes.job_role import error_3 as jobrole_error3

from routes.skill import error_1 as skill_error1
from routes.skill import error_3 as skill_error3

job_role_skill = APIRouter()

# Get all job role skill relationships
@job_role_skill.get(
    "/job_role_skills",
    tags=["job_role_skill"],
    description="Get a list of all job role skill relationships.",
)
def get_all_job_role_skill():
    return conn.execute(job_role_skills.select()).fetchall()

# Create
@job_role_skill.post(
    "/job_role_skills/create",
    tags=["job_role_skill"],
    description="Create a new job role skill relationship.",
)
async def create_job_role_skill(job_role_skill: Job_role_skill):
    # Error handling: 
    search_jobrole_ID = job_role_skill.Job_Role_ID.upper()
    search_skill_ID = job_role_skill.Skill_ID.upper()

    errors = [jobrole_error1(search_jobrole_ID), jobrole_error3(search_jobrole_ID), skill_error1(search_skill_ID), skill_error3(search_skill_ID)]
    errors_list = [e for e in errors if e != None]
    if len(errors_list) == 0:
        # Create job role skill
        statement = job_role_skills.insert([job_role_skill])
        conn.execute(statement)
        # Return created job role skill
        return conn.execute(job_role_skills.select().where(
            (job_role_skills.c.Job_Role_ID == search_jobrole_ID) & 
            (job_role_skills.c.Skill_ID == search_skill_ID))
            ).fetchall()
    else:
        return {'errors': errors_list}

# Read 
@job_role_skill.get(
    "/job_role_skills/read/jobrole/{search_jobrole}",
    tags=["job_role_skill"],
    description="Get a list of all active skills for a role",
)
def get_skill_jobrole(search_jobrole: str):
    # Error handling
    search_jobrole = search_jobrole.upper()
    errors = [jobrole_error1(search_jobrole), jobrole_error3(search_jobrole)]
    errors_list = [e for e in errors if e != None]
    if len(errors_list) == 0:
        return conn.execute(job_role_skills.select().where(
            (job_role_skills.c.Job_Role_ID == search_jobrole) & (job_role_skills.c.Active == 1))).fetchall()
    else:
        return {'errors': errors_list}


@job_role_skill.get(
    "/job_role_skills/read/skill/{search_skill}",
    tags=["job_role_skill"],
    description="Get a list of all roles with a skill",
)
def get_job_role_skill(search_skill: str):
    # Error handling
    search_skill = search_skill.capitalize()
    errors = [skill_error1(search_skill), skill_error3(search_skill)]
    errors_list = [e for e in errors if e != None]
    if len(errors_list) == 0:
        # Return a list of all roles with a skill
        return conn.execute(job_role_skills.select().where(
            (job_role_skills.c.Skill_ID == search_skill) & 
            (job_role_skills.c.Active == 1))).fetchall()
    else:
        return {'errors': errors_list}

# Soft delete 
@job_role_skill.post(
    "/job_role_skills/delete/soft",
    tags=["job_role_skill"],
    description="Soft delete job role skill relationship.",
)
def update_soft_delete(job_role_skill: Job_role_skill):

    # Error handling: 
    search_jobrole_ID = job_role_skill.Job_Role_ID.capitalize()
    search_skill_ID = job_role_skill.Skill_ID.capitalize()
    job_role_skill.Active = 0

    errors = [
        jobrole_error1(search_jobrole_ID), 
        jobrole_error3(search_jobrole_ID), 
        skill_error1(search_skill_ID), 
        skill_error3(search_skill_ID)
        ]
    errors_list = [e for e in errors if e != None]
    if len(errors_list) == 0:
        statement = job_role_skills.update().where(
            (job_role_skills.c.Skill_ID==job_role_skill.Skill_ID) & 
            (job_role_skills.c.Job_Role_ID==job_role_skill.Job_Role_ID)
            ).values(Active=job_role_skill.Active)
        conn.execute(statement)
    else:
        return {'errors': errors_list}

# Soft undelete 
@job_role_skill.post(
    "/job_role_skills/delete/softrestore",
    tags=["job_role_skill"],
    description="Soft undelete job role skill relationship.",
)
def delete_jobrole_softrestore(job_role_skill: Job_role_skill):
    

    # Error handling: 
    search_jobrole_ID = job_role_skill.Job_Role_ID.capitalize()
    search_skill_ID = job_role_skill.Skill_ID.capitalize()
    job_role_skill.Active = 1

    errors = [
        jobrole_error1(search_jobrole_ID), 
        jobrole_error3(search_jobrole_ID), 
        skill_error1(search_skill_ID), 
        skill_error3(search_skill_ID)]
    errors_list = [e for e in errors if e != None]
    if len(errors_list) == 0:
        statement = job_role_skills.update().where(
            (job_role_skills.c.Skill_ID==job_role_skill.Skill_ID) & 
            (job_role_skills.c.Job_Role_ID==job_role_skill.Job_Role_ID)
            ).values(Active=job_role_skill.Active)
        conn.execute(statement)
    else:
        return {'errors': errors_list}

# # Hard delete
# @job_role_skill.post(
#     "/job_role_skills/delete/hard",
#     tags=["skills"],
#     description="Hard delete job role skill relationship.",
# )
# async def update_hard_delete(job_role_skill: dict):
#     job_role_skill['Job_Role_ID'] = job_role_skill['Job_Role_ID'].upper()
#     job_role_skill['Skill_ID'] = job_role_skill['Skill_ID'].upper()

#     # Error handling: 
#     search_jobrole_ID = job_role_skill['Job_Role_ID']
#     search_skill_ID = job_role_skill['Skill_ID']

#     errors = [jobrole_error1(search_jobrole_ID), jobrole_error3(search_jobrole_ID), skill_error1(search_skill_ID), skill_error3(search_skill_ID)]
#     errors_list = [e for e in errors if e != None]
#     if len(errors_list) == 0:
#         statement = job_role_skills.delete().where(job_role_skills.c.Skill_ID==job_role_skill['Skill_ID'] & job_role_skills.c.Job_Role_ID==job_role_skill['Job_Role_ID'])
#         conn.execute(statement)
#     else:
#         return {'errors': errors_list}
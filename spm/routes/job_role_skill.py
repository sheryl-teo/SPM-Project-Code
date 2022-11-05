from fastapi import APIRouter
from config.db import conn
from schemas.job_role_skill import Job_role_skill
from models.job_role_skill import job_role_skills
from typing import List
from sqlalchemy import func, select
from schemas.index import Job_role_skill

job_role_skill = APIRouter()

# @job_role_skill.post(
#     "/job_role_skill/create_job_role_skill",
#     tags=["job_role_skills"],
#     response_model=List[Job_role_skill],
#     description="Assign skills to a job role",
# )
# def create_job_role_skill(job_skill: Job_role_skill):
#     conn.execute(job_role_skills.insert().values(
#         Job_Role_ID = job_skill.Job_Role_ID,
#         Skill_ID = job_skill.Skill_ID,
#         Active = job_skill.Active
#     ))
#     return conn.execute(job_role_skills.select().where(job_role_skill.c.Job_Role_ID == job_skill.Job_Role_ID and job_role_skill.c.Skill_ID == job_skill.Skill_ID)).fetchall()

@job_role_skill.get(
    "/job_role_skill/get_job_role_skill/{Job_Role_ID}",
    tags=["job_role_skills"],
    response_model=List[Job_role_skill],
    description="Get a list of all skills of a job role",
)
def get_job_role_skill(Job_Role_ID: str):
    return conn.execute(job_role_skills.select().where(job_role_skills.c.Job_Role_ID == Job_Role_ID)).fetchall()


@job_role_skill.put(
    "/job_roles_skill/delete_job_role_skill/{Job_Role_ID}",
    tags=["job_role_skills"],
    response_model=List[Job_role_skill],
    description="Delete a specified job role",
)
def delete_job_role_skill(Job_Role_ID: str):
    conn.execute(job_role_skills.delete().where(job_role_skills.c.Job_Role_ID == Job_Role_ID)) 
    return conn.execute(job_role_skills.select()).fetchall()



# errors = [error_2(search_skill_ID), error_3(search_skill_ID)]
# errors_list = [e for e in errors if e != None]
# if len(errors_list) == 0:
#     statement = skills.insert([skill])
#     return conn.execute(statement)
# else:
#     return {'errors': errors_list}


    
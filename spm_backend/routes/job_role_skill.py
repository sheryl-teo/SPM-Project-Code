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
#     description="Get a list of all skills of a job role",
# )
# def create_job_role_skill(job_skill: Job_role_skill):
#           conn.execute(job_role_skills.insert().values(
#                job_role_id = job_skill.job_role_id
#                skill_id = job_skill.skill_id
# ))
#     return conn.execute(job_role_skills.select()).fetchall()

# @job_role_skill.get(
#     "/job_role_skill/get_job_role_skill/{Job_Role_ID}",
#     tags=["job_role_skills"],
#     response_model=List[Job_role_skill],
#     description="Get a list of all skills of a job role",
# )
# def get_job_role_skill(Job_Role_ID: str):
#     return conn.execute(job_role_skills.select().where(job_role_skills.c.Job_Role_ID == Job_Role_ID)).fetchall()


# @job_role_skill.put(
#     "/job_roles_skill/delete_job_role_skill/{Job_Role_ID}",
#     tags=["job_role_skills"],
#     response_model=List[Job_role_skill],
#     description="Delete a specified job role",
# )
# def delete_job_role_skill(Job_Role_ID: str):
#     conn.execute(job_role_skills.delete().where(job_role_skills.c.Job_Role_ID == Job_Role_ID)) 
#     return conn.execute(job_role_skills.select()).fetchall()
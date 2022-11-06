from fastapi import APIRouter
from config.db import conn
from schemas.job_role import Job_role
from models.job_role import job_roles
from schemas.job_role_skill import Job_role_skill
from models.job_role_skill import job_role_skills
from schemas.learning_journey import Learning_journey
from models.learning_journey import learning_journeys
from typing import List
from sqlalchemy import func, select, join

job_role = APIRouter()


@job_role.post(
    "/job_role/create",
    tags=["job_roles"],
    description="Create a job role",
)
def create(job: Job_role):
    #create new job role
    #when new job role is created, skills pertaining to this job role should also be added into job_role_skill table
    conn.execute(job_roles.insert().values(
        Job_Role_ID = job.Job_Role_ID,
        Job_Role_Name = job.Job_Role_Name,
        Job_Department = job.Job_Department,
        Active = job.Active
    ))
    #return created job role
    return conn.execute(job_roles.select().where(job_roles.c.Job_Role_ID == job.Job_Role_ID)).fetchall()

@job_role.get(
    
    "/job_roles/get_job_roles",
    tags=["job_roles"],
    description="Get a list of all job roles details",
)
def get_job_roles():
    #return all job roles in db
    return conn.execute(job_roles.select()).fetchall()

@job_role.get(
    "/job_roles/get_job_role_by_department/{Job_Department}",
    tags=["job_roles"],
    description="Get a list of job roles by department",
)
def get_job_role_by_department(Job_Department: str):
    #return all job roles in a department
    #departments are Chairman, CEO, Ops, Finance, Sales, HR
    return conn.execute(job_roles.select().where(job_roles.c.Job_Department == Job_Department)).fetchall()


@job_role.put(
    "/job_roles/update/{Job_Role_ID}",
    tags=["job_roles"],
    description="Update a specified job role",
)
def update(job: Job_role):
    conn.execute(job_roles.update().values(
        Job_Role_Name = job.Job_Role_Name,
        Job_Department = job.Job_Department
    ).where(job_roles.c.Job_Role_ID == job.Job_Role_ID))
    return conn.execute(job_roles.select().where(job_roles.c.Job_Role_ID == job.Job_Role_ID)).fetchall()

@job_role.put(
    "/job_roles/delete/{Job_Role_ID}",
    tags=["job_roles"],
    description="Soft delete a specified job role",
)
def delete(Job_Role_ID: str):
    #soft delete a job role row by changing the active value
    # active = 0(retired)
    conn.execute(job_roles.update().values(
        Active = 0
    ).where(job_roles.c.Job_Role_ID == Job_Role_ID))
    #soft delete a job role skill row by changing the active value
    #when a job role is retired, the job role skills are retired as well
    conn.execute(job_role_skills.update().values(
        Active = 0
    ).where(job_role_skills.c.Job_Role_ID == Job_Role_ID))
    #return deleted job role
    return conn.execute(job_roles.select().where(job_roles.c.Job_Role_ID == Job_Role_ID)).fetchall()

@job_role.put(
    "/job_roles/undelete/{Job_Role_ID}",
    tags=["job_roles"],
    description="Soft undelete a specified job role",
)
def undelete(Job_Role_ID: str):
    #soft undelete a job role row by changing the active value
    # active = 1(active)
    conn.execute(job_roles.update().values(
        Active = 1
    ).where(job_roles.c.Job_Role_ID == Job_Role_ID))
    #soft undelete a job role skill row by changing the active value
    #when a job role is active, the job role skills are active as well
    conn.execute(job_role_skills.update().values(
        Active = 1
    ).where(job_role_skills.c.Job_Role_ID == Job_Role_ID))
    #return undeleted job role
    return conn.execute(job_roles.select().where(job_roles.c.Job_Role_ID == Job_Role_ID)).fetchall()
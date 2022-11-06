from fastapi import APIRouter
from config.db import conn
from schemas.job_role import Job_role
from models.job_role import job_roles
from schemas.learning_journey import Learning_journey
from models.learning_journey import learning_journeys
from typing import List
from sqlalchemy import func, select

job_role = APIRouter()


@job_role.post(
    "/job_role/create_job_role",
    tags=["job_roles"],
    response_model=List[Job_role],
    description="Create a job role",
)
def create_job_role(job: Job_role):
    conn.execute(job_roles.insert().values(
        Job_Role_ID = job.Job_Role_ID,
        Job_Role_Name = job.Job_Role_Name,
        Job_Department = job.Job_Department,
        Active = job.Active
))
    return conn.execute(job_roles.select().where(job_roles.c.Job_Role_ID == job.Job_Role_ID)).fetchall()

@job_role.get(
    
    "/job_roles/get_job_roles",
    tags=["job_roles"],
    response_model=List[Job_role],
    description="Get a list of all job roles details",
)
def get_job_roles():
    return conn.execute(job_roles.select()).fetchall()

@job_role.get(
    "/job_roles/get_job_role_by_department/{Job_Department}",
    tags=["job_roles"],
    response_model=List[Job_role],
    description="Get a list of job roles by department",
)
def get_job_role_by_department(Job_Department: str):
    return conn.execute(job_roles.select().where(job_roles.c.Job_Department == Job_Department)).fetchall()


@job_role.put(
    "/job_roles/update_job_role/{Job_Role_ID}",
    tags=["job_roles"],
    response_model=List[Job_role],
    description="Update/soft delete a specified job role",
)
def update_job_role(job: Job_role):
    conn.execute(job_roles.update().values(
        Job_Role_Name = job.Job_Role_Name,
        Job_Department = job.Job_Department,
        Active = job.Active
    ).where(job_roles.c.Job_Role_ID == job.Job_Role_ID))
    return conn.execute(job_roles.select().where(job_roles.c.Job_Role_ID == job.Job_Role_ID)).fetchall()


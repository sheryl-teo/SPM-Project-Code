from fastapi import APIRouter
from config.db import conn
from schemas.job_role import Job_role
from models.job_role import job_roles
from typing import List
from sqlalchemy import func, select

job_role = APIRouter()

@job_role.get(
    "/job_roles",
    tags=["job_roles"],
    response_model=List[Job_role],
    description="Get a list of all job roles details",
)
def get_job_roles():
    return conn.execute(job_roles.select()).fetchall()

@job_role.get(
    "/job_roles/{Job_Department}",
    tags=["job_roles"],
    response_model=List[Job_role],
    description="Get a list of job roles by department",
)
def get_job_role_by_department(Job_Department: str):
    return conn.execute(job_roles.select().where(job_roles.c.Job_Department == Job_Department)).fetchall()

@job_role.put(
    "/job_roles/{Job_Role_ID}",
    tags=["job_roles"],
    response_model=List[Job_role],
    description="Soft delete a specified job role",
)
def soft_delete_job_role(Job_Role_ID: str):
    conn.execute(job_roles.update().where(job_roles.c.Job_Role_ID == Job_Role_ID).values(Job_Role_Status = "Retired"))
    return conn.execute(job_roles.select().where(job_roles.c.Job_Role_ID == Job_Role_ID)).fetchall()
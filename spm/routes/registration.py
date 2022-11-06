from fastapi import APIRouter
from config.db import conn
from schemas.registration import Registration
from models.registration import registrations
from schemas.staff import Staff
from models.staff import staffs
from typing import List
from sqlalchemy import func, select, join

registration = APIRouter()

@registration.get(
    "/registration/get_registration_list",
    tags=["registrations"],
    response_model=List[Registration],
    description="Get a list of all registrations",
)
def get_registration_list():
    return conn.execute(registrations.select()).fetchall()


# @registration.get(
#     "/registration/get_staff_completed_courses/{Staff_ID}",
#     tags=["registrations"],
#     response_model=List[Registration],
#     description="Get a list of all completed courses of a staff",
# )
# def get_staff_completed_skills(Staff_ID: int):
#     return conn.execute(registrations.select().where(registrations.c.Staff_ID == Staff_ID)).fetchall()


# @registration.get(
#     "/registration/get_staff_completed_skills/{Staff_ID}",
#     tags=["registrations"],
#     response_model=List[Registration],
#     description="Get a list of all job roles details",
# )
# def get_staff_completed_skills(Staff_ID: int):
#     return conn.execute(registrations.select().where(registrations.c.Staff_ID == Staff_ID)).fetchall()

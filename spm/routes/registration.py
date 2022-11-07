from fastapi import APIRouter
from config.db import conn
from schemas.registration import Registration
from models.registration import registrations
from schemas.skill_course import Skill_course
from models.skill_course import skill_courses
from schemas.staff import Staff
from models.staff import staffs
from typing import List
from sqlalchemy import func, select, join
from sqlalchemy.sql import text
from .staff import error_1 

registration = APIRouter()

def error_2(Staff_ID: int):
    """Check whether staff exists
    """
    statement = staffs.select().where(staffs.c.Staff_ID == Staff_ID)
    staff_check = conn.execute(statement).fetchall()
    if staff_check == []:
        error_msg = {
            'Error_ID': 'R1', 
            'Error_Desc': '''This staff could not be found within the database. Check your staff ID and try again.''',
            'Error_Details': ''
        }
    else: 
        error_msg = None
    return error_msg 


@registration.get(
    "/registration/get_registration_list",
    tags=["registrations"],
    response_model=List[Registration],
    description="Get a list of all registrations",
)
def get_registration_list():
    return conn.execute(registrations.select()).fetchall()


@registration.get(
    "/registration/get_staff_completed_courses/{Staff_ID}",
    tags=["registrations"],
    description="Get a list of all completed courses of a staff",
)
def get_staff_completed_courses(Staff_ID: int):
    errors = [error_1(Staff_ID), error_2(Staff_ID)]
    errors_list = [e for e in errors if e != None]
    if len(errors_list) == 0:
        return conn.execute(registrations.select().where((registrations.c.Staff_ID == Staff_ID) & (registrations.c.Completion_Status == "Completed"))).fetchall()   
    else:
        return {'errors': errors_list}

    

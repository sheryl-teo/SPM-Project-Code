from fastapi import APIRouter
from config.db import conn
from schemas.staff import Staff
from models.staff import staffs
from typing import List
from sqlalchemy import func, select

# staff = APIRouter()

# @staff.get(
#     "/staffs/get_all_staff",
#     tags=["staffs"],
#     response_model=List[Staff],
#     description="Get a list of all staff",
# )
# def get_all_staff():
#     return conn.execute(staffs.select()).fetchall()


# @staff.get(
#     "/staffs/get_staff_details/{Staff_ID}",
#     tags=["staffs"],
#     response_model=List[Staff],
#     description="Get details of a staff",
# )
# def get_staff_details(Staff_ID: int):
#     return conn.execute(staffs.select().where(staffs.c.Staff_ID == Staff_ID)).fetchall()

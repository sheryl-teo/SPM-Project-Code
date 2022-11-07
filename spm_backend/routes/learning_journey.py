from fastapi import APIRouter
from config.db import conn
from schemas.learning_journey import Learning_journey
from models.learning_journey import learning_journeys
from schemas.staff import Staff
from models.staff import staffs
from schemas.job_role import Job_role
from models.job_role import job_roles
from typing import List
from sqlalchemy import func, select, join

learning_journey = APIRouter()

@learning_journey.post(
    "/learning_journey/create_learning_journey",
    tags=["learning_journeys"],
    response_model=List[Learning_journey],
    description="Create a learning journey",
)
def create_learning_journey(ljourney: Learning_journey):
    conn.execute(learning_journeys.insert().values(
        Learning_Journey_ID = ljourney.Learning_Journey_ID,
        Job_Role_ID = ljourney.Job_Role_ID,
        Staff_ID = ljourney.Staff_ID
    ))
    return conn.execute(learning_journeys.select().where(learning_journeys.c.Learning_Journey_ID == ljourney.Learning_Journey_ID)).fetchall()

@learning_journey.get(
    "/learning_journey/get_learning_journey",
    tags=["learning_journeys"],
    response_model=List[Learning_journey],
    description="Get a list of all learning journeys",
)
def get_learning_journey():
    return conn.execute(learning_journeys.select()).fetchall()
   
@learning_journey.get(
    "/learning_journey/get_staff_learning_journey",
    tags=["learning_journeys"],
    response_model=List[Learning_journey],
    description="Get a list of all learning journeys",
)
def get_staff_learning_journey(s: Learning_journey):
    return conn.execute(learning_journeys.select().where(learning_journeys.c.Staff_ID == Learning_journey.Staff_ID)).fetchall()
   

@learning_journey.put(
    "/learning_journey/update_learning_journey/{Learning_Journey_ID}",
    tags=["learning_journeys"],
    response_model=List[Learning_journey],
    description="Update the job role of a learning journey",
)
def update_learning_journey(ljourney: Learning_journey):
    conn.execute(learning_journeys.update().values(
        Job_Role_ID = ljourney.Job_Role_ID
    ).where(learning_journeys.c.Learning_Journey_ID == ljourney.Learning_Journey_ID))
    return conn.execute(learning_journeys.select().where(learning_journeys.c.Learning_Journey_ID == ljourney.Learning_Journey_ID)).fetchall()

@learning_journey.put(
    "/learning_journey/delete_learning_journey/{Learning_Journey_ID}",
    tags=["learning_journeys"],
    response_model=List[Learning_journey],
    description="Delete a learning journey",
)
def delete_learning_journey(Learning_Journey_ID: str):
    conn.execute(learning_journeys.delete().where(learning_journeys.c.Learning_Journey_ID == Learning_Journey_ID))
    return conn.execute(learning_journeys.select()).fetchall()


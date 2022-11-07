from fastapi import APIRouter
from config.db import conn
from schemas.learning_journey import Learning_journey
from models.learning_journey import learning_journeys
from schemas.learning_journey_course import Learning_journey_course
from models.learning_journey_course import learning_journey_courses
from schemas.learning_journey_skill import Learning_journey_skill
from models.learning_journey_skill import learning_journey_skills
from schemas.job_role import Job_role
from models.job_role import job_roles
from typing import List
from sqlalchemy import func, select, join
import requests

learning_journey = APIRouter()

@learning_journey.post(
    "/learning_journey/create_learning_journey",
    tags=["learning_journeys"],
    description="Create a learning journey",
)
def create_learning_journey(ljourney: Learning_journey):
    #create learning journey
    conn.execute(learning_journeys.insert().values(
        Learning_Journey_ID = ljourney.Learning_Journey_ID,
        Job_Role_ID = ljourney.Job_Role_ID,
        Staff_ID = ljourney.Staff_ID
    ))
    #created learning journey
    return conn.execute(learning_journeys.select().where(learning_journeys.c.Learning_Journey_ID == ljourney.Learning_Journey_ID)).fetchall()




@learning_journey.get(
    "/learning_journey/get_learning_journey",
    tags=["learning_journeys"],
    description="Get a list of all learning journeys",
)
def get_learning_journey():
    #get all learning journeys in db
    return conn.execute(learning_journeys.select()).fetchall()
   


# User story: see all learning journey that a staff has
@learning_journey.get(
    "/learning_journey/get_staff_learning_journey/{Staff_ID}",
    tags=["learning_journeys"],
    description="Get a list of all staff learning journeys",
)
def get_staff_learning_journey(Staff_ID: int):
    #get all learning journeys of a staff
    return conn.execute(learning_journeys.select().where(learning_journeys.c.Staff_ID == Staff_ID)).fetchall()
   
# User story: see a learning journey that a staff has
@learning_journey.post(
    "/learning_journey/get_a_staff_learning_journey",
    tags=["learning_journeys"],
    description="Get a learning journey details of a staff",
)
def get_a_staff_learning_journey(slj: dict):
    # input format:
    # {
    #     "Staff_ID": 130001,
    #     "Learning_Journey_ID": "LJ1"
    # }
    staff_id = slj['Staff_ID']
    learning_journey_id = slj['Learning_Journey_ID']
    # Get job role id
    response = conn.execute(learning_journeys.select().where(
        (learning_journeys.c.Staff_ID == staff_id) & 
        (learning_journeys.c.Learning_Journey_ID == learning_journey_id))).fetchall()
    job_role_id = response[0]['Job_Role_ID']
    # get job role name
    response2 = conn.execute(job_roles.select().where(job_roles.c.Job_Role_ID == job_role_id)).fetchall()
    job_role_name = response2[0]['Job_Role_Name']
    return job_role_name, job_role_id
    # get skill id
    # get skill name
   

@learning_journey.put(
    "/learning_journey/update_learning_journey",
    tags=["learning_journeys"],
    description="Update the job role of a learning journey",
)
def update_learning_journey(ljourney: Learning_journey):
    #update learning journey
    conn.execute(learning_journeys.update().values(
        Learning_Journey_ID = ljourney.Learning_Journey_ID,
        Job_Role_ID = ljourney.Job_Role_ID,
        Staff_ID = ljourney.Staff_ID
    ).where(learning_journeys.c.Learning_Journey_ID == ljourney.Learning_Journey_ID))
    #return updated learning journey
    return conn.execute(learning_journeys.select().where(learning_journeys.c.Learning_Journey_ID == ljourney.Learning_Journey_ID)).fetchall()



@learning_journey.put(
    "/learning_journey/delete/{Learning_Journey_ID}",
    tags=["learning_journeys"],
    description="Delete a learning journey",
)
def delete(Learning_Journey_ID: str):
    #delete learning journey
    conn.execute(learning_journeys.delete().where(learning_journeys.c.Learning_Journey_ID == Learning_Journey_ID))
    #delete learning journey skills
    conn.execute(learning_journey_skills.delete().where(learning_journey_skills.c.Learning_journey_ID == Learning_Journey_ID))
    #delete learning journey courses
    conn.execute(learning_journey_courses.delete().where(learning_journey_courses.c.Learning_journey_ID == Learning_Journey_ID))
    #return all learning_journeys
    return conn.execute(learning_journeys.select()).fetchall()


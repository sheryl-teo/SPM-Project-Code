from fastapi import APIRouter
from config.db import conn
from schemas.learning_journey import Learning_journey
from models.learning_journey import learning_journeys
from schemas.learning_journey_course import Learning_journey_course
from models.learning_journey_course import learning_journey_courses
from schemas.learning_journey_skill import Learning_journey_skill
from models.learning_journey_skill import learning_journey_skills
from schemas.job_role_skill import Job_role_skill
from models.job_role_skill import job_role_skills
from schemas.job_role import Job_role
from models.job_role import job_roles
from schemas.skill import Skill
from models.skill import skills

from schemas.course import Course
from models.course import courses
from typing import List
from sqlalchemy import func, select, join
import requests


from routes.job_role import error_1 as jobrole_error1
from routes.job_role import error_3 as jobrole_error3

from routes.skill import error_1 as skill_error1
from routes.skill import error_3 as skill_error3

learning_journey = APIRouter()


# Create a learning journey
@learning_journey.post(
    "/learning_journey/create_learning_journey",
    tags=["learning_journeys"],
    description="Create a learning journey",
)
def create_learning_journey(clj: dict):
    #create learning journey
    #inputs:
            # {
            #     "Learning_Journey_ID": "LJ100",
            #     "Staff_ID": 130001,
            #     "Job_Role_ID": "JR1",
            #     "skill_list": [
            #         "S1",
            #         "S2"
            #     ],
            #     "course_list": [
            #         "COR001",
            #         "COR002"
            #     ]
            # }
    learning_journey_id = clj['Learning_Journey_ID']
    staff_id = clj['Staff_ID']
    job_role_id = clj['Job_Role_ID']
    skill_list = clj['skill_list']
    course_list = clj['course_list']
    # create row in learning journey table
    conn.execute(learning_journeys.insert().values(
        Learning_Journey_ID = learning_journey_id,
        Job_Role_ID = job_role_id,
        Staff_ID = staff_id
    ))
    #for each course in course_list
    for course_id in course_list:
        # create row in learning journey course table
        conn.execute(learning_journey_courses.insert().values(
            Learning_Journey_ID = learning_journey_id,
            Course_ID = course_id
            ))
    # for each skill in skill_list
    for skill_id in skill_list:
        # create row in learning journey skill table
        conn.execute(learning_journey_skills.insert().values(
            Learning_Journey_ID = learning_journey_id,
            Skill_ID = skill_id
            ))
    ### Return created record
    slj = {
        "Staff_ID": staff_id,
        "Learning_Journey_ID": learning_journey_id
    }
    response = get_a_staff_learning_journey(slj)
    return response


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
    # get skills id in the learning journey
    skill_id_list = []
    response3 = conn.execute(learning_journey_skills.select().where(
        learning_journey_skills.c.Learning_Journey_ID == learning_journey_id
    )).fetchall()
    for ljsrow in response3:
        skill_id_list.append(ljsrow['Skill_ID'])
    # get skills name in the learning journey
    skill_name_list = []
    for skill_id in skill_id_list:
        response4 = conn.execute(skills.select().where(
            skills.c.Skill_ID == skill_id
        )).fetchall()
        skill_name = response4[0]['Skill_Name']
        skill_name_list.append(skill_name)
    # Format the skills list
    skill_list = {}
    for index in range(len(skill_id_list)):
        skill_id = skill_id_list[index]
        skill_name = skill_name_list[index]
        skill_list[skill_id] = skill_name
    # get courses they have in the learning journey
    response5 = conn.execute(learning_journey_courses.select().where(
            learning_journey_courses.c.Learning_Journey_ID == learning_journey_id
    )).fetchall()
    # get course id
    course_id_list = []
    for ljcrow in response5:
        course_id_list.append(ljcrow['Course_ID'])
    # get course name
    course_name_list = []
    for course_id in course_id_list:
        response6 = conn.execute(courses.select().where(
            courses.c.Course_ID == course_id
        )).fetchall()
        course_name = response6[0]['Course_Name']
        course_name_list.append(course_name)
    # Format the course list
    course_list = {}
    for index in range(len(course_id_list)):
        course_id = course_id_list[index]
        course_name = course_name_list[index]
        course_list[course_id] = course_name
    #output format:
            # { 
            #     "Learning_Journey_ID": "LJ100",
            #     "Staff_ID": 130001,
            #     "Job_Role_ID": "JR1",
                # "Job_Role_Name": "Jobrolename"
            #     "skill_list": {
            #         "S1": "Skillname",
            #         "S2": "Skillname"
            #     },
            #     "course_list": {
            #         "COR001": "Coursename",
            #         "COR002": "Coursename"
            #     }
            # }
    output = {
                "Learning_Journey_ID": learning_journey_id,
                "Staff_ID": staff_id,
                "Job_Role_ID": job_role_id,
                "Job_Role_Name": job_role_name,
                "skill_list": skill_list,
                "course_list": course_list
            }
    return output
    
    

   

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


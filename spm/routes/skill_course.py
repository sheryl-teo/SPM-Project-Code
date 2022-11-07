from fastapi import APIRouter
from config.db import conn
from schemas.skill_course import Skill_course
from models.skill_course import skill_courses
from schemas.skill import Skill
from models.skill import skills
from schemas.course import Course
from models.course import courses
from typing import List
from sqlalchemy import func, select

from routes.skill import error_1 as skill_error1
from routes.skill import error_3 as skill_error3

from routes.course import error_1 as course_error1
from routes.course import error_2 as course_error2

skill_course = APIRouter()

# Get all skill course relationships
@skill_course.get(
    "/skill_courses",
    tags=["skill_courses"],
    description="Get a list of all skill course relationships.",
)
def get_all_skill_course():
    return conn.execute(skill_courses.select()).fetchall()

# Create
@skill_course.post(
    "/skill_courses/create",
    tags=["skill_courses"],
    description="Create a new skill course relationship.",
)
def create_skill_course(skill_course: Skill_course):
    skill_course.Skill_ID = skill_course.Skill_ID.upper()
    skill_course.Course_ID = skill_course.Course_ID.upper()

    # Error handling:
    search_course_ID = skill_course.Course_ID
    search_skill_ID = skill_course.Skill_ID

    errors = [skill_error1(search_skill_ID), skill_error3(search_skill_ID)]
    errors_list = [e for e in errors if e != None]
    if len(errors_list) == 0:
        # Create skill course
        conn.execute(skill_courses.insert().values(
            Course_ID = search_course_ID,
            Skill_ID = search_skill_ID,
            Active = 1
        ))
        # Return created skill course
        return conn.execute(skill_courses.select().where(
            (skill_courses.c.Skill_ID == search_skill_ID) & 
            (skill_courses.c.Course_ID == search_course_ID))
            ).fetchall()
    else:
        return {'errors': errors_list}

# Read
@skill_course.get(
    "/skill_courses/read/course/{search_course_ID}",
    tags=["skill_courses"],
    description="Get a list of all skills in course",
)
def get_course_skill(search_course_ID: str):
    # Error handling
    search_course_ID = search_course_ID.upper()
    errors = [
        course_error1(search_course_ID), 
        course_error2(search_course_ID)
        ]
    errors_list = [e for e in errors if e != None]
    if len(errors_list) == 0:
        # Return a list of all active skills in a active course
        return conn.execute(skill_courses.select().where(
            (skill_courses.c.Course_ID == search_course_ID) & 
            (skill_courses.c.Active == 1))).fetchall()
    else:   
        return {'errors': errors_list}

@skill_course.get(
    "/skill_courses/read/skill/{search_skill_ID}",
    tags=["skill_courses"],
    description="Get a list of all course in a skill",
)
def get_skill_course(search_skill_ID: str):
    # Error handling
    # search_skill_ID = search_skill_ID.upper()
    errors = [skill_error1(search_skill_ID), skill_error3(search_skill_ID)]
    errors_list = [e for e in errors if e != None]
    if len(errors_list) == 0:
        # Return a list of all active course in a active skill
        response = conn.execute(skill_courses.select().where(
            (skill_courses.c.Skill_ID == search_skill_ID) &
            (skill_courses.c.Active == 1))).fetchall()
        course_id_list = []
        for r in response:
            # get a list of course ids
            course_id_list.append(r['Course_ID'])
        course_name_list = []
        # for each course id,
        for c in course_id_list:
            # get the row from courses table
            courserow = conn.execute(courses.select().where(
                courses.c.Course_ID == c
            )).fetchall()
            # get the course name from row
            if courserow != []:
                course_name_list.append(courserow[0]['Course_Name'])
        #format the response
        # output = {
        #     "output" : [
        #                 {"Course_ID": "COR002", "Course_Name": "Coursename"},
        #                 {"Course_ID": "COR001", "Course_Name": "Coursename"},
        #                 {"Course_ID": "COR003", "Course_Name": "Coursename"},
        #                  ]
        # }

        output = {}
        courses_list = []
        for index in range(len(course_name_list)):
            course_dict = {}
            course_id = course_id_list[index]
            course_name = course_name_list[index]
            course_dict["Course_ID"] = course_id
            course_dict["Course_Name"] = course_name
            courses_list.append(course_dict)
        output["output"] = courses_list
        return output
        
        
    else:   
        return {'errors': errors_list}

# Soft delete
@skill_course.post(
    "/skill_courses/delete/",
    tags=["skill_courses"],
    description="Delete skill course relationship.",
)
def delete_skill_course(skill_course: Skill_course):
    

    # Error handling
    search_course_ID = skill_course.Course_ID.upper()
    search_skill_ID = skill_course.Skill_ID.upper()
    skill_course.Active = 0

    errors = [
        skill_error1(search_skill_ID), 
        skill_error3(search_skill_ID),
        course_error1(search_course_ID), 
        course_error2(search_course_ID)
        ]
    errors_list = [e for e in errors if e != None]
    if len(errors_list) == 0:
        statement = skill_courses.delete().where(
            (skill_courses.c.Skill_ID==skill_courses.Skill_ID) &
             (skill_courses.c.Job_Role_ID==skill_courses.Course_ID)
             )
        conn.execute(statement)
    else:   
        return {'errors': errors_list}

# # Soft undelete
# @skill_course.post(
#     "/skill_courses/delete/softrestore",
#     tags=["skill_courses"],
#     description="Soft undelete skill course relationship.",
# )
# def delete_skillcourse_softrestore(skill_course: Skill_course):

#     # Error handling
#     search_course_ID = skill_course.Course_ID.upper()
#     search_skill_ID = skill_course.Skill_ID.upper()
#     skill_course.Active = 1

#     errors = [
#         skill_error1(search_skill_ID), 
#         skill_error3(search_skill_ID),
#         course_error1(search_course_ID), 
#         course_error2(search_course_ID)
#         ]
#     errors_list = [e for e in errors if e != None]
#     if len(errors_list) == 0:
#         statement = skill_courses.update().where(
#             (skill_courses.c.Skill_ID==skill_courses.Skill_ID) &
#              (skill_courses.c.Job_Role_ID==skill_courses.Course_ID)
#              ).values(Active=skill_courses.Active)
#         conn.execute(statement)
#     else:   
#         return {'errors': errors_list}
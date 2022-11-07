from fastapi import APIRouter
from config.db import conn
from config.db import session
from sqlalchemy import select
from schemas.course import Course
from models.course import courses
from typing import List
from sqlalchemy import func, select

course = APIRouter()

#####################################
#error handling
#####################################
def error_1(search_Course_ID: str):
    search = courses.select().where(courses.c.Course_ID==search_Course_ID)
    result = conn.execute(search)
    result_dict = result.mappings().all()
    print('result_dict', result_dict)
    if result_dict == []: 
        error_msg = {
            'Error_ID': 'C1', 
            'Error_Desc': '''The course you're looking for is not inside our database. Check your search terms and try again.''',
            'Error_Details': ''
        }
    else: 
        error_msg = None
    
    return error_msg 

def can_convert_to_int(string: str):
    try:
        int(string)
        return True
    except ValueError:
        return False

def error_2(search_Course_ID: str):
    course_prefixes = ['COR', 'FIN', 'MGT', 'SAL', 'tch']
    letter_check = search_Course_ID[0:3].lower in [c.lower() for c in course_prefixes]
    int_check = can_convert_to_int(search_Course_ID[3:])
    if letter_check == False or int_check == False:
        error_msg = {
            'Error_ID': 'C2', 
            'Error_Desc': '''This course has an invalid course ID. Check your course ID and try again.''',
            'Error_Details': ''
        }
    else: 
        error_msg = None
    return error_msg 

def error_3(search_course_name: str):
    if len(search_course_name) <= 0:
        error_msg = {
            'Error_ID': 'C3', 
            'Error_Desc': '''This course does not have a course name. Check your course name and try again.''',
            'Error_Details': ''
        }
    else: 
        error_msg = None
    return error_msg 

#####################################
#error handling
#####################################

@course.get(
    "/courses/get_all_courses",
    tags=["courses"],
    response_model=List[Course],
    description="Get a list of all courses",
)
def get_all_courses():
    #get all courses
    return conn.execute(courses.select()).fetchall()

@course.get(
    "/courses/get_course_by_id/{Course_ID}", 
    tags=["courses"], 
    response_model=List[Course],
    description="Get details of a course by id",
)
def get_course_by_id(Course_ID:str):
    #get a single course by ID
    return conn.execute(courses.select().where(courses.c.Course_ID == Course_ID)).fetchall()

@course.get(
    "/courses/get_course_by_name/{search_course_name}", 
    tags=["courses"], 
    description="Get details of a course by name",
)
def get_course_by_name(search_course_name:str):
    search_course_name = search_course_name.lower()
    statement = courses.select().where(func.lower(courses.c.Course_Name).contains(search_course_name))
    #get a single course by name
    #name can be partially written or fully written
    return conn.execute(statement).fetchall()


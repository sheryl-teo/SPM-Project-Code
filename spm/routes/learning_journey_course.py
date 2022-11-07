from fastapi import APIRouter
from config.db import conn
from schemas.learning_journey_course import Learning_journey_course
from models.learning_journey_course import learning_journey_courses
from typing import List
from sqlalchemy import func, select, join

learning_journey_course = APIRouter()


@learning_journey_course.post(
    "/learning_journey_course/create",
    tags=["learning_journey_course"],
    description="Add a list of courses to a learning journey to be completed, returns a list of courses in a learning journey",
)
def create_learning_journey(ljcourse: Learning_journey_course):
    conn.execute(learning_journey_courses.insert().values(
        Learning_Journey_ID = ljcourse.Learning_Journey_ID,
        Course_ID = ljcourse.Course_ID
    ))
    #create new learning journey course
    #happens courses are added into a new/existing learning journey
    return conn.execute(learning_journey_courses.select().where(learning_journey_courses.c.Learning_Journey_ID == ljcourse.Learning_Journey_ID)).fetchall()



@learning_journey_course.get(
    "/learning_journey_course/get/{Learning_Journey_ID}",
    tags=["learning_journey_course"],
    description="Get a list of courses added to a learning journey",
)
def get(Learning_Journey_ID: str):
    #return all courses added to a learning journey
    return conn.execute(learning_journey_courses.select().where(learning_journey_courses.c.Learning_Journey_ID == Learning_Journey_ID)).fetchall()




@learning_journey_course.put(
    "/learning_journey_course/delete",
    tags=["learning_journeys"],
    description="Delete a learning_journey_skill row",
)
def delete(ljcourse: Learning_journey_course):
    #delete courses in a learning journey
    conn.execute(learning_journey_courses.delete().where((learning_journey_courses.c.Learning_Journey_ID == ljcourse.Learning_Journey_ID) & (learning_journey_courses.c.Skill_ID == ljcourse.Skill_ID)))
    #return all learning journey courses in db
    return conn.execute(learning_journey_courses.select()).fetchall()


#update function not needed, just delete row and create new row


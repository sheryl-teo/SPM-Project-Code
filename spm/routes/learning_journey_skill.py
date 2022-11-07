from fastapi import APIRouter
from config.db import conn
from schemas.learning_journey_skill import Learning_journey_skill
from models.learning_journey_skill import learning_journey_skills
from typing import List
from sqlalchemy import func, select, join

learning_journey_skill = APIRouter()


@learning_journey_skill.post(
    "/learning_journey_skill/create",
    tags=["learning_journey_skill"],
    description="Create a list of skills in learning journey to be completed based on the job role selected",
)
def create(ljskill: Learning_journey_skill):
    #create new learning journey skill
    #happens courses are added into a new/existing learning journey
    conn.execute(learning_journey_skills.insert().values(
        Learning_Journey_ID = ljskill.Learning_Journey_ID,
        Skill_ID = ljskill.Skill_ID
    ))
    return conn.execute(learning_journey_skills.select().where(learning_journey_skills.c.Learning_Journey_ID == ljskill.Learning_Journey_ID)).fetchall()



@learning_journey_skill.get(
    "/learning_journey_skill/get/{Learning_Journey_ID}",
    tags=["learning_journey_skill"],
    description="Get a list of skills in learning journey to be completed based on the job role selected",
)
def get(Learning_Journey_ID: str):
    return conn.execute(learning_journey_skills.select().where(learning_journey_skills.c.Learning_Journey_ID == Learning_Journey_ID)).fetchall()

# @learning_journey_skill.get(
#     "/learning_journey_skill/get_obtained_skills/{Learning_Journey_ID}",
#     tags=["learning_journey_skill"],
#     description="Get a list of obtained skills in learning journey",
# )
# def get_obtained_skills(Learning_Journey_ID: str):
#     return conn.execute(learning_journey_skills.select().where((learning_journey_skills.c.Learning_Journey_ID == Learning_Journey_ID) & (learning_journey_skills.c.Obtained == 1))).fetchall()

# @learning_journey_skill.get(
#     "/learning_journey_skill/get_unobtained_skills/{Learning_Journey_ID}",
#     tags=["learning_journey_skill"],
#     description="Get a list of unobtained skills in learning journey",
# )
# def get_unobtained_skills(Learning_Journey_ID: str):
#     return conn.execute(learning_journey_skills.select().where((learning_journey_skills.c.Learning_Journey_ID == Learning_Journey_ID) & (learning_journey_skills.c.Obtained == 0))).fetchall()

@learning_journey_skill.put(
    "/learning_journey_skill/delete",
    tags=["learning_journey_skill"],
    description="Delete a learning_journey_skill row",
)
def delete(ljskill: Learning_journey_skill):
    conn.execute(learning_journey_skills.delete().where((learning_journey_skills.c.Learning_Journey_ID == ljskill.Learning_Journey_ID) & (learning_journey_skills.c.Skill_ID == ljskill.Skill_ID)))
    return conn.execute(learning_journey_skills.select()).fetchall()

#update function not needed, just delete row and create new row


from fastapi import APIRouter
from config.db import conn
from schemas.learning_journey_skill import Learning_journey_skill
from models.learning_journey_skill import learning_journey_skills
# from schemas.staff import Staff
# from models.staff import staffs
# from schemas.job_role import Job_role
# from models.job_role import job_roles
from typing import List
from sqlalchemy import func, select, join

learning_journey_skill = APIRouter()


# @learning_journey_skill.post(
#     "/learning_journey_skill/create",
#     tags=["learning_journeys"],
#     description="Create a list of skills in learning journey to be completed based on the job role selected",
# )
# def create_learning_journey(ljskill: Learning_journey_skill):
#     conn.execute(learning_journey_skills.insert().values(
#         Learning_Journey_ID = ljskill.Learning_Journey_ID,
#         Skill_ID = ljskill.Skill_ID,
#         Obtained = ljskill.Obtained
#     ))
#     return conn.execute(learning_journey_skills.select().where(learning_journey_skills.c.Learning_Journey_ID == ljskill.Learning_Journey_ID)).fetchall()



# @learning_journey_skill.get(
#     "/learning_journey_skill/get_learning_journey_skills/{Learning_Journey_ID}",
#     tags=["learning_journeys"],
#     description="Get a list of skills in learning journey to be completed based on the job role selected",
# )
# def create_learning_journey(ljskill: Learning_journey_skill):
#     conn.execute(learning_journey_skills.insert().values(
#         Learning_Journey_ID = ljskill.Learning_Journey_ID,
#         Skill_ID = ljskill.Skill_ID,
#         Obtained = ljskill.Obtained
#     ))
#     return conn.execute(learning_journey_skills.select().where(learning_journey_skills.c.Learning_Journey_ID == ljskill.Learning_Journey_ID)).fetchall()

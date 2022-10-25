from fastapi import APIRouter
from config.db import conn
from schemas.skill import Skill
from models.skill import skills
from typing import List
from sqlalchemy import func, select

skill = APIRouter()

@skill.get(
    "/skills",
    tags=["skills"],
    response_model=List[Skill],
    description="Get a list of all skills",
)
def get_all_skill():
    return conn.execute(skills.select()).fetchall()


# @skill.put(
#     "/delete_skill_course/{Skill_ID}{Course_ID}",
#     tags=["delete_skill_course"],
#     response_model=List[Skill],
#     description="Soft delete a skill from a course",
# )
# def delete_skill_course(Skill_ID: str, soft_delete: bool):
#     conn.execute(skills.update(
#         soft_delete = skill.soft_delete
#     ).where(skills.c.Skill_ID == "S2")).values(soft_delete=1)


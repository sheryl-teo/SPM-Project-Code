from fastapi import APIRouter
from config.db import conn
from schemas.skill import Skill
from models.skill import skills
from typing import List
from sqlalchemy import func, select

skill = APIRouter()

@skill.get(
    "/skills/get_all_skill",
    tags=["skills"],
    response_model=List[Skill],
    description="Get a list of all skills",
)
def get_all_skill():
    return conn.execute(skills.select()).fetchall()


@skill.put(
    "/skills/delete_skill/{Skill_ID}",
    tags=["skills"],
    response_model=List[Skill],
    description="Delete a specified skill",
)
def delete_skill(Skill_ID: str):
    conn.execute(skills.delete().where(skills.c.Skill_ID == Skill_ID))
    return conn.execute(skills.select()).fetchall()
    #need to include sub functions: delete_skill_course(), delete_job_role_skill(), delete_learning_journey_skill()
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

# Read 
@skill.get(
    "/skills/read/id/{search_skill_ID}",
    tags=["skills"],
    response_model=List[Skill],
    description="Reads a skill through an exact match search by skill ID.",
)
def read_skill_id(search_skill_ID: str):
    """Reads a skill through an exact match search by skill ID.

    Args:
        search_skill_ID (str): Skill ID, following the format "SXX", 
        with XX representing the skill number.

    Returns:
        _type_: _description_
    """
    search_skill_ID = search_skill_ID.upper()
    statement = skills.select().where(skills.c.Skill_ID==search_skill_ID)
    return conn.execute(statement).all()

@skill.get(
    "/skills/read/name/{search_skill_name}",
    tags=["skills"],
    response_model=List[Skill],
    description="Reads a skill through a substring match search by skill name.",
)
def read_skill_name(search_skill_name: str):
    """Reads a skill through a substring match search by skill name.

    Args:
        search_skill_name (str): _description_

    Returns:
        _type_: _description_
    """
    search_skill_name = search_skill_name.lower()
    statement = skills.select().where(func.lower(skills.c.Skill_Name).contains(search_skill_name))
    return conn.execute(statement).all()

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


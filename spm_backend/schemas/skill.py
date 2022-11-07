from pydantic import BaseModel


class Skill(BaseModel):
    Skill_ID: str
    Skill_Name: str
    Active: int
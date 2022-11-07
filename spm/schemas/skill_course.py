from pydantic import BaseModel
class Skill_course(BaseModel):
    Course_ID: str
    Skill_ID: str
    Active: int
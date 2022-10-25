from pydantic import BaseModel
class Skill_course(BaseModel):
    Course_Id: str
    Skill_Id: str
    soft_delete: bool
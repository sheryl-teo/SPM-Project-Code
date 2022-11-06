from pydantic import BaseModel
class Job_role_skill(BaseModel):
    Job_Role_ID: str
    Skill_ID: str
    Active: int
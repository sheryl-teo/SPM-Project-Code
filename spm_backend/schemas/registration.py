from pydantic import BaseModel

class Registration(BaseModel):
    Reg_ID: int
    Course_ID: str
    Staff_ID: int
    Reg_Status: str
    Completion_Status: str
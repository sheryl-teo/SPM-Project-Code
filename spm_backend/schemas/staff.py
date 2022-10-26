from pydantic import BaseModel
class Staff(BaseModel):
    Staff_ID: int
    Staff_FName: str
    Staff_LName: str
    Dept: str
    Email: str
    Role: int
from pydantic import BaseModel
class Job_role(BaseModel):
    Job_Role_ID: str
    Job_Role_Name: str
    Job_Department: str
    Active: int
from pydantic import BaseModel


class Course(BaseModel):
    Course_Name: str
    Course_Desc: str
    Course_Status: str
    Course_Type: str
    Course_Category: str


class job_role(BaseModel):
    Job_Role_ID: str
    Job_Role_Name: str
    Job_Department: str


class job_role_skill(BaseModel):
    Job_Role_ID: str
    Skill_ID: str


class learning_journey(BaseModel):
    Learning_Journey_ID: str
    Staff_ID: int
    Job_Role_ID: str


class learning_journey_course(BaseModel):
    Learning_Journey_ID: str
    Course_ID: str


class learning_journey_skill(BaseModel):
    Learning_Journey_ID: str
    Skill_ID: str
    Obtained: bool


class registration(BaseModel):
    Reg_ID: int
    Course_ID: str
    Staff_ID: int
    Reg_Status: str
    Completion_Status: str


class role(BaseModel):
    Role_Id: int
    Role_Name: str


class skill(BaseModel):
    Skill_ID: int
    Skill_Name: int


class skill_course(BaseModel):
    Course_Id: str
    Skill_Id: str


class staff(BaseModel):
    Course_Id: str
    Skill_ID: str

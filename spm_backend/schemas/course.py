from pydantic import BaseModel


class Course(BaseModel):
    Course_ID: str
    Course_Name: str
    Course_Desc: str
    Course_Status: str
    Course_Type: str
    Course_Category: str


# class CourseCount(BaseModel):
#     total: int

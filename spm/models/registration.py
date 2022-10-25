from sqlalchemy import Column, Table , ForeignKeyConstraint, PrimaryKeyConstraint
from sqlalchemy.sql.sqltypes import Integer, String 
from config.db import meta

registrations = Table(
     "registration",
     meta,
    Column("Learning_Journey_ID", String(5), primary_key=True),
    Column("Course_ID", String(20)),
    Column("Staff_ID",Integer),
    Column("Reg_Status", String(20)) , 
    Column("Completion_Status",String(20)),
    ForeignKeyConstraint(
        ["Course_ID", "Staff_ID"], ["course.Course_ID", "staff.Staff_ID"]
    ) 
)

from sqlalchemy import Column, Table , ForeignKeyConstraint, PrimaryKeyConstraint
from sqlalchemy.sql.sqltypes import Integer, String 
from config.db import meta

registrations = Table(
     "registration",
     meta,
    Column("Reg_ID", String(5), primary_key=True),
    Column("Course_ID", String(20)),
    Column("Staff_ID",Integer),
    Column("Reg_Status", String(20)) , 
    Column("Completion_Status",String(20)),
    ForeignKeyConstraint(
        ["Course_ID"], ["course.Course_ID"], name = "fk_registration_course"
    ),
    ForeignKeyConstraint(
        ["Staff_ID"], ["staff.Staff_ID"], name = "fk_registration_staff"
    ) 
)

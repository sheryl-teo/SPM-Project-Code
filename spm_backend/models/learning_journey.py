from sqlalchemy import Column, Table , ForeignKeyConstraint, PrimaryKeyConstraint
from sqlalchemy.sql.sqltypes import Integer, String , Boolean
from config.db import meta

learning_journeys = Table(
     "learning_journey",
     meta,
    Column("Learning_Journey_ID", String(5), primary_key=True),
    Column("Staff_ID",Integer),  
    Column("Job_Role_ID",String(5)),
    ForeignKeyConstraint(
        ["Job_Role_ID", "Staff_ID"], ["job_role.Job_Role_ID", "staff.Staff_ID"]
    ) 
)

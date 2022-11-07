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
        ["Staff_ID"], ["staff.Staff_ID"], name = "fk_learning_journey_staff"
    ),
    ForeignKeyConstraint(
        ["Job_Role_ID"], ["job_role.Job_Role_ID"], name="fk_learning_journey_job_role"
    )
)

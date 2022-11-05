from sqlalchemy import Column, Table , ForeignKeyConstraint, PrimaryKeyConstraint
from sqlalchemy.sql.sqltypes import Integer, String , Boolean
from config.db import meta

job_role_soft_delete = Table (
    "job_role_soft_delete",
    meta,
    Column("Job_Role_ID" , String(5), primary_key= True ),
    Column("soft_delete" ,Boolean),
    ForeignKeyConstraint(
        ["Job_Role_ID"], ["Job_Role.Job_Role_ID"]
    ) 
    )


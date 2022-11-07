from sqlalchemy import Column, Table
from sqlalchemy.sql.sqltypes import Integer, String
from config.db import meta, engine

job_roles = Table (
    "job_role",
    meta,
    Column("Job_Role_ID" , String(5), primary_key= True),
    Column("Job_Role_Name" , String(50)),
    Column("Job_Department" , String(50)),
    Column("Active", Integer )
    )
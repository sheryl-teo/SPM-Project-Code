from sqlalchemy import Column, Table , ForeignKeyConstraint, PrimaryKeyConstraint
from sqlalchemy.sql.sqltypes import Integer, String, Boolean
from config.db import meta

job_role_skills = Table (
    "job_role_skill",
    meta,
    Column("Job_Role_ID" , String(5), primary_key= True ),
    Column("Skill_ID" , String(5), primary_key = True ),
    Column("soft_delete", Boolean),
    ForeignKeyConstraint(
        ["Job_Role_ID", "Skill_ID"], ["Job_Role.Job_Role_ID", "skill.Skill_ID"]
    ) 
    )


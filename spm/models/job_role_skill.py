from sqlalchemy import Column, Table , ForeignKeyConstraint, PrimaryKeyConstraint
from sqlalchemy.sql.sqltypes import Integer, String, Boolean
from config.db import meta

job_role_skills = Table (
    "job_role_skill",
    meta,
    Column("Job_Role_ID" , String(5), primary_key= True ),
    Column("Skill_ID" , String(5), primary_key = True ),
    Column("Active", Integer),
    ForeignKeyConstraint(
        ["Job_Role_ID"],["job_role.Job_Role_ID"], name = "fk_job_role_skill_jr"
    ),
    ForeignKeyConstraint(
        ["Skill_ID"], ["skill.Skill_ID"], name = "fk_job_role_skill_s"
    )
    )


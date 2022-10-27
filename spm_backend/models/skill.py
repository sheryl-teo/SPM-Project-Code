from sqlalchemy import Column, Table
from sqlalchemy.sql.sqltypes import Integer, String 
from config.db import meta

skills = Table(
     "skill",
     meta,
    Column("Skill_ID", String(5), primary_key=True),
    Column("Skill_Name", String(50)),
)


from sqlalchemy import Column, Table , ForeignKeyConstraint, PrimaryKeyConstraint
from sqlalchemy.sql.sqltypes import Integer, String, Boolean
from config.db import meta

skill_courses = Table(
     "skill_course",
     meta,
    Column("Course_ID", String(20), primary_key=True),
    Column("Skill_ID", String(5), primary_key=True),
    Column("soft_delete", Boolean),
    ForeignKeyConstraint(
        ["Course_ID", "Skill_ID"], ["course.Course_ID", "skill.Skill_ID"]
    ) 
)


from sqlalchemy import Column, Table , ForeignKeyConstraint, PrimaryKeyConstraint
from sqlalchemy.sql.sqltypes import Integer, String, Boolean
from config.db import meta

skill_courses = Table(
     "skill_course",
     meta,
    Column("Course_ID", String(20), primary_key=True),
    Column("Skill_ID", String(5), primary_key=True),
    Column("Active", Integer),
    ForeignKeyConstraint(
        ["Course_ID"], ["course.Course_ID"], name = "fk_skill_course_course"
    ),
    ForeignKeyConstraint(
        ["Skill_ID"], ["skill.Skill_ID"], name = "fk_skill_course_skill"
    )
)


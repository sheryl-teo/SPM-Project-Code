from sqlalchemy import Column, Table , ForeignKeyConstraint, PrimaryKeyConstraint
from sqlalchemy.sql.sqltypes import Integer, String  
from config.db import meta, engine

learning_journey_courses = Table(
     "learning_journey_course",
     meta,
    Column("Learning_Journey_ID", String(5), primary_key=True),
    Column("Course_ID",String(10),primary_key = True),  
    ForeignKeyConstraint(
        ["Learning_Journey_ID"], ["learning_Journey.Learning_Journey_ID"], name = "fk_learning_journey_course_learning_journey"
    ),
    ForeignKeyConstraint(
        ["Course_ID"], ["course.Course_ID"], name = "fk_learning_journey_course_course"
    )
)

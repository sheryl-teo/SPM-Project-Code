from sqlalchemy import Column, Table , ForeignKeyConstraint, PrimaryKeyConstraint
from sqlalchemy.sql.sqltypes import Integer, String , Boolean
from config.db import meta

learning_journey_skills = Table(
     "learning_journey_skill",
     meta,
    Column("Learning_Journey_ID", String(5), primary_key=True),
    Column("Skill_ID",String(5),primary_key = True),  
    Column("Obtained",Boolean),
    # ForeignKeyConstraint(
    #     ["Learning_Journey_ID"], ["learning_Journey.Learning_Journey_ID"], name = "fk_learning_journey"
    # ) 
)



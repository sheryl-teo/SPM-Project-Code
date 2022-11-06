from sqlalchemy import Column, Table , ForeignKeyConstraint, PrimaryKeyConstraint
from sqlalchemy.sql.sqltypes import Integer, String , Boolean
from config.db import meta

learning_journey_skills = Table(
     "learning_journey_skill",
     meta,
    Column("Learning_Journey_ID", String(5), primary_key=True),
    Column("Skill_ID",String(5),primary_key = True),  
    Column("Obtained",Integer),
    ForeignKeyConstraint(
        ["Learning_Journey_ID", "Skill_ID"], ["learning_Journey.Learning_Journey_ID", "skill.Skill_ID"]
    ) 
)



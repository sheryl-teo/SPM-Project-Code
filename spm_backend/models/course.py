from sqlalchemy import Column, Table
from sqlalchemy.sql.sqltypes import Integer, String
from config.db import meta, engine

courses = Table(
     "course",
     meta,
    Column("Course_ID", String(20), primary_key=True),
    Column("Course_Name",String(50)),
    Column("Course_Desc", String(255)),
    Column("Course_Status", String(15)),
    Column("Course_Type", String(10)),
    Column("Course_Category", String(50)),
)



# meta.create_all(engine)
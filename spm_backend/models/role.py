from sqlalchemy import Column, Table , ForeignKeyConstraint, PrimaryKeyConstraint
from sqlalchemy.sql.sqltypes import Integer, String 
from config.db import meta

roles = Table(
     "role",
     meta,
    Column("Role_ID", Integer, primary_key=True),
    Column("Role_Name", String(20))
)
  

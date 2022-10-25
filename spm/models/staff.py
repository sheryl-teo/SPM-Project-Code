from sqlalchemy import Column, Table , ForeignKeyConstraint
from sqlalchemy.sql.sqltypes import Integer, String 
from config.db import meta

staffs = Table(
     "staff",
     meta,
    Column("Staff_ID", Integer, primary_key=True),
    Column("Staff_FName", String(50)),
    Column("Staff_LName", String(50)),
    Column("Dept", String(50)),
    Column("Email", String(50)),
    Column("Role", Integer),
    ForeignKeyConstraint(
        ["Role"], ["role.Role_ID"]
    ) 
)


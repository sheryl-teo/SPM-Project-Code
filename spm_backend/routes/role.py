from fastapi import APIRouter
from config.db import conn
from schemas.role import Role
from models.role import roles
from typing import List
from sqlalchemy import func, select, text

role = APIRouter()

@role.get(
    "/role/get_all_role",
    tags=["role"],
    response_model=List[Role],
    description="Get a list of all roles",
)
def get_all_role():
    return conn.execute(roles.select()).fetchall()
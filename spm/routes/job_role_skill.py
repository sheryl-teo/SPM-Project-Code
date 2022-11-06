from fastapi import APIRouter
from config.db import conn
from schemas.job_role_skill import Job_role_skill
from models.job_role_skill import job_role_skills
from typing import List
from sqlalchemy import func, select

job_role_skill = APIRouter()

@job_role_skill.post( 
    "/job_role_skill/create",
    tags=["job_role_skills"],
    description="Assign skills to a job role, returns the skills a job role has",
)
def create(job_skill: Job_role_skill):
    #create new job role skil
    #happens when a new job role is created
    conn.execute(job_role_skills.insert().values(
        Job_Role_ID = job_skill.Job_Role_ID,
        Skill_ID = job_skill.Skill_ID,
        Active = job_skill.Active
    )) 
    #return all skills pertaining to the job role
    return conn.execute(job_role_skills.select().where(job_role_skills.c.Job_Role_ID == job_skill.Job_Role_ID)).fetchall()

@job_role_skill.get(
    "/job_role_skill/get_job_role_skill/",
    tags=["job_role_skills"],
    description="Get all job role skills",
)
def get_job_role_skill():
    #get all job role skill in db
    return conn.execute(job_role_skills.select()).fetchall()


@job_role_skill.get(
    "/job_role_skill/get_by_jr_id/{Job_Role_ID}",
    tags=["job_role_skills"],
    description="Get a list of all skills of a job role",
)
def get_by_jr_id(Job_Role_ID: str):
    #get all skills pertaining to a job role
    return conn.execute(job_role_skills.select().where(job_role_skills.c.Job_Role_ID == Job_Role_ID)).fetchall()



@job_role_skill.get(
    "/job_role_skill/get_by_skill_id/{Skill_ID}",
    tags=["job_role_skills"],
    description="Get a list of all job role a skill belongs to",
)
def get_by_skill_id(Skill_ID: str):
    #get all job roles pertaining to a skill
    return conn.execute(job_role_skills.select().where(job_role_skills.c.Skill_ID == Skill_ID)).fetchall()



@job_role_skill.put(
    "/job_roles_skill/delete",
    tags=["job_role_skills"],
    description="Delete/undelete a job role skill row",
)
def delete(jrs: Job_role_skill):
    # soft delete a job role skill row by changing the active value
    # active = 0(retired)
    conn.execute(job_role_skills.update().values(
        Job_Role_ID = jrs.Job_Role_ID,
        Skill_ID = jrs.Skill_ID,
        Active = 0
    ).where((job_role_skills.c.Skill_ID == jrs.Skill_ID) & (job_role_skills.c.Job_Role_ID == jrs.Job_Role_ID))) 
    #return updated job_role_skill
    return conn.execute(job_role_skills.select().where((job_role_skills.c.Skill_ID == jrs.Skill_ID) & (job_role_skills.c.Job_Role_ID == jrs.Job_Role_ID))).fetchall()

@job_role_skill.put(
    "/job_roles_skill/undelete",
    tags=["job_role_skills"],
    description="Delete/undelete a job role skill row",
)
def undelete(jrs: Job_role_skill):
    # soft undelete a job role skill row by changing the active value
    # active = 1(active)
    conn.execute(job_role_skills.update().values(
        Job_Role_ID = jrs.Job_Role_ID,
        Skill_ID = jrs.Skill_ID,
        Active = 1
    ).where((job_role_skills.c.Skill_ID == jrs.Skill_ID) & (job_role_skills.c.Job_Role_ID == jrs.Job_Role_ID))) 
    #return updated  job_role_skill
    return conn.execute(job_role_skills.select().where((job_role_skills.c.Skill_ID == jrs.Skill_ID) & (job_role_skills.c.Job_Role_ID == jrs.Job_Role_ID))).fetchall()




# errors = [error_2(search_skill_ID), error_3(search_skill_ID)]
# errors_list = [e for e in errors if e != None]
# if len(errors_list) == 0:
#     statement = skills.insert([skill])
#     return conn.execute(statement)
# else:
#     return {'errors': errors_list}



# @job_role_skill.put(
#     "/job_roles_skill/delete_job_role/{Job_Role_ID}",
#     tags=["job_role_skills"],
#     description="Delete a specified job role",
# )
# def delete_job_role(Job_Role_ID: str, Active: int):
#     conn.execute(job_role_skills.update().values(
#         Active = Active
#     ).where(job_role_skills.c.Job_Role_ID == Job_Role_ID)) 
#     return conn.execute(job_role_skills.select().where(job_role_skills.c.Job_Role_ID == Job_Role_ID)).fetchall()

# @job_role_skill.put(
#     "/job_roles_skill/delete_skill/{Skill_ID}",
#     tags=["job_role_skills"],
#     description="Delete a specified job role",
# )
# def delete_skill(Skill_ID: str, Active: int):
#     conn.execute(job_role_skills.update().values(
#         Active = Active
#     ).where(job_role_skills.c.Skill_ID == Skill_ID)) 
#     return conn.execute(job_role_skills.select().where(job_role_skills.c.Skill_ID == Skill_ID)).fetchall()

    
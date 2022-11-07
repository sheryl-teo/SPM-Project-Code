from fastapi import APIRouter
from config.db import conn
from schemas.job_role import Job_role
from models.job_role import job_roles
from schemas.job_role_skill import Job_role_skill
from models.job_role_skill import job_role_skills
from schemas.learning_journey import Learning_journey
from models.learning_journey import learning_journeys
from typing import List
from sqlalchemy import func, select

job_role = APIRouter()


#####################################
#error handling
#####################################
def error_1(search_jobrole_ID: str):
    search = job_roles.select().where(job_roles.c.Job_Role_ID==search_jobrole_ID)
    result = conn.execute(search)
    result_dict = result.mappings().all()
    if result_dict == []: 
        error_msg = {
            'Error_ID': 'JR1', 
            'Error_Desc': '''The job role you're looking for is not inside our database. Check your search terms and try again.''',
            'Error_Details': ''
        }
    else: 
        error_msg = None
    
    return error_msg

def error_2(search_jobrole_ID: str):
    search = job_roles.select().where(job_roles.c.Job_Role_ID==search_jobrole_ID)
    result = conn.execute(search)
    result_dict = result.mappings().all()

    if result_dict != []: 
        error_msg = {
            'Error_ID': 'JR2', 
            'Error_Desc': '''This job role is already within our database. Check your job role details and try again.''',
            'Error_Details': ''
        }
    else: 
        error_msg = None
    
    return error_msg 

def can_convert_to_int(string: str):
    try:
        int(string)
        return True
    except ValueError:
        return False

def error_3(search_jobrole_ID: str):
    letter_check = search_jobrole_ID[:2] == 'JR'
    print(search_jobrole_ID[:2])
    print('letter_check', letter_check)
    int_check = can_convert_to_int(search_jobrole_ID[2:])
    if letter_check == False or int_check == False:
        error_msg = {
            'Error_ID': 'JR3', 
            'Error_Desc': '''This job role has an invalid job role ID. Check your job role ID and try again.''',
            'Error_Details': ''
        }
    else: 
        error_msg = None
    return error_msg

def error_4(search_jobrole_name: str):
    if len(search_jobrole_name) <= 0:
        error_msg = {
            'Error_ID': 'JR4', 
            'Error_Desc': '''This job role does not have a job role name. Check your job role name and try again.''',
            'Error_Details': ''
        }
    else: 
        error_msg = None
    return error_msg 

def error_5(search_jobrole_name: str):
    if len(search_jobrole_name) > 50:
        error_msg = {
            'Error_ID': 'JR5', 
            'Error_Desc': '''This job role name is too long (more than 50 characters). Check your job role name and try again.''',
            'Error_Details': ''
        }
    else: 
        error_msg = None
    return error_msg

def error_6(search_jobrole_dept: str):
    search_jobrole_dept = search_jobrole_dept.lower()
    dept_list = [
        'Chairman',
        'CEO',
        'Sales',
        'Ops',
        'HR',
        'Finance'
    ]

    is_error = False
    is_substring_error = True
    error_msg = {
        'Error_ID': 'JR6', 
        'Error_Desc': '''This job role department is not valid (Chairman, CEO, Sales, Ops, HR, Finance). Check your job department and try again.''',
        'Error_Details': ''
    }

    if search_jobrole_dept == '':
        is_error = True
    elif search_jobrole_dept not in dept_list:
        for dept in dept_list:
            dept_lower = dept.lower()
            if search_jobrole_dept in dept_lower:
                is_substring_error = False 
        is_error = is_substring_error


    return error_msg if is_error else None
#####################################
#error handling
#####################################



@job_role.get(
    "/jobroles/",
    tags=["job_roles"],
    response_model=List[Job_role],
    description="Get a list of all job roles details",
)
def get_all_jobrole():
    return conn.execute(job_roles.select()).fetchall()

# Create
@job_role.post(
    "/jobroles/create",
    tags=["job_roles"],
    description="Create a job role",
)
def create_jobrole(job: Job_role):
    job.Job_Role_ID = job.Job_Role_ID.capitalize()
    search_jobrole_ID = job.Job_Role_ID
    search_jobrole_name = job.Job_Role_Name
    search_jobrole_dept = job.Job_Department

    errors = [error_2(search_jobrole_ID), error_3(search_jobrole_ID), error_4(search_jobrole_name), error_5(search_jobrole_name), error_6(search_jobrole_dept)]
    errors_list = [e for e in errors if e != None]

    if len(errors_list) == 0:
        conn.execute(job_roles.insert().values(
            Job_Role_ID = job.Job_Role_ID.capitalize(),
            Job_Role_Name = job.Job_Role_Name,
            Job_Department = job.Job_Department,
            Active = job.Active
        ))

        return conn.execute(job_roles.select().where(job_roles.c.Job_Role_ID == job.Job_Role_ID)).fetchall()

    else:
        return {'errors': errors_list}

# Read 
@job_role.get(
    "/jobroles/read/id/{search_jobrole_ID}",
    tags=["job_roles"],
    description="Reads a job role through an exact match search by job ID.",
)
def read_jobrole_id(search_jobrole_ID: str):
    search_jobrole_ID = search_jobrole_ID.upper()

    errors = [error_1(search_jobrole_ID), error_3(search_jobrole_ID)]
    errors_list = [e for e in errors if e != None]
    if len(errors_list) == 0:
        statement = job_roles.select().where(job_roles.c.Job_Role_ID==search_jobrole_ID)
        return conn.execute(statement).all()
    else:
        return {'errors': errors_list}

@job_role.get(
    "/jobroles/read/dept/{search_jobrole_dept}",
    tags=["job_roles"],
    description="Get a list of job roles by department",
)
def read_jobrole_department(search_jobrole_dept: str):
    errors = [error_6(search_jobrole_dept)]
    errors_list = [e for e in errors if e != None]

    if len(errors_list) == 0:
        return conn.execute(job_roles.select().where(func.lower(job_roles.c.Job_Department).contains(search_jobrole_dept))).all()
    else:
        return {'errors': errors_list}

@job_role.get(
    "/jobroles/read/name/{search_jobrole_name}",
    tags=["job_roles"],
    description="Get a list of job roles by name",
)
def read_jobrole_name(search_jobrole_name: str):
    return conn.execute(job_roles.select().where(func.lower(job_roles.c.Job_Role_Name).contains(search_jobrole_name))).all()

# Update 
@job_role.post(
    "/jobroles/update",
    tags=["job_roles"],
    description="Update a specified job role",
)

async def update_jobrole(job: Job_role):
    job.Job_Role_ID = job.Job_Role_ID.upper()
    search_jobrole_ID = job.Job_Role_ID
    search_jobrole_name = job.Job_Role_Name
    search_jobrole_dept = job.Job_Department

    errors = [error_1(search_jobrole_ID), error_3(search_jobrole_ID), error_4(search_jobrole_name), error_5(search_jobrole_name), error_6(search_jobrole_dept)]
    errors_list = [e for e in errors if e != None]
    if len(errors_list) == 0:
        statement = job_roles.update().values(
            Job_Role_Name = job.Job_Role_Name,
            Job_Department = job.Job_Department,
            Active = job.Active
        ).where(job_roles.c.Job_Role_ID==job.Job_Role_ID)
        conn.execute(statement)
        return conn.execute(job_roles.select().where(job_roles.c.Job_Role_ID == job.Job_Role_ID)).fetchall()
    else:
        return {'errors': errors_list}

# Soft delete 
@job_role.post(
    "/jobroles/delete/soft/{search_jobrole_ID}",
    tags=["job_roles"],
    description="Soft delete a specified job role",
)
def delete_jobrole_soft(search_jobrole_ID: str):
    search_jobrole_ID = search_jobrole_ID.upper()
    errors = [error_1(search_jobrole_ID), error_3(search_jobrole_ID)]
    errors_list = [e for e in errors if e != None]

    if len(errors_list) == 0:
        # Job role 
        jobrole_statement = job_roles.update().values(
            Active = 0
        ).where(job_roles.c.Job_Role_ID==search_jobrole_ID)
        conn.execute(jobrole_statement)

        # Job role skill
        job_role_skill_statement = job_role_skills.update().values(
            Active = 0
        ).where(job_role_skills.c.Job_Role_ID==search_jobrole_ID)
        conn.execute(job_role_skill_statement)
        
        #return deleted job role
        return conn.execute(job_roles.select().where(job_roles.c.Job_Role_ID == search_jobrole_ID)).fetchall()

    else:
        return {'errors': errors_list}

# Soft undelete
@job_role.post(
    "/jobroles/delete/softrestore/{search_jobrole_ID}",
    tags=["job_roles"],
    description="Soft undelete a specified job role",
)
def delete_jobrole_softrestore(search_jobrole_ID: str):
    search_jobrole_ID = search_jobrole_ID.upper()
    errors = [error_1(search_jobrole_ID), error_3(search_jobrole_ID)]
    errors_list = [e for e in errors if e != None]

    if len(errors_list) == 0:
        # Job role 
        jobrole_statement = job_roles.update().values(
            Active = 1
        ).where(job_roles.c.Job_Role_ID==search_jobrole_ID)
        conn.execute(jobrole_statement)

        # Job role skill
        job_role_skill_statement = job_role_skills.update().values(
            Active = 1
        ).where(job_role_skills.c.Job_Role_ID==search_jobrole_ID)
        conn.execute(job_role_skill_statement)
        
        return conn.execute(job_roles.select().where(job_roles.c.Job_Role_ID == search_jobrole_ID)).fetchall()
        
    else:
        return {'errors': errors_list}

# @job_role.get(
#     "/jobroles/delete/hard/{search_jobrole_ID}",
#     tags=["job_roles"],
#     description="Hard delete a specified job role",
# )
# def delete_jobrole_hard(search_jobrole_ID: str):
#     search_jobrole_ID = search_jobrole_ID.upper()
#     errors = [error_1(search_jobrole_ID), error_3(search_jobrole_ID)]
#     errors_list = [e for e in errors if e != None]

#     if len(errors_list) == 0:
#         # Job role skill
#         job_role_skill_statement = job_role_skills.delete().where(job_role_skills.c.Job_Role_ID==search_jobrole_ID)
#         conn.execute(job_role_skill_statement)

#         # Job role 
#         jobrole_statement = job_roles.delete().where(job_roles.c.Job_Role_ID==search_jobrole_ID)
#         conn.execute(jobrole_statement)
        
#         return conn.execute(job_roles.select().where(job_roles.c.Job_Role_ID == search_jobrole_ID)).fetchall()

#     else:
#         return {'errors': errors_list}


from fastapi import APIRouter
from config.db import conn
from schemas.skill import Skill
from models.skill import skills
from schemas.job_role_skill import Job_role_skill
from models.job_role_skill import job_role_skills
from schemas.skill_course import Skill_course
from models.skill_course import skill_courses
from typing import List
from sqlalchemy import func, select

skill = APIRouter()

#####################################
#error handling
#####################################
def error_1(search_skill_ID: str):
    search = skills.select().where(skills.c.Skill_ID==search_skill_ID)
    result = conn.execute(search)
    result_dict = result.mappings().all()
    print('result_dict', result_dict)
    if result_dict == []: 
        error_msg = {
            'Error_ID': 'S1', 
            'Error_Desc': '''The skill you're looking for is not inside our database. Check your search terms and try again.''',
            'Error_Details': ''
        }
    else: 
        error_msg = None
    
    return error_msg 

def error_2(search_skill_ID: str):
    search = skills.select().where(skills.c.Skill_ID==search_skill_ID)
    result = conn.execute(search)
    result_dict = result.mappings().all()

    if result_dict != []: 
        error_msg = {
            'Error_ID': 'S2', 
            'Error_Desc': '''This skill is already within our database. Check your skill details and try again.''',
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

def error_3(search_skill_ID: str):
    letter_check = search_skill_ID[0] == 'S'
    int_check = can_convert_to_int(search_skill_ID[1:])
    if letter_check == False or int_check == False:
        error_msg = {
            'Error_ID': 'S3', 
            'Error_Desc': '''This skill has an invalid skill ID. Check your skill ID and try again.''',
            'Error_Details': ''
        }
    else: 
        error_msg = None
    return error_msg 

def error_4(search_skill_name: str):
    if len(search_skill_name) <= 0:
        error_msg = {
            'Error_ID': 'S4', 
            'Error_Desc': '''This skill does not have a skill name. Check your skill name and try again.''',
            'Error_Details': ''
        }
    else: 
        error_msg = None
    return error_msg 

def error_5(search_skill_name: str):
    if len(search_skill_name) > 50:
        error_msg = {
            'Error_ID': 'S5', 
            'Error_Desc': '''This skill is too long (more than 50 characters). Check your skill name and try again.''',
            'Error_Details': ''
        }
    else: 
        error_msg = None
    return error_msg 
#####################################
#error handling
#####################################



@skill.get(
    "/skills",
    tags=["skills"],
    description="Get a list of all skills",
)
def get_all_skill():
    return conn.execute(skills.select()).fetchall()

# Create
@skill.post(
    "/skills/create",
    tags=["skills"],
    description="Create a new skill.",
)
async def create_skill(skill: Skill):
    """Create a new skill.

    Args:
        skill (dict): JSON dictionary, containing Skill_ID and Skill_Name

    Returns:
        _type_: _description_
    """
    skill.Skill_ID = skill.Skill_ID.upper()
    search_skill_ID = skill.Skill_ID
    search_skill_name = skill.Skill_Name

    errors = [error_2(search_skill_ID), error_3(search_skill_ID), error_4(search_skill_name), error_5(search_skill_name)]
    errors_list = [e for e in errors if e != None]
    if len(errors_list) == 0:
        statement = skills.insert().values(
            Skill_ID = skill.Skill_ID,
            Skill_Name = skill.Skill_Name,
            Active = skill.Active
        )
        conn.execute(statement)
        return conn.execute(skills.select().where(skills.c.Skill_ID == skill.Skill_ID)).fetchall()
    else:
        return {'errors': errors_list}

# Read 
@skill.get(
    "/skills/read/id/{search_skill_ID}",
    tags=["skills"],
    description="Reads a skill through an exact match search by skill ID.",
)
def read_skill_id(search_skill_ID: str):
    """Reads a skill through an exact match search by skill ID.

    Args:
        search_skill_ID (str): Skill ID, following the format "SXX", 
        with XX representing the skill number.

    Returns:
        _type_: _description_
    """
    search_skill_ID = search_skill_ID.upper()

    errors = [error_1(search_skill_ID), error_3(search_skill_ID)]
    print('errors', errors)
    errors_list = [e for e in errors if e != None]
    if len(errors_list) == 0:
        statement = skills.select().where(skills.c.Skill_ID==search_skill_ID)
        return conn.execute(statement).all()
    else:
        return {'errors': errors_list}


@skill.get(
    "/skills/read/name/{search_skill_name}",
    tags=["skills"],
    description="Reads a skill through a substring match search by skill name.",
)
def read_skill_name(search_skill_name: str):
    """Reads a skill through a substring match search by skill name.

    Args:
        search_skill_name (str): The name of the skill being searched.

    Returns:
        _type_: _description_
    """
    search_skill_name = search_skill_name.lower()
    statement = skills.select().where(func.lower(skills.c.Skill_Name).contains(search_skill_name))
    return conn.execute(statement).all()

# Update 
@skill.post(
    "/skills/update",
    tags=["skills"],
    description="Update an existing skill.",
)
async def update_skill(search_skill: Skill):
    """Update an existing skill.

    Args:
        skill (dict): JSON dictionary, containing Skill_ID and Skill_Name

    Returns:
        _type_: _description_
    """
    search_skill.Skill_ID = search_skill.Skill_ID.upper()
    search_skill_ID = search_skill.Skill_ID
    search_skill_name = search_skill.Skill_Name

    errors = [error_1(search_skill_ID), error_3(search_skill_ID), error_4(search_skill_name), error_5(search_skill_name)]
    errors_list = [e for e in errors if e != None]
    if len(errors_list) == 0:
        statement = skills.update().values(
            Skill_Name = search_skill.Skill_Name,
            Active = search_skill.Active
        ).where(skills.c.Skill_ID==search_skill_ID)
        conn.execute(statement)
        return conn.execute(skills.select().where(skills.c.Skill_ID == search_skill.Skill_ID)).fetchall()
    else:
        return {'errors': errors_list}

# Soft delete 
@skill.get(
    "/skills/delete/soft/{search_skill_ID}",
    tags=["skills"],
    description="Soft delete an existing skill.",
)
def delete_skill_soft(search_skill_ID: str):
    """Soft delete an existing skill.

    Args:
        search_skill_ID (str): Skill ID, following the format "SXX", 
        with XX representing the skill number.
    """
    search_skill_ID = search_skill_ID.upper()
    errors = [error_1(search_skill_ID), error_3(search_skill_ID)]
    errors_list = [e for e in errors if e != None]
    if len(errors_list) == 0:
        # Skill
        skill_statement = skills.update().values(
            Active = 0
        ).where(skills.c.Skill_ID==search_skill_ID)
        conn.execute(skill_statement)

        #Job role skill
        job_role_skill_statement = job_role_skills.update().values(
            Active = 0
        ).where(job_role_skills.c.Skill_ID == search_skill_ID)
        conn.execute(job_role_skill_statement)

        #Skill courses
        skill_course_statement = skill_courses.update().values(
            Active = 0
        ).where(skill_courses.c.Skill_ID == search_skill_ID)
        conn.execute(skill_course_statement)

        #return soft deleted skill
        return conn.execute(skills.select().where(skills.c.Skill_ID == search_skill_ID)).fetchall()
    else:
        return {'errors': errors_list}

# Soft undelete 
@skill.get(
    "/skills/delete/softrestore/{search_skill_ID}",
    tags=["skills"],
    description="Soft undelete an existing skill.",
)
def delete_skill_soft(search_skill_ID: str):
    """Soft undelete an existing skill.

    Args:
        search_skill_ID (str): Skill ID, following the format "SXX", 
        with XX representing the skill number.
    """
    search_skill_ID = search_skill_ID.upper()
    errors = [error_1(search_skill_ID), error_3(search_skill_ID)]
    errors_list = [e for e in errors if e != None]

    if len(errors_list) == 0:
        # Skill
        skill_statement = skills.update().values(
            Active = 1
        ).where(skills.c.Skill_ID==search_skill_ID)
        conn.execute(skill_statement)

        #Job role skill
        job_role_skill_statement = job_role_skills.update().values(
            Active = 1
        ).where(job_role_skills.c.Skill_ID == search_skill_ID)
        conn.execute(job_role_skill_statement)

        #Skill courses
        skill_course_statement = skill_courses.update().values(
            Active = 1
        ).where(skill_courses.c.Skill_ID == search_skill_ID)
        conn.execute(skill_course_statement)

        #return soft undeleted skill
        return conn.execute(skills.select().where(skills.c.Skill_ID == search_skill_ID)).fetchall()
    else:
        return {'errors': errors_list}

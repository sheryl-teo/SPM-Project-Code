# import unittest
# from testcases import job_role_test

# class testjobrole(unittest.TestCase):
#     def testcreatejobrole(self):
#         s = JobRole("JR100","Finance manager","Finance")
#         job_role_id = s.job_role_id
#         job_role_name = s.job_role_name
#         job_department = s.job_department
#         self.assertEqual(s.job_role_id,"JR100")
#         self.assertEqual(s.job_role_name,"Finance manager")
#         self.assertEqual(s.job_department,"Finance")
#         s.create_job_role(job_role_id, job_role_name, job_department)
#         self.assertEqual()

from fastapi import FastAPI
from fastapi.testclient import TestClient
from app import app

client = TestClient(app)

# def testcreatejobrole():
#     response = client.post(
#         "/job_role/create_job_role",
#         json={
#             "Job_Role_ID": "JR111",
#             "Job_Role_Name": "string",
#             "Job_Department": "string"
#             })
#     assert response.status_code == 200
#     assert response.json() == [
#             {
#                 "Job_Role_ID": "JR111",
#                 "Job_Role_Name": "string",
#                 "Job_Department": "string"
#             }
#             ]

# Skills 

# Create 
def test_create_skill_1():
    """Happy Path
    """
    test_setup = client.get("/skills/delete/hard/S88")
    response = client.post("/skills/create",
        json = {
            "Skill_ID": "S88",
            "Skill_Name": "Test Skill 88",
            "Active": 1
        }
    )
    assert response.status_code == 200
    assert response.json() == [
        {
            "Skill_ID": "S88",
            "Skill_Name": "Test Skill 88",
            "Active": 1
        }
    ]

def test_create_skill_2():
    """Error: Skill ID already exists
    """
    response = client.post(
        "/skills/create",
        json = {
            "Skill_ID": "S11",
            "Skill_Name": "Data analysis",
            "Active": 1
        }
    )
    assert response.status_code == 200
    assert response.json() == {
        "errors": [
            {
                "Error_ID": "S2",
                "Error_Desc": "This skill is already within our database. Check your skill details and try again.",
                "Error_Details": ""
            }
        ]
    }

def test_create_skill_3():
    """Error: Invalid Skill ID - First Letter Not S
    """
    response = client.post(
        "/skills/create",
        json = {
            "Skill_ID": "C88",
            "Skill_Name": "Test Skill 88",
            "Active": 1
        }
    )
    assert response.status_code == 200
    assert response.json() == {
    "errors": [
            {
                "Error_ID": "S3",
                "Error_Desc": "This skill has an invalid skill ID. Check your skill ID and try again.",
                "Error_Details": ""
            }
        ]
    }


def test_create_skill_4():
    """Valid Skill ID: First Letter Lowercase S
    """
    test_setup = client.get("/skills/delete/hard/S88")

    response = client.post(
        "/skills/create",
        json = {
            "Skill_ID": "s88",
            "Skill_Name": "Test Skill 88",
            "Active": 1
        }
    )
    assert response.status_code == 200
    assert response.json() == [
        {
            "Skill_ID": "S88",
            "Skill_Name": "Test Skill 88", 
            "Active": 1
        }
    ]
    
def test_create_skill_5():
    """Error: Valid Skill ID: Identifying section not numbers
    """
    response = client.post(
        "/skills/create",
        json = {
            "Skill_ID": "STU",
            "Skill_Name": "Test Skill TU",
            "Active": 1
        }
    )
    assert response.status_code == 200
    assert response.json() == {
    "errors": [
            {
                "Error_ID": "S3",
                "Error_Desc": "This skill has an invalid skill ID. Check your skill ID and try again.",
                "Error_Details": ""
            }
        ]
    }

def test_create_skill_6():
    """Error: Invalid Skill Name - Empty name
    """
    test_setup = client.get("/skills/delete/hard/S88")

    response = client.post(
        "/skills/create",
        json = {
            "Skill_ID": "S88",
            "Skill_Name": "",
            "Active": 1
        }
    )
    assert response.status_code == 200
    assert response.json() == {
    "errors": [
        {
            "Error_ID": "S4",
            "Error_Desc": "This skill does not have a skill name. Check your skill name and try again.",
            "Error_Details": ""
        }
    ]
}

def test_create_skill_7():
    """Invalid Skill Name - More than 50 characters
    """
    test_setup = client.get("/skills/delete/hard/S88")

    response = client.post(
        "/skills/create",
        json = {
            "Skill_ID": "S88",
            "Skill_Name": "Test Skill 88 Updated Updated Updated Updated Updated Updated",
            "Active": 1
        }
    )
    assert response.status_code == 200
    assert response.json() == {
        "errors": [
            {
                "Error_ID": "S5",
                "Error_Desc": "This skill is too long (more than 50 characters). Check your skill name and try again.",
                "Error_Details": ""
            }
        ]
    }

# Read 
def test_read_skill_skillID_1():
    """Happy Path: Read skill by skill ID
    """
    response = client.get("/skills/read/id/S11")
    assert response.status_code == 200
    assert response.json() == [
        {
            "Skill_ID": "S11",
            "Skill_Name": "Data analysis",
            "Active": 1
        }
    ]

def test_read_skill_skillID_2():
    """Error: Skill ID does not exist
    """
    response = client.get("/skills/read/id/S99")
    assert response.status_code == 200
    assert response.json() == {
    "errors": [
            {
                "Error_ID": "S1",
                "Error_Desc": "The skill you're looking for is not inside our database. Check your search terms and try again.",
                "Error_Details": ""
            }
        ]
    }

def test_read_skill_skillID_3():
    """Error: Invalid Skill ID - First Letter Not S
    """
    response = client.get("/skills/read/id/c11")
    assert response.status_code == 200
    assert response.json() == {
    "errors": [
            {
                "Error_ID": "S1",
                "Error_Desc": "The skill you're looking for is not inside our database. Check your search terms and try again.",
                "Error_Details": ""
            },
            {
                "Error_ID": "S3",
                "Error_Desc": "This skill has an invalid skill ID. Check your skill ID and try again.",
                "Error_Details": ""
            }
        ]
    }

def test_read_skill_skillID_4():
    """Happy Path: Read skill by skill ID
    """
    response = client.get("/skills/read/id/s11")
    assert response.status_code == 200
    assert response.json() == [
        {
            "Skill_ID": "S11",
            "Skill_Name": "Data analysis",
            "Active": 1
        }
    ]

def test_read_skill_SkillID_5():
    """Error: Invalid Skill ID - Following characters not numbers 
    """
    response = client.get("/skills/read/id/STU")
    assert response.status_code == 200
    assert response.json() == {
    "errors": [
        {
            "Error_ID": "S1",
            "Error_Desc": "The skill you're looking for is not inside our database. Check your search terms and try again.",
            "Error_Details": ""
        },
        {
            "Error_ID": "S3",
            "Error_Desc": "This skill has an invalid skill ID. Check your skill ID and try again.",
            "Error_Details": ""
        }
    ]
}

def test_read_skill_SkillID_6():
    """Valid: Inactive skill
    """
    response = client.get("/skills/read/id/S24")
    assert response.status_code == 200
    assert response.json() == [
        {
            "Skill_ID": "S24",
            "Skill_Name": "Open platforms communication",
            "Active": 0
        }
    ]


def test_read_skill_skillName_1():
    """Happy Path: Complete string match
    """
    response = client.get("/skills/read/name/Data analysis")
    assert response.status_code == 200
    assert response.json() == [
        {
            "Skill_ID": "S11",
            "Skill_Name": "Data analysis",
            "Active": 1
        }
    ]

def test_read_skill_skillName_2():
    """Valid: Camel capitalisation
    """
    response = client.get("/skills/read/name/Data Analysis")
    assert response.status_code == 200
    assert response.json() == [
        {
            "Skill_ID": "S11",
            "Skill_Name": "Data analysis",
            "Active": 1
        }
    ]

def test_read_skill_skillName_3():
    """Valid: Full capitalisation
    """
    response = client.get("/skills/read/name/DATA ANALYSIS")
    assert response.status_code == 200
    assert response.json() == [
        {
            "Skill_ID": "S11",
            "Skill_Name": "Data analysis",
            "Active": 1
        }
    ]

def test_read_skill_skillName_4():
    """Valid: No capitalisation
    """
    response = client.get("/skills/read/name/data analysis")
    assert response.status_code == 200
    assert response.json() == [
        {
            "Skill_ID": "S11",
            "Skill_Name": "Data analysis",
            "Active": 1
        }
    ]

def test_read_skill_skillName_5():
    """Valid: Partial string match
    """
    response = client.get("/skills/read/name/analysis")
    assert response.status_code == 200
    assert response.json() == [
        {
            "Skill_ID": "S11",
            "Skill_Name": "Data analysis",
            "Active": 1
        }
    ]

def test_read_skill_skillName_6():
    """Valid: Partial string match with camel capitalisation
    """
    response = client.get("/skills/read/name/Analysis")
    assert response.status_code == 200
    assert response.json() == [
        {
            "Skill_ID": "S11",
            "Skill_Name": "Data analysis",
            "Active": 1
        }
    ]

def test_read_skill_skillName_7():
    """Valid: Partial string match with full capitalisation
    """
    response = client.get("/skills/read/name/ANALYSIS")
    assert response.status_code == 200
    assert response.json() == [
        {
            "Skill_ID": "S11",
            "Skill_Name": "Data analysis",
            "Active": 1
        }
    ]

def test_read_skill_skillName_8():
    """Valid: Partial string match with multiple courses
    """
    response = client.get("/skills/read/name/thinking")
    assert response.status_code == 200
    assert response.json() == [
        {
            "Skill_ID": "S15",
            "Skill_Name": "Innovative thinking",
            "Active": 1
        },
        {
            "Skill_ID": "S19",
            "Skill_Name": "System thinking",
            "Active": 1
        },
        {
            "Skill_ID": "S20",
            "Skill_Name": "Strategic thinking",
            "Active": 1
        }
    ]

def test_read_skill_skillName_9():
    """Valid: No match
    """
    response = client.get("/skills/read/name/spm")
    assert response.status_code == 200
    assert response.json() == [
    ]

def test_read_skill_skillName_10():
    """Valid: Inactive skill
    """
    response = client.get("/skills/read/name/Open platforms communication")
    assert response.status_code == 200
    assert response.json() == [
        {
            "Skill_ID": "S24",
            "Skill_Name": "Open platforms communication",
            "Active": 0
        }
    ]


# Update 
def test_update_skill_1():
    """Happy Path
    """
    test_setup_0 = client.get("/skills/delete/hard/S88")
    test_setup_1 = client.post(
        "/skills/create",
        json = {
            "Skill_ID": "S88",
            "Skill_Name": "Test Skill 88",
            "Active": 1
        }
    )
    response = client.post(
        "/skills/update",
        json = {
            "Skill_ID": "S88",
            "Skill_Name": "Test Skill 88 Updated",
            "Active": 1
        }
    )
    assert response.status_code == 200
    assert response.json() == [
        {
            "Skill_ID": "S88",
            "Skill_Name": "Test Skill 88 Updated",
            "Active": 1
        }
    ]

def test_update_skill_2():
    """Error: Skill ID does not exist
    """
    response = client.post(
        "/skills/update",
        json = {
            "Skill_ID": "S99",
            "Skill_Name": "Test Skill 99 Updated",
            "Active": 1
        }
    )
    assert response.status_code == 200
    assert response.json() == {
    "errors": [
            {
                "Error_ID": "S1",
                "Error_Desc": "The skill you're looking for is not inside our database. Check your search terms and try again.",
                "Error_Details": ""
            }
        ]
    }

def test_update_skill_3():
    """Valid Path: No change
    """
    test_setup_0 = client.get("/skills/delete/hard/S88")

    test_setup_1 = client.post(
        "/skills/create",
        json = {
            "Skill_ID": "S88",
            "Skill_Name": "Test Skill 88 Updated",
            "Active": 1
        }

    )

    response = client.post(
        "/skills/update",
        json = {
            "Skill_ID": "S88",
            "Skill_Name": "Test Skill 88 Updated",
            "Active": 1
        }

    )
    assert response.status_code == 200
    assert response.json() == [
        {
            "Skill_ID": "S88",
            "Skill_Name": "Test Skill 88 Updated",
            "Active": 1
        }
    ]

    

def test_update_skill_4():
    """Valid Skill ID: First Letter Lowercase S
    """
    test_setup_0 = client.get("/skills/delete/hard/S88")

    test_setup_1 = client.post(
        "/skills/create",
        json = {
            "Skill_ID": "S88",
            "Skill_Name": "Test Skill 88 Updated",
            "Active": 1
        }
    )

    response = client.post(
        "/skills/update",
        json = {
            "Skill_ID": "s88",
            "Skill_Name": "Test Skill 88 Updated 2",
            "Active": 1
        }
    )
    assert response.status_code == 200
    assert response.json() == [
        {
            "Skill_ID": "S88",
            "Skill_Name": "Test Skill 88 Updated 2",
            "Active": 1
        }
    ]

    

def test_update_skill_5():
    """Error: Invalid Skill Name - Empty name
    """
    test_setup_0 = client.get("/skills/delete/hard/S88")
    test_setup_1 = client.post(
        "/skills/create",
        json = {
            "Skill_ID": "S88",
            "Skill_Name": "Test Skill 88 Updated",
            "Active": 1
        }
    )

    response = client.post(
        "/skills/update",
        json = {
            "Skill_ID": "S88",
            "Skill_Name": "",
            "Active": 1
        }
    )
    assert response.status_code == 200
    assert response.json() == {
        "errors": [
                {
                    "Error_ID": "S4",
                    "Error_Desc": "This skill does not have a skill name. Check your skill name and try again.",
                    "Error_Details": ""
                }
            ]
        }

    

def test_update_skill_6():
    """Error: Invalid Skill Name - More than 50 characters
    """
    test_setup_0 = client.get("/skills/delete/hard/S88")
    test_setup_1 = client.post(
        "/skills/create",
        json = {
            "Skill_ID": "S88",
            "Skill_Name": "Test Skill 88 Updated",
            "Active": 1
        }
    )

    response = client.post(
        "/skills/update",
        json = {
            "Skill_ID": "S88",
            "Skill_Name": "Test Skill 88 Updated Updated Updated Updated Updated Updated",
            "Active": 1
        }
    )
    assert response.status_code == 200
    assert response.json() == {
        "errors": [
                {
                    'Error_ID': 'S5', 
                    'Error_Desc': '''This skill is too long (more than 50 characters). Check your skill name and try again.''',
                    'Error_Details': ''
                }
            ]
        }

def test_update_skill_7():
    """Valid: Change skill active status
    """
    test_setup_0 = client.get("/skills/delete/hard/S88")
    test_setup_1 = client.post(
        "/skills/create",
        json = {
            "Skill_ID": "S88",
            "Skill_Name": "Test Skill 88 Updated",
            "Active": 1
        }
    )

    response = client.post(
        "/skills/update",
        json = {
            "Skill_ID": "S88",
            "Skill_Name": "Test Skill 88 Updated",
            "Active": 0
        }
    )
    assert response.status_code == 200
    assert response.json() == [
        {
            "Skill_ID": "S88",
            "Skill_Name": "Test Skill 88 Updated",
            "Active": 0
        }
    ]

    

# Delete 
def test_delete_skill_1():
    """Happy path
    """
    test_setup = client.post(
        "/skills/create",
        json = {
            "Skill_ID": "S88",
            "Skill_Name": "Test Skill 88 Updated",
            "Active": 1
        }
    )

    response = client.get("skills/delete/hard/S88")
    assert response.status_code == 200
    assert response.json() == {}

def test_delete_skill_2():
    """Error: Skill ID does not exist
    """
    response = client.get("skills/delete/hard/S99")
    assert response.status_code == 200
    assert response.json() == {
        "errors": [
                {
                    "Error_ID": "S1",
                    "Error_Desc": "The skill you're looking for is not inside our database. Check your search terms and try again.",
                    "Error_Details": ""
                }
            ]
        }

def test_delete_skill_3():
    """Valid Skill ID: First Letter Lowercase S
    """
    test_setup = client.post(
        "/skills/create",
        json = {
            "Skill_ID": "S88",
            "Skill_Name": "Test Skill 88 Updated",
            "Active": 1
        }
    )

    test_setup = client.post(
        "/skills/create",
        json = {
            "Skill_ID": "S88",
            "Skill_Name": "Test Skill 88",
            "Active": 1
        }
    )
    response = client.get("skills/delete/hard/s88")
    assert response.status_code == 200
    assert response.json() == {}

def test_delete_skill_4():
    """Error: Invalid Skill ID - First Letter Not S
    """
    response = client.get("skills/delete/hard/C11")
    assert response.status_code == 200
    assert response.json() == {
        "errors": [
            {
                "Error_ID": "S1",
                "Error_Desc": "The skill you're looking for is not inside our database. Check your search terms and try again.",
                "Error_Details": ""
            },
            {
                "Error_ID": "S3",
                "Error_Desc": "This skill has an invalid skill ID. Check your skill ID and try again.",
                "Error_Details": ""
            }
        ]
    }


def test_delete_skill_5():
    """Error: Valid Skill ID: Identifying section not numbers
    """
    response = client.get("skills/delete/hard/STU")
    assert response.status_code == 200
    assert response.json() == {
        "errors": [
            {
                "Error_ID": "S1",
                "Error_Desc": "The skill you're looking for is not inside our database. Check your search terms and try again.",
                "Error_Details": ""
            },
            {
                "Error_ID": "S3",
                "Error_Desc": "This skill has an invalid skill ID. Check your skill ID and try again.",
                "Error_Details": ""
            }
        ]
    }



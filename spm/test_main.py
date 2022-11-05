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

def testcreatejobrole():
    response = client.post(
        "/job_role/create_job_role",
        json={
            "Job_Role_ID": "JR111",
            "Job_Role_Name": "string",
            "Job_Department": "string"
            })
    assert response.status_code == 200
    assert response.json() == [
            {
                "Job_Role_ID": "JR111",
                "Job_Role_Name": "string",
                "Job_Department": "string"
            }
            ]

# Skills 

# Create 
def test_create_skill_1():
    """Happy Path
    """
    response = client.post(
        "/skills/create",
        json = {
            "Skill_ID": "S88",
            "Skill_Name": "Test Skill 88"
        }
    )
    assert response.status_code == 200
    assert response.json() == [
        {
            "Skill_ID": "S88",
            "Skill_Name": "Test Skill 88"
        }
    ]

    # Delete test 

def test_create_skill_2():
    """Error: Skill ID already exists
    """
    response = client.post(
        "/skills/create",
        json = {
            "Skill_ID": "S11",
            "Skill_Name": "Data analysis"
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
            "Skill_Name": "Test Skill 88"
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
    response = client.post(
        "/skills/create",
        json = {
            "Skill_ID": "s88",
            "Skill_Name": "Test Skill 88"
        }
    )
    assert response.status_code == 200
    assert response.json() == [
        {
            "Skill_ID": "S88",
            "Skill_Name": "Test Skill 88"
        }
    ]

    # Delete test

def test_create_skill_5():
    """Error: Invalid Skill ID - Following characters not numbers 
    """
    response = client.post(
        "/skills/create",
        json = {
            "Skill_ID": "STU",
            "Skill_Name": "Test Skill TU"
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



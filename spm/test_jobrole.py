from fastapi import FastAPI
from fastapi.testclient import TestClient
from app import app

client = TestClient(app)

def test_create_jobrole_1():
    """Happy Path
    """
    test_setup = client.get("/jobroles/delete/hard/JR88")
    response = client.post("/jobroles/create",
        json = {
            "Job_Role_ID": "JR88",
            "Job_Role_Name": "Test Job Role 88",
            "Job_Department": "Chairman",
            "Active": 1
        }
    )
    assert response.status_code == 200
    assert response.json() == [
        {
            "Job_Role_ID": "JR88",
            "Job_Role_Name": "Test Job Role 88",
            "Job_Department": "Chairman",
            "Active": 1
        }
    ]

def test_create_jobrole_2():
    """Error: Job Role ID already exists
    """
    response = client.post(
        "/jobroles/create",
        json = {
            "Job_Role_ID": "JR2",
            "Job_Role_Name": "Performance management",
            "Job_Department": "HR",
            "Active": 1
        }
    )
    assert response.status_code == 200
    assert response.json() == {
        "errors": [
            {
                "Error_ID": "JR2",
                "Error_Desc": "This job role is already within our database. Check your job role details and try again.",
                "Error_Details": ""
            }
        ]
    }

def test_create_skill_3():
    """Error: Invalid Skill ID - First Letters Not JR
    """
    response = client.post(
        "/jobroles/create",
        json = {
            "Job_Role_ID": "JK88",
            "Job_Role_Name": "Test Job Role 88",
            "Job_Department": "Chairman",
            "Active": 1
        }
    )
    assert response.status_code == 200
    assert response.json() == {
        "errors": [
            {
                "Error_ID": "JR3",
                "Error_Desc": "This job role has an invalid job role ID. Check your job role ID and try again.",
                "Error_Details": ""
            }
        ]
    }

def test_create_skill_4():
    """Error: Invalid Skill ID - Following characters not numbers 
    """
    response = client.post(
        "/jobroles/create",
        json = {
            "Job_Role_ID": "JKLM",
            "Job_Role_Name": "Test Job Role LM",
            "Job_Department": "Chairman",
            "Active": 1
        }
    )
    assert response.status_code == 200
    assert response.json() == {
        "errors": [
            {
                "Error_ID": "JR3",
                "Error_Desc": "This job role has an invalid job role ID. Check your job role ID and try again.",
                "Error_Details": ""
            }
        ]
    }

def test_create_jobrole_5():
    """Valid Job Role ID: Capitalised letters
    """
    test_setup = client.get("/jobroles/delete/hard/JR88")
    response = client.post("/jobroles/create",
        json = {
            "Job_Role_ID": "Jr88",
            "Job_Role_Name": "Test Job Role 88",
            "Job_Department": "Chairman",
            "Active": 1
        }
    )
    assert response.status_code == 200
    assert response.json() == [
        {
            "Job_Role_ID": "JR88",
            "Job_Role_Name": "Test Job Role 88",
            "Job_Department": "Chairman",
            "Active": 1
        }
    ]


def test_create_jobrole_6():
    """Valid Job Role ID: Lowercase letters
    """
    test_setup = client.get("/jobroles/delete/hard/JR88")
    response = client.post("/jobroles/create",
        json = {
            "Job_Role_ID": "jr88",
            "Job_Role_Name": "Test Job Role 88",
            "Job_Department": "Chairman",
            "Active": 1
        }
    )
    assert response.status_code == 200
    assert response.json() == [
        {
            "Job_Role_ID": "JR88",
            "Job_Role_Name": "Test Job Role 88",
            "Job_Department": "Chairman",
            "Active": 1
        }
    ]

def test_create_jobrole_7():
    """Error: Invalid Job role Name - Empty name
    """
    test_setup = client.get("/jobroles/delete/hard/JR88")
    response = client.post("/jobroles/create",
        json = {
            "Job_Role_ID": "JR88",
            "Job_Role_Name": "",
            "Job_Department": "Chairman",
            "Active": 1
        }
    )
    assert response.status_code == 200
    assert response.json() == {
        "errors": [
            {
                "Error_ID": "JR4",
                "Error_Desc": "This job role does not have a job role name. Check your job role name and try again.",
                "Error_Details": ""
            }
        ]
    }


def test_create_jobrole_8():
    """Error: Invalid Job role Name - More than 50 characters
    """
    test_setup = client.get("/jobroles/delete/hard/JR88")
    response = client.post("/jobroles/create",
        json = {
            "Job_Role_ID": "JR88",
            "Job_Role_Name": "Test Job Role 88 Test Job Role 88 Test Job Role 88 Test Job Role 88 Test Job Role 88 Test Job Role 88Test Job Role 88 Test Job Role 88",
            "Job_Department": "Chairman",
            "Active": 1
        }
    )
    assert response.status_code == 200
    assert response.json() == {
        "errors": [
            {
                "Error_ID": "JR5",
                'Error_Desc': '''This job role name is too long (more than 50 characters). Check your job role name and try again.''',
                "Error_Details": ""
            }
        ]
    }

def test_create_jobrole_9():
    """Error: Invalid Job role Department - Empty department
    """
    test_setup = client.get("/jobroles/delete/hard/JR88")
    response = client.post("/jobroles/create",
        json = {
            "Job_Role_ID": "JR88",
            "Job_Role_Name": "Test Job Role 88",
            "Job_Department": "",
            "Active": 1
        }
    )
    assert response.status_code == 200
    assert response.json() == {
        "errors": [
            {
                "Error_ID": "JR6",
                "Error_Desc": '''This job department is not valid (Chairman, CEO, Sales, Ops, HR, Finance). Check your job department and try again.''',
                "Error_Details": ""
            }
        ]
    }

def test_create_jobrole_10():
    """Error: Invalid Job role Department - More than 50 characters
    """
    test_setup = client.get("/jobroles/delete/hard/JR88")
    response = client.post("/jobroles/create",
        json = {
            "Job_Role_ID": "JR88",
            "Job_Role_Name": "Test Job Role 88",
            "Job_Department": "Chairman Chairman Chairman Chairman Chairman Chairman Chairman Chairman Chairman",
            "Active": 1
        }
    )
    assert response.status_code == 200
    assert response.json() == {
        "errors": [
            {
                "Error_ID": "JR6",
                "Error_Desc": "This job department is not valid (Chairman, CEO, Sales, Ops, HR, Finance). Check your job department and try again.",
                "Error_Details": ""
            }
        ]
    }


def test_create_jobrole_11():
    """Error: Invalid Job role Department - Not a matching (sub)string
    """
    test_setup = client.get("/jobroles/delete/hard/JR88")
    response = client.post("/jobroles/create",
        json = {
            "Job_Role_ID": "JR88",
            "Job_Role_Name": "Test Job Role 88",
            "Job_Department": "SPM",
            "Active": 1
        }
    )
    assert response.status_code == 200
    assert response.json() == {
        "errors": [
            {
                "Error_ID": "JR6",
                "Error_Desc": "This job department is not valid (Chairman, CEO, Sales, Ops, HR, Finance). Check your job department and try again.",
                "Error_Details": ""
            }
        ]
    }

# Read 

def test_read_jobrole_ID_1():
    """Happy Path: Read active job role by job role ID
    """
    response = client.get("/jobroles/read/id/JR2")
    assert response.status_code == 200
    assert response.json() == [
        {
            "Job_Role_ID": "JR2",
            "Job_Role_Name": "Performance management",
            "Job_Department": "HR",
            "Active": 1
        }
    ]

def test_read_jobrole_ID_2():
    """Valid Path: Read inactive job role by job role ID
    """
    response = client.get("/jobroles/read/id/JR1")
    assert response.status_code == 200
    assert response.json() == [
        {
            "Job_Role_ID": "JR1",
            "Job_Role_Name": "Employee conflict management",
            "Job_Department": "HR",
            "Active": 0
        }
    ]

def test_read_jobrole_ID_3():
    """Error: Job Role ID does not exist
    """
    response = client.get("/jobroles/read/id/JR99")
    assert response.status_code == 200
    assert response.json() == {
        "errors": [
            {
                "Error_ID": "JR1",
                "Error_Desc": "The job role you're looking for is not inside our database. Check your search terms and try again.",
                "Error_Details": ""
            }
        ]
    }

def test_read_jobrole_ID_4():
    """Error: Invalid Job role ID - First Letters Not JR
    """
    response = client.get("/jobroles/read/id/JK99")
    assert response.status_code == 200
    assert response.json() == {
        "errors": [
            {
                "Error_ID": "JR1",
                "Error_Desc": "The job role you're looking for is not inside our database. Check your search terms and try again.",
                "Error_Details": ""
            },
            {
                "Error_ID": "JR3",
                "Error_Desc": "This job role has an invalid job role ID. Check your job role ID and try again.",
                "Error_Details": ""
            }
        ]
    }

def test_read_jobrole_ID_5():
    """Error: Invalid Job role ID - Following characters not numbers 
    """
    response = client.get("/jobroles/read/id/JKLM")
    assert response.status_code == 200
    assert response.json() == {
        "errors": [
            {
                "Error_ID": "JR1",
                "Error_Desc": "The job role you're looking for is not inside our database. Check your search terms and try again.",
                "Error_Details": ""
            },
            {
                "Error_ID": "JR3",
                "Error_Desc": "This job role has an invalid job role ID. Check your job role ID and try again.",
                "Error_Details": ""
            }
        ]
    }

def test_read_jobrole_ID_6():
    """Valid Job Role ID: Capitalised letters
    """
    response = client.get("/jobroles/read/id/Jr2")
    assert response.status_code == 200
    assert response.json() == [
        {
            "Job_Role_ID": "JR2",
            "Job_Role_Name": "Performance management",
            "Job_Department": "HR",
            "Active": 1
        }
    ]

def test_read_jobrole_ID_7():
    """Valid Job Role ID: Lowercase letters
    """
    response = client.get("/jobroles/read/id/jr2")
    assert response.status_code == 200
    assert response.json() == [
        {
            "Job_Role_ID": "JR2",
            "Job_Role_Name": "Performance management",
            "Job_Department": "HR",
            "Active": 1
        }
    ]

def test_read_jobrole_name_1():
    """Happy Path: Read active job role by exact match job role name
    """
    response = client.get("/jobroles/read/name/Performance management")
    assert response.status_code == 200
    assert response.json() == [
        {
            "Job_Role_ID": "JR2",
            "Job_Role_Name": "Performance management",
            "Job_Department": "HR",
            "Active": 1
        }
    ]

def test_read_jobrole_name_2():
    """Valid Path: Read inactive job role by exact match job role name
    """
    response = client.get("/jobroles/read/name/Employee conflict management")
    assert response.status_code == 200
    assert response.json() == [
        {
            "Job_Role_ID": "JR1",
            "Job_Role_Name": "Employee conflict management",
            "Job_Department": "HR",
            "Active": 0
        }
    ]

def test_read_jobrole_name_3():
    """Valid Path: Read active job role by substring match job role with a single match
    """
    response = client.get("/jobroles/read/name/product")
    assert response.status_code == 200
    assert response.json() == [
    {
        "Job_Role_ID": "JR4",
        "Job_Role_Name": "Product handling",
        "Job_Department": "Sales",
        "Active": 0
    }
    ]

def test_read_jobrole_name_4():
    """Valid Path: Read active job role by substring match job role with multiple matches
    """
    response = client.get("/jobroles/read/name/management")
    assert response.status_code == 200
    assert response.json() == [
        {
            "Job_Role_ID": "JR1",
            "Job_Role_Name": "Employee conflict management",
            "Job_Department": "HR",
            "Active": 0
        },
        {
            "Job_Role_ID": "JR2",
            "Job_Role_Name": "Performance management",
            "Job_Department": "HR",
            "Active": 1
        },
        {
            "Job_Role_ID": "JR6",
            "Job_Role_Name": "Customer compliant management",
            "Job_Department": "Sales",
            "Active": 1
        },
        {
            "Job_Role_ID": "JR12",
            "Job_Role_Name": "Cash flow management",
            "Job_Department": "Finance",
            "Active": 0
        }
    ]

def test_read_jobrole_name_5():
    """Error: Substring not found in any job role
    """
    response = client.get("/jobroles/read/name/spm")
    assert response.status_code == 200
    assert response.json() == []


def test_read_jobrole_name_6():
    """Valid Path: Read active job role by exact match job role name in uppercase
    """
    response = client.get("/jobroles/read/name/PERFORMANCE MANAGEMENT")
    assert response.status_code == 200
    assert response.json() == [
        {
            "Job_Role_ID": "JR2",
            "Job_Role_Name": "Performance management",
            "Job_Department": "HR",
            "Active": 1
        }
    ]

def test_read_jobrole_name_7():
    """Valid Path: Read active job role by exact match job role name capitalised
    """
    response = client.get("/jobroles/read/name/Performance Management")
    assert response.status_code == 200
    assert response.json() == [
        {
            "Job_Role_ID": "JR2",
            "Job_Role_Name": "Performance management",
            "Job_Department": "HR",
            "Active": 1
        }
    ]


def test_read_jobrole_dept_1():
    """Valid Path: Read job roles by exact match job role department for a single job role
    """
    response = client.get("/jobroles/read/dept/Chairman")
    assert response.status_code == 200
    assert response.json() == [
        {
            "Job_Role_ID": "JR3",
            "Job_Role_Name": "Board representative",
            "Job_Department": "Chairman",
            "Active": 0
        }
    ]

def test_read_jobrole_dept_2():
    """Happy Path: Read job roles by exact match job role department for multiple job roles
    """
    response = client.get("/jobroles/read/dept/HR")
    assert response.status_code == 200
    assert response.json() == [
        {
            "Job_Role_ID": "JR1",
            "Job_Role_Name": "Employee conflict management",
            "Job_Department": "HR",
            "Active": 0
        },
        {
            "Job_Role_ID": "JR2",
            "Job_Role_Name": "Performance management",
            "Job_Department": "HR",
            "Active": 1
        }
    ]


def test_read_jobrole_dept_3():
    """Valid Path: Read active job role by substring match job role with a single match
    """
    response = client.get("/jobroles/read/dept/chair")
    assert response.status_code == 200
    assert response.json() == [
        {
            "Job_Role_ID": "JR3",
            "Job_Role_Name": "Board representative",
            "Job_Department": "Chairman",
            "Active": 0
        }
    ]

def test_read_jobrole_dept_4():
    """Valid Path: Read active job role by substring match job role with multiple matches
    """
    response = client.get("/jobroles/read/dept/op")
    assert response.status_code == 200
    assert response.json() == [
        {
            "Job_Role_ID": "JR9",
            "Job_Role_Name": "Learning System Administrator",
            "Job_Department": "Ops",
            "Active": 0
        },
        {
            "Job_Role_ID": "JR10",
            "Job_Role_Name": "Business Process Development",
            "Job_Department": "Ops",
            "Active": 1
        },
        {
            "Job_Role_ID": "JR11",
            "Job_Role_Name": "Market Research",
            "Job_Department": "Ops",
            "Active": 0
        }
    ]

def test_read_jobrole_dept_5():
    """Error: Substring not found in any job role
    """
    response = client.get("/jobroles/read/dept/spm")
    assert response.status_code == 200
    assert response.json() == {
        "errors": [
            {
                "Error_ID": "JR6",
                "Error_Desc": "This job department is not valid (Chairman, CEO, Sales, Ops, HR, Finance). Check your job department and try again.",
                "Error_Details": ""
            }
        ]
    }

def test_read_jobrole_dept_6():
    """Valid Path: Read active job role by exact match job role name in uppercase
    """
    response = client.get("/jobroles/read/dept/OPS")
    assert response.status_code == 200
    assert response.json() == [
        {
            "Job_Role_ID": "JR9",
            "Job_Role_Name": "Learning System Administrator",
            "Job_Department": "Ops",
            "Active": 0
        },
        {
            "Job_Role_ID": "JR10",
            "Job_Role_Name": "Business Process Development",
            "Job_Department": "Ops",
            "Active": 1
        },
        {
            "Job_Role_ID": "JR11",
            "Job_Role_Name": "Market Research",
            "Job_Department": "Ops",
            "Active": 0
        }
    ]

def test_read_jobrole_dept_7():
    """Valid Path: Read active job role by exact match job role name capitalised
    """
    response = client.get("/jobroles/read/dept/Ceo")
    assert response.status_code == 200
    assert response.json() == [
        {
            "Job_Role_ID": "JR7",
            "Job_Role_Name": "Capital allocation",
            "Job_Department": "CEO",
            "Active": 1
        },
        {
            "Job_Role_ID": "JR8",
            "Job_Role_Name": "Organizational strategy",
            "Job_Department": "CEO",
            "Active": 1
        }
    ]

# Update 
def test_update_jobrole_1():
    """Happy Path: update job role name
    """
    test_setup_0 = client.get("/jobroles/delete/hard/JR88")
    test_setup_1 = client.post(
        "/jobroles/create",
        json = {
            "Job_Role_ID": "JR88",
            "Job_Role_Name": "Test Skill 88",
            "Job_Department": "Chairman",
            "Active": 1
        }
    )
    response = client.post(
        "/jobroles/update",
        json = {
            "Job_Role_ID": "JR88",
            "Job_Role_Name": "Test Job Role 88 Updated",
            "Job_Department": "Chairman",
            "Active": 1
        }
    )
    assert response.status_code == 200
    assert response.json() == [
        {
            "Job_Role_ID": "JR88",
            "Job_Role_Name": "Test Job Role 88 Updated",
            "Job_Department": "Chairman",
            "Active": 1
        }
    ]

def test_update_jobrole_2():
    """Happy Path: update job role department
    """
    test_setup_0 = client.get("/jobroles/delete/hard/JR88")
    test_setup_1 = client.post(
        "/jobroles/create",
        json = {
            "Job_Role_ID": "JR88",
            "Job_Role_Name": "Test Job Role 88",
            "Job_Department": "Chairman",
            "Active": 1
        }
    )
    response = client.post(
        "/jobroles/update",
        json = {
            "Job_Role_ID": "JR88",
            "Job_Role_Name": "Test Job Role 88",
            "Job_Department": "CEO",
            "Active": 1
        }
    )
    assert response.status_code == 200
    assert response.json() == [
        {
            "Job_Role_ID": "JR88",
            "Job_Role_Name": "Test Job Role 88",
            "Job_Department": "CEO",
            "Active": 1
        }
    ]

def test_update_jobrole_3():
    """Error: Empty job role name
    """
    test_setup_0 = client.get("/jobroles/delete/hard/JR88")
    test_setup_1 = client.post(
        "/jobroles/create",
        json = {
            "Job_Role_ID": "JR88",
            "Job_Role_Name": "Test Job Role 88",
            "Job_Department": "Chairman",
            "Active": 1
        }
    )
    response = client.post(
        "/jobroles/update",
        json = {
            "Job_Role_ID": "JR88",
            "Job_Role_Name": "",
            "Job_Department": "Chairman",
            "Active": 1
        }
    )
    assert response.status_code == 200
    assert response.json() == {
        "errors": [
            {
                "Error_ID": "JR4",
                "Error_Desc": "This job role does not have a job role name. Check your job role name and try again.",
                "Error_Details": ""
            }
        ]
    }

def test_update_jobrole_4():
    """Error: Job role name > 50 Characters
    """
    test_setup_0 = client.get("/jobroles/delete/hard/JR88")
    test_setup_1 = client.post(
        "/jobroles/create",
        json = {
            "Job_Role_ID": "JR88",
            "Job_Role_Name": "Test Job Role 88",
            "Job_Department": "Chairman",
            "Active": 1
        }
    )
    response = client.post(
        "/jobroles/update",
        json = {
            "Job_Role_ID": "JR88",
            "Job_Role_Name": "Test Job Role 88 Updated Updated Updated Updated Updated Updated Updated Updated Updated",
            "Job_Department": "Chairman",
            "Active": 1
        }
    )
    assert response.status_code == 200
    assert response.json() == {
        "errors": [
            {
                "Error_ID": "JR5",
                "Error_Desc": "This job role name is too long (more than 50 characters). Check your job role name and try again.",
                "Error_Details": ""
            }
        ]
    }

def test_update_jobrole_5():
    """Error: Empty job role department
    """
    test_setup_0 = client.get("/jobroles/delete/hard/JR88")
    test_setup_1 = client.post(
        "/jobroles/create",
        json = {
            "Job_Role_ID": "JR88",
            "Job_Role_Name": "Test Job Role 88",
            "Job_Department": "Chairman",
            "Active": 1
        }
    )
    response = client.post(
        "/jobroles/update",
        json = {
            "Job_Role_ID": "JR88",
            "Job_Role_Name": "Test Job Role 88",
            "Job_Department": "",
            "Active": 1
        }
    )
    assert response.status_code == 200
    assert response.json() == {
        "errors": [
            {
                'Error_ID': 'JR6', 
                'Error_Desc': '''This job department is not valid (Chairman, CEO, Sales, Ops, HR, Finance). Check your job department and try again.''',
                'Error_Details': ''
            }
        ]
    }

def test_update_jobrole_6():
    """Error: Job role department > 50 Characters
    """
    test_setup_0 = client.get("/jobroles/delete/hard/JR88")
    test_setup_1 = client.post(
        "/jobroles/create",
        json = {
            "Job_Role_ID": "JR88",
            "Job_Role_Name": "Test Job Role 88",
            "Job_Department": "Chairman",
            "Active": 1
        }
    )
    response = client.post(
        "/jobroles/update",
        json = {
            "Job_Role_ID": "JR88",
            "Job_Role_Name": "Test Job Role 88 Updated",
            "Job_Department": "Chairman Chairman Chairman Chairman Chairman Chairman Chairman Chairman Chairman Chairman Chairman Chairman Chairman",
            "Active": 1
        }
    )
    assert response.status_code == 200
    assert response.json() == {
        "errors": [
            {
                'Error_ID': 'JR6', 
                'Error_Desc': '''This job department is not valid (Chairman, CEO, Sales, Ops, HR, Finance). Check your job department and try again.''',
                'Error_Details': ''
            }
        ]
    }

def test_update_jobrole_7():
    """Error: Job role department not within existing departments
    """
    test_setup_0 = client.get("/jobroles/delete/hard/JR88")
    test_setup_1 = client.post(
        "/jobroles/create",
        json = {
            "Job_Role_ID": "JR88",
            "Job_Role_Name": "Test Job Role 88",
            "Job_Department": "Chairman",
            "Active": 1
        }
    )
    response = client.post(
        "/jobroles/update",
        json = {
            "Job_Role_ID": "JR88",
            "Job_Role_Name": "Test Job Role 88 Updated",
            "Job_Department": "spm",
            "Active": 1
        }
    )
    assert response.status_code == 200
    assert response.json() == {
        "errors": [
            {
                'Error_ID': 'JR6', 
                'Error_Desc': '''This job department is not valid (Chairman, CEO, Sales, Ops, HR, Finance). Check your job department and try again.''',
                'Error_Details': ''
            }
        ]
    }


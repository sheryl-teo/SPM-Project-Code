from fastapi import FastAPI
from fastapi.testclient import TestClient
from app import app

client = TestClient(app)

# Read 

def test_read_course_ID_1():
    """Happy Path: Read course by course ID
    """
    response = client.get("/courses/get_course_by_id/COR001")
    assert response.status_code == 200
    assert response.json() == [
        {
            "Course_ID": "COR001",
            "Course_Name": "Systems Thinking and Design",
            "Course_Desc": "This foundation module aims to introduce students to the fundamental concepts and underlying principles of systems thinking,",
            "Course_Status": "Retired",
            "Course_Type": "Internal",
            "Course_Category": "Core"
        }
    ]

def test_read_course_ID_2():
    """Valid Path: Course does not exist
    """
    response = client.get("/courses/get_course_by_id/COR000")
    assert response.status_code == 200
    assert response.json() == [
    ]

def test_read_course_ID_3():
    """Error: Course prefix is not valid
    """
    response = client.get("/courses/get_course_by_id/ABC001")
    assert response.status_code == 200
    assert response.json() == [
    ]

def test_read_course_ID_4():
    """Error: Course number is not valid
    """
    response = client.get("/courses/get_course_by_id/COR000")
    assert response.status_code == 200
    assert response.json() == [
    ]
def test_read_course_ID_5(): 
    """Valid Path: Lowercase 
    """
    response = client.get("/courses/get_course_by_id/cor001")
    assert response.status_code == 200
    assert response.json() == [
        {
            "Course_ID": "COR001",
            "Course_Name": "Systems Thinking and Design",
            "Course_Desc": "This foundation module aims to introduce students to the fundamental concepts and underlying principles of systems thinking,",
            "Course_Status": "Retired",
            "Course_Type": "Internal",
            "Course_Category": "Core"
        }
    ]

def test_read_course_ID_6(): 
    """Valid Path: Camelcase
    """
    response = client.get("/courses/get_course_by_id/Cor001")
    assert response.status_code == 200
    assert response.json() == [
        {
            "Course_ID": "COR001",
            "Course_Name": "Systems Thinking and Design",
            "Course_Desc": "This foundation module aims to introduce students to the fundamental concepts and underlying principles of systems thinking,",
            "Course_Status": "Retired",
            "Course_Type": "Internal",
            "Course_Category": "Core"
        }
    ]

def test_read_course_name_1():
    """Happy Path: Read course by full course name
    """
    response = client.get("/courses/get_course_by_name/Systems Thinking and Design")
    assert response.status_code == 200
    assert response.json() == [
        {
            "Course_ID": "COR001",
            "Course_Name": "Systems Thinking and Design",
            "Course_Desc": "This foundation module aims to introduce students to the fundamental concepts and underlying principles of systems thinking,",
            "Course_Status": "Retired",
            "Course_Type": "Internal",
            "Course_Category": "Core"
        }
    ]

def test_read_course_name_2():
    """Valid Path: Read course by partial course name
    """
    response = client.get("/courses/get_course_by_name/Systems Thinking and")
    assert response.status_code == 200
    assert response.json() == [
        {
            "Course_ID": "COR001",
            "Course_Name": "Systems Thinking and Design",
            "Course_Desc": "This foundation module aims to introduce students to the fundamental concepts and underlying principles of systems thinking,",
            "Course_Status": "Retired",
            "Course_Type": "Internal",
            "Course_Category": "Core"
        }
    ]

def test_read_course_name_3():
    """Valid Path: Read courses by partial course name
    """
    response = client.get("/courses/get_course_by_name/Management")
    assert response.status_code == 200
    assert response.json() == [
        {
            "Course_ID": "MGT001",
            "Course_Name": "People Management",
            "Course_Desc": "enable learners to manage team performance and development through effective communication, conflict resolution and negotiation skills.",
            "Course_Status": "Active",
            "Course_Type": "Internal",
            "Course_Category": "Management"
        },
        {
            "Course_ID": "MGT002",
            "Course_Name": "Workplace Conflict Management for Professionals",
            "Course_Desc": "This course will address the gaps to build consensus and utilise knowledge of conflict management techniques to diffuse tensions and achieve resolutions effectively in the best interests of the organisation.",
            "Course_Status": "Active",
            "Course_Type": "External",
            "Course_Category": "Management"
        },
        {
            "Course_ID": "MGT007",
            "Course_Name": "Supervisory Management Skills",
            "Course_Desc": "Supervisors lead teams, manage tasks, solve problems, report up and down the hierarchy, and much more. ",
            "Course_Status": "Retired",
            "Course_Type": "External",
            "Course_Category": "Management"
        },
        {
            "Course_ID": "SAL001",
            "Course_Name": "Risk Management for Smart Business",
            "Course_Desc": "Apply risk management concepts to digital business",
            "Course_Status": "Retired",
            "Course_Type": "Internal",
            "Course_Category": "Sales"
        },
        {
            "Course_ID": "SAL004",
            "Course_Name": "Stakeholder Management",
            "Course_Desc": "Develop a stakeholder engagement plan and negotiate with stakeholders to arrive at mutually-beneficial arrangements.",
            "Course_Status": "Active",
            "Course_Type": "Internal",
            "Course_Category": "Sales"
        },
        {
            "Course_ID": "tch018",
            "Course_Name": "Professional Project Management",
            "Course_Desc": "solid foundation in the project management processes from initiating a project, through planning, execution, control,",
            "Course_Status": "Active",
            "Course_Type": "Internal",
            "Course_Category": "Technical"
        },
        {
            "Course_ID": "tch019",
            "Course_Name": "Innovation and Change Management",
            "Course_Desc": "the organization that constantly reinvents itself to be relevant has a better chance of making progress",
            "Course_Status": "Active",
            "Course_Type": "External",
            "Course_Category": "Technical"
        }
    ]

def test_read_course_name_4():
    """Valid Path: Course name substring does not exist
    """
    response = client.get("/courses/get_course_by_name/spm")
    assert response.status_code == 200
    assert response.json() == [
    ]

def test_read_course_name_5():
    """Valid Path: Lower case
    """
    response = client.get("/courses/get_course_by_name/systems thinking and design")
    assert response.status_code == 200
    assert response.json() == [
        {
            "Course_ID": "COR001",
            "Course_Name": "Systems Thinking and Design",
            "Course_Desc": "This foundation module aims to introduce students to the fundamental concepts and underlying principles of systems thinking,",
            "Course_Status": "Retired",
            "Course_Type": "Internal",
            "Course_Category": "Core"
        }
    ]

def test_read_course_name_6():
    """Valid Path: Capitalised
    """
    response = client.get("/courses/get_course_by_name/Systems thinking and design")
    assert response.status_code == 200
    assert response.json() == [
        {
            "Course_ID": "COR001",
            "Course_Name": "Systems Thinking and Design",
            "Course_Desc": "This foundation module aims to introduce students to the fundamental concepts and underlying principles of systems thinking,",
            "Course_Status": "Retired",
            "Course_Type": "Internal",
            "Course_Category": "Core"
        }
    ]

def test_read_course_name_7():
    """Valid Path: Capitalised
    """
    response = client.get("/courses/get_course_by_name/SYSTEMS THINKING AND DESIGN")
    assert response.status_code == 200
    assert response.json() == [
        {
            "Course_ID": "COR001",
            "Course_Name": "Systems Thinking and Design",
            "Course_Desc": "This foundation module aims to introduce students to the fundamental concepts and underlying principles of systems thinking,",
            "Course_Status": "Retired",
            "Course_Type": "Internal",
            "Course_Category": "Core"
        }
    ]
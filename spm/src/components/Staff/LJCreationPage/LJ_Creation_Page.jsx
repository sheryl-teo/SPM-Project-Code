

import "./LJ_Creation_Page.css"
import React, { useEffect, useState } from "react";
import { browserHistory } from 'react-router';

var roleSelected = ''
var skillSelected = ''
var courseSelected = ''

//remove present options for skill list
function removeOptions(selectElement) {
  var i, L = selectElement.options.length - 1;
  for (i = L; i >= 0; i--) {
    selectElement.remove(i);
  }
}

// form creation
const LJCreationPage = () => {

  // fetchroles
  const [Roles, setRoles] = useState([])
  const fetchRoles = async () => {
    try {
      const response = await fetch("http://127.0.0.1:8000/job_roles/get_job_roles")
      const Roles = await response.json()
      const RoleList = []
      Roles.map((Roles) => {
        RoleList.push([Roles.Job_Role_Name, Roles.Job_Role_ID])
      })
      setRoles(RoleList)
    } catch (e) {
      console.log('error:' + e)
    }

  }
  useEffect(() => {
    fetchRoles()
  }, [])

  // skillID
  const [SkillsID, setSkillsID] = useState([])

  const fetchSkillsID = async () => {
    const response = await fetch("http://127.0.0.1:8000/job_role_skill/get_job_role_skill/")
    const SkillsID = await response.json()
    const SkillsIDList = []
    SkillsID.map((SkillsID) => {
      SkillsIDList.push([SkillsID.Job_Role_ID, SkillsID.Skill_ID])
    })
    setSkillsID(SkillsIDList)
  }
  useEffect(() => {
    fetchSkillsID()
  }, [])

  // skill Name
  const [Skills, setSkills] = useState([])


  const fetchSkills = async () => {
    const response = await fetch("http://127.0.0.1:8000/skills")
    const Skills = await response.json()
    const SkillList = []
    Skills.map((Skills) => {
      SkillList.push([Skills.Skill_ID, Skills.Skill_Ndisplayame])
    })
    setSkills(SkillList)
  }
  useEffect(() => {
    fetchSkills()
  }, [])

  // Course Name
  const [Courses, setCourses] = useState([])
  const fetchCourses = async () => {
    const response = await fetch('http://127.0.0.1:8000/courses/get_all_courses')
    const Courses = await response.json()
    const CoursesList = []
    Courses.map((Courses) => {
      CoursesList.push([Courses.Course_Name, Courses.Course_ID])
    })
    setCourses(CoursesList)
  }
  useEffect(() => {
    fetchCourses()
  }, [])


  // fetch skill course
  const [skillCourses, setSkillCourses] = useState([])
  const fetchSkillCourses = async () => {
    const response = await fetch('http://127.0.0.1:8000/skill_courses')
    const skillCourses = await response.json()
    const skillCoursesList = []
    skillCourses.map((skillCourses) => {
      skillCoursesList.push([skillCourses.Course_ID, skillCourses.Skill_ID])
    })
    setSkillCourses(skillCoursesList)
  }
  useEffect(() => {
    fetchSkillCourses()
  }, [])

  console.log(skillCourses)

  // Display Roles
  var rolesArray = Roles

  var RolesList = document.getElementById('roles');
  for (var role in rolesArray) {
    var newoption = document.createElement("option");
    newoption.value = rolesArray[role][0]
    newoption.innerHTML = rolesArray[role][0]
    RolesList.options.add(newoption)
  }

  function displaySkills(jobPosition) {
    var skillList = document.getElementById('skills');
    var courseList = document.getElementById('courses');
    var job = jobPosition.target.value;
    roleSelected = job    //delete
    // console.log(roleSelected)
    var jobID = ''
    var starter = "Select Skill";
    var skillsneededID = [starter]
    for (var roleIndex in Roles) {
      if (job == Roles[roleIndex][0]) {
        jobID = Roles[roleIndex][1]
        roleSelected = jobID
      }
    }

    for (var skillIndex in SkillsID) {
      if (jobID == SkillsID[skillIndex][0]) {
        skillsneededID.push(SkillsID[skillIndex][1])
      }
    }

    if (skillList.options.length != 0) {
      removeOptions(skillList);
    }

    //adding options for skill-list
    for (var skill in skillsneededID) {
      var newoption = document.createElement("option");
      newoption.value = skillsneededID[skill]
      newoption.innerHTML = skillsneededID[skill]
      skillList.options.add(newoption)
    }

    if (courseList.options.length != 0) {
      removeOptions(courseList);
    }
  };

  function pickCourse(event) {
    courseSelected= event.target.value
    // console.log(roleSelected,skillSelected,courseSelected)
   }
  //alternate skill droplist according to job role
  function displayCourses(event) {
    var CoursesArray = ["Select Course"]

    var CourseList = document.getElementById('courses');

    var skill = event.target.value; //job role selection dynamic value
    skillSelected = skill
    for (var skillcourseindex in skillCourses) {
      if (skill == skillCourses[skillcourseindex][1]) {
        var courseNeeded = skillCourses[skillcourseindex][0]
        CoursesArray.push(courseNeeded)

      }
    }
 

    //clear present options for skill-list to prevent replication + change dynamically according to skill selected
    if (CourseList.options.length != 0) {
      removeOptions(CourseList);
    }

    //adding options for skill-list
    
    for (var course in CoursesArray) {
      var newoption = document.createElement("option");
      newoption.value = CoursesArray[course]
      newoption.innerHTML = CoursesArray[course]
      CourseList.options.add(newoption)
    }

  };


  function handleSubmit(event) {

    var userID = 130001
    const newLJ = {
      "Learning_Journey_ID": "LJ1314",
      "Staff_ID": userID,
      "Job_Role_ID": roleSelected,
      "skill_list": [
        skillSelected
      ],
      "course_list": [
        courseSelected
      ]

    }
    // console.log(newCourses)
    fetch("http://127.0.0.1:8000/learning_journey/create_learning_journey",
      {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(newLJ)
      })




  };


  function poppin() {
    alert("Learning Journey Created!");
  }


  //html
  return (
    <div className='creation'>
      <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.1.0/css/bootstrap.min.css"
        integrity="sha384-9gVQ4dYFwwWSjIDZnLEWnxCjeSWFphJiwGPXr1jddIhOegiu1FwO5qRGvFXOdJZ4"
        crossorigin="anonymous"></link>




      <form onSubmit={handleSubmit}>
        <h1>Registration Form</h1>
        {/* <input type="text" name="username" placeholder="Email" />
        <input type="password" name="password" placeholder="Password" /> */}

        <p>
          <input type="text" className="id" name="id" class="formStyle" placeholder="Staff_ID (required)" required />
        </p>

        <p>
          <select className="jobSkills" name="job" data-size="4" onChange={displaySkills} id="roles" required>
          </select>
        </p>
        <p>
          <select className="jobSkills" name="skills" data-size="4" onChange={displayCourses} id="skills" required>
          </select>
        </p>
        <p>
          <select className="jobSkills" name='courses' data-size="4" id='courses'  onChange={pickCourse}>
          </select>
        </p>


        <button type="submit" class="btn btn-dark" onClick={poppin}>Submit</button>
      </form>
      <a href='/staff'>Return Home</a>




    </div>
  );
};

export default LJCreationPage;

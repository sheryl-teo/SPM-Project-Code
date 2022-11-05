
import React from 'react';
import "./LJ_Creation_Page.css"

//remove present options for skill list
function removeOptions(selectElement) {
  var i, L = selectElement.options.length - 1;
  for (i = L; i >= 0; i--) {
    selectElement.remove(i);
  }
}

//form creation
const LJCreationPage = () => {
  var coursesArray = []
  var skillsArray = []
  var courseList = document.getElementById('courses');
  var skillList = document.getElementById('skills');

  //alternate skill droplist according to job role
  function displayCourses(event) {
    
    var skill = event.target.value; //job role selection dynamic value

    //assigning diff job position diff skill-list
    var starter = "Select Course";
    var noCourse = "No Course Available";


    if (skill == "admin first skill") {
      coursesArray = [starter,'admin first course', 'admin second course', 'admin third course'];
    }
    else if (skill == 'manager first skill') {
      coursesArray = [starter,'manager first course', 'manager second course', 'manager third course']
    }
    else {
      coursesArray = [noCourse]
    }

    //clear present options for skill-list to prevent replication + change dynamically according to skill selected
    if (courseList.options.length != 0) {
      removeOptions(courseList);
    }

    //adding options for skill-list
    for (var course in coursesArray) {
      var newoption = document.createElement("option");
      newoption.value = coursesArray[course]
      newoption.innerHTML = coursesArray[course]
      courseList.options.add(newoption)
    }
  };


  function displaySkills(jobPosition) {
    console.log(" skills function working");
    var job = jobPosition.target.value; //job role selection dynamic value

    //assigning diff job position diff skill-list
    var starter = "Select Skill";
    var noSkill = "No Skill Available";

    if (job == "admin") {
      skillsArray = [starter,'admin first skill', 'admin second skill', 'admin third skill']
    }
    else if (job == 'manager') {
      skillsArray = [starter,'manager first skill', 'manager second skill', 'manager third skill']
    }
    else {
      skillsArray = [noSkill]
      
    }

    if (skillList.options.length != 0) {
      removeOptions(skillList);
    }

    //adding options for skill-list
    for (var skill in skillsArray) {
      var newoption = document.createElement("option");
      newoption.value = skillsArray[skill]
      newoption.innerHTML = skillsArray[skill]
      skillList.options.add(newoption)
    }
    
    if (courseList.options.length != 0) {
      removeOptions(courseList);
    }
  };

  //html
  return (
    <div className='creation'>
      <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.1.0/css/bootstrap.min.css"
        integrity="sha384-9gVQ4dYFwwWSjIDZnLEWnxCjeSWFphJiwGPXr1jddIhOegiu1FwO5qRGvFXOdJZ4"
        crossorigin="anonymous"></link>
      <form action="" method='post'>
        <h1>Registration Form</h1>
        <p>
          <input type="text" className="name" class="formStyle" placeholder="Name (required)" required />
        </p>
        <p>
          <input type="text" className="id" class="formStyle" placeholder="Staff_ID (required)" required />
        </p>
        <p>

        </p>
        <p>
          <select class="jobSkills" data-size="4" onChange={displaySkills} id="job" required>
            <option value="">Select Job Position</option>
            <option value="admin">Admin</option>
            <option value="manager">Manager</option>
          </select>
        </p>
        <p>
          <select class="jobSkills" data-size="4" onChange={displayCourses} id="skills" required>
          </select>
        </p>
        <p>
          <select class="jobSkills" data-size="4" id='courses'>
          </select>
        </p>
        <button type="submit" class="btn btn-light">Submit</button>
      </form>
    </div>
  );
};

export default LJCreationPage;
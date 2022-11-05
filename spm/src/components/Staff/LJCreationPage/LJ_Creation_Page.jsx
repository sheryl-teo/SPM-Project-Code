
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


  //alternate skill droplist according to job role
  function displayCourses(event) {
    var courseList = document.getElementById('courses');

    var skill = event.target.value; //job role selection dynamic value

    //assigning diff job position diff skill-list
    var starter = "Select Course";
    var noCourse = "No Course Available";


    if (skill == "admin first skill") {
      coursesArray = [starter, 'admin first course', 'admin second course', 'admin third course'];
    }
    else if (skill == 'manager first skill') {
      coursesArray = [starter, 'manager first course', 'manager second course', 'manager third course']
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
    var skillList = document.getElementById('skills');
    var courseList = document.getElementById('courses');

    console.log(" skills function working");
    var job = jobPosition.target.value; //job role selection dynamic value

    //assigning diff job position diff skill-list
    var starter = "Select Skill";
    var noSkill = "No Skill Available";

    if (job == "admin") {
      skillsArray = [starter, 'admin first skill', 'admin second skill', 'admin third skill']
    }
    else if (job == 'manager') {
      skillsArray = [starter, 'manager first skill', 'manager second skill', 'manager third skill']
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


  function handleSubmit(event) {
    
    const formData = new FormData(event.currentTarget);
    event.preventDefault();  // prevent page refresh
    for (let [key, value] of formData.entries()) {
      console.log(key, value); // push to backend
    };
  
  };

  function poppin() {
    alert("Learning Journey Created!");
    window.location.replace("/staff");
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
          <input type="text" className="name" name="name" class="formStyle" placeholder="Name (required)" required />
        </p>
        <p>
          <input type="text" className="id" name="id" class="formStyle" placeholder="Staff_ID (required)" required />
        </p>

        <p>
          <select className="jobSkills" name="job" data-size="4" onChange={displaySkills} id="job" required>
            <option value="">Select Job Position</option>
            <option value="admin">Admin</option>
            <option value="manager">Manager</option>
          </select>
        </p>
        <p>
          <select className="jobSkills" name="skills" data-size="4" onChange={displayCourses} id="skills" required>
          </select>
        </p>
        <p>
          <select className="jobSkills" name='courses' data-size="4" id='courses'>
          </select>
        </p>


        <button type="submit" class="btn btn-dark" onClick={poppin}>Submit</button>
      </form>




    </div>
  );
};

export default LJCreationPage;



//working -------

// const handleSubmit = (event) => {
//   const formData = new FormData(event.currentTarget);
//   event.preventDefault();
//   for (let [key, value] of formData.entries()) {
//     console.log(key, value);
//   }
// };

// <form onSubmit={handleSubmit}>
// <input type="text" name="username" placeholder="Email" />
// <input type="password" name="password" placeholder="Password" />
// <button type="submit">Login</button>
// </form>




// original -------
{/* <h1>Registration Form</h1>
<p>
  <input type="text" className="name" class="formStyle" placeholder="Name (required)" required />
</p>
<p>
  <input type="text" className="id" class="formStyle" placeholder="Staff_ID (required)" required />
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
<button type="submit" class="btn btn-dark">Submit</button> */}
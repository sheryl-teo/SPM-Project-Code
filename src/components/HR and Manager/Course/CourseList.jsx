import React, { useEffect, useState } from "react";
import { BrowserRouter as Router, Link } from 'react-router-dom';
import {
  Input,
  InputGroup,

} from "@chakra-ui/react";



// Fetching Course List Data
const CourseListContext = React.createContext({
  CourseList: [], fetchCourseList: () => { }
})

export default function CourseList() {
  const [CourseList, setCourseList] = useState([])
  const fetchCourseList = async () => {
    const response = await fetch("http://127.0.0.1:8000/job_roles/get_job_roles")
    const CourseList = await response.json()
    setCourseList(CourseList)
  }
  useEffect(() => {
    fetchCourseList()
  }, [])

  console.log(CourseList)

  return (

    <CourseListContext.Provider value={{ CourseList, fetchCourseList }}>

      <p><b>Courses Available</b></p>
      <ol>
        <AddCourses />
        {CourseList.map((CourseList) => (
          <li>{CourseList.Job_Role_ID} {CourseList.Job_Role_Name}</li>
        ))}
      </ol>

    </CourseListContext.Provider>
  )
}

// Adding Courses to Course List

function AddCourses() {
  const [item1, setItem1] = React.useState("")
  const [item2, setItem2] = React.useState("")
  const [item3, setItem3] = React.useState("")


  const { Courses, fetchCourseList } = React.useContext(CourseListContext)

  const handleInput1 = event => {
    setItem1(event.target.value)
  }

  const handleInput2 = event => {
    setItem2(event.target.value)
  }

  const handleInput3 = event => {
    setItem3(event.target.value)
  }

  const handleSubmit = (event) => {
    const newCourses = {
       "Job_Role_ID":item1,
       "Job_Role_Name":item2,
       "Job_Department":item3
    }
    console.log(newCourses)
    fetch("http://127.0.0.1:8000/job_role/create_job_role", 
    {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(newCourses)
    }).then(fetchCourseList)
  }

  return (
    <form>
      <InputGroup size="md">
        <Input
          pr="4.5rem"
          type="text"
          placeholder="Add a Course ID"
          aria-label="Add a Course ID"
          onChange={handleInput1}
        />
      </InputGroup>

      <InputGroup size="md">
        <Input
          pr="4.5rem"
          type="text"
          placeholder="Add a Course Name"
          aria-label="Add a Course Name"
          onChange={handleInput2}
        />
      </InputGroup>

      <InputGroup size="md">
        <Input
          pr="4.5rem"
          type="text"
          placeholder="Add a Course Desc"
          aria-label="Add a Course Desc"
          onChange={handleInput3}
        />

        <Input
          type='submit'
          onMouseEnter={handleSubmit} />
      </InputGroup>


    </form>
  )
}

// Adding Courses to Course List




// function CourseList(props) {
//     const CourseListItems = props.map(
//         (course) => {
//             return (
//                 <li>{course.Course_ID}: <a href = {`/Hr/Courses/${course.Course_ID}`}>{course.Course_Name}</a></li>
//             )
//         }
//     )
//     return (
//         <div>
//             <h2>Course List</h2>
//             <ol>
//                 <div>Courses Available:
//                 {CourseListItems}

//                 </div>
//             </ol>

//             <Link to="/">
//             <button>
//                 Back
//             </button>
//             </Link>
//         </div>
//     )
// }

// export default CourseList;
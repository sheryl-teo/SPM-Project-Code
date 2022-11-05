import React from 'react';
import './App.css';
import { BrowserRouter as Router, Routes, Route}
	from 'react-router-dom';
import Home from './components/home';
import Profile from './components/Staff/profile/profile';
import Staff from './components/Staff/staff_home';
import HR from './components/HR and Manager/HR_home'
import CourseList from './components/HR and Manager/Course/CourseList'
import CourseInfo from './components/HR and Manager/Course/CourseInfo'
import CourseAdd from './components/HR and Manager/Course/CourseAdd';
import LJCreationPage from './components/Staff/LJCreationPage/LJ_Creation_Page';
import JobList from './components/HR and Manager/Jobs/JobList';
function App() {

	// Test Data 
	// const courses = [ 
	// 	{
	// 	  Course_ID: "COR001",
	// 	  Course_Name: "Systems Thinking and Design",
	// 	  Course_Desc: "This foundation module aims to introduce students to the fundamental concepts and underlying principles of systems thinking",
	// 	  Course_Status: "Active",
	// 	  Course_Type: "Internal",
	// 	  Course_Category: "Core",
	// 	},
	
	// 	{
	// 	  Course_ID:"COR002",
	// 	  Course_Name: "Lean Six Sigma Green Belt Certification",
	// 	  Course_Desc: "Apply Lean Six Sigma methodology and statistical tools such as Minitab to be used in process analytics",
	// 	  Course_Status: "Active",
	// 	  Course_Type: "Internal",
	// 	  Course_Category: "Core",
	// 	},
	
	// 	{
	// 	  Course_ID:"COR004",
	// 	  Course_Name: "Service Excellence",
	// 	  Course_Desc: "The programme provides the learner with the key foundations of what builds customer confidence in the service industry",
	// 	  Course_Status: "Pending",
	// 	  Course_Type: "Internal",
	// 	  Course_Category: "Core",
	// 	}
	//   ] 
	//   ;

		// const CourseRoutes = courses.map(

		// 	(course) => {
		// 		console.log(course)
				
		// 		return (
		// 			<>
		// 			<Route path = {`/HR/Courses/${course.Course_ID}`} element = {CourseInfo(course)}/>
		// 			<Route path = {`/HR/Courses/${course.Course_ID}/CourseAdd`} element = {CourseAdd(course)}/>
		// 			</>
					
		// 		)
		// 	}
		// )
	  
	
return (
	<>
	<Router>
	<Routes>
		<Route exact path='/' element={<Home />} />
		<Route path="/staff" element={<Staff />} />
		<Route path="/staff/learningjourneyCreation" element={<LJCreationPage />} />
		<Route path = "/HR" element = {<HR />}/>
		{/* <Route path = "/HR/Courses" element = {CourseList(courses)}/> */}
		<Route path = "/HR/Courses" element = {<CourseList/>}/>
		<Route path = "HR/Roles" element = {<JobList/>}/>
		{/* {CourseRoutes} */}


		
	</Routes>
	</Router>
	</>
);
}

export default App;

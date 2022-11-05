import React from 'react';
import './App.css';
import { BrowserRouter as Router, Routes, Route}
	from 'react-router-dom';
import Home from './components/home';
import Profile from './components/Staff/profile/profile';
import Staff from './components/Staff/staff_home';
import HR from './components/HR and Manager/HR_home'
import CourseList from './components/HR and Manager/Course/CourseList'
import LJCreationPage from './components/Staff/LJCreationPage/LJ_Creation_Page';
import JobList from './components/HR and Manager/Jobs/JobList';
import SkillsList from './components/HR and Manager/Skills/SkillsList'
function App() {

		// const CourseRoutes = CourseList.map(

		// 	(course) => {
		// 		console.log(course)
				
		// 		return (
		// 			<>
		// 			<Route path = {`/HR/Courses/${course.Course_ID}`} element = {CourseInfo(course)}/>
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
		<Route path = "/HR/Courses" element = {<CourseList/>}/>
		<Route path = "HR/Roles" element = {<JobList/>}/>
		<Route path = "/HR/Skills" element = {<SkillsList/>}/>

	</Routes>
	</Router>
	</>
);
}

export default App;

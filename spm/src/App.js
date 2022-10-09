import React from 'react';
import './App.css';
import { BrowserRouter as Router, Routes, Route}
	from 'react-router-dom';
import Home from './components/home';
import Profile from './components/Staff/profile/profile';
import Staff from './components/Staff/staff_home';
import LJCreationPage from './components/Staff/LJCreationPage/LJ_Creation_Page';

function App() {
return (
	<Router>
	<Routes>
		<Route exact path='/' element={<Home />} />
		<Route path="/staff" element={<Staff />} />
		<Route path="/staff/learningjourneyCreation" element={<LJCreationPage />} />
	</Routes>
	</Router>
);
}

export default App;

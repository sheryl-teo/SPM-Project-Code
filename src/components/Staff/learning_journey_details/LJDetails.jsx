
import React from 'react';
import "./LJDetails.css";
import Courses from '../courses/courses';
import Skills from '../skills/skills';

const LJDetails = () => {
    return (
        <div className="ljDetails">
            <h1 className='position'>HR Manager</h1>

            <div className='courseSection'>
                <h2>Courses</h2>
                <Courses />
            </div>

            <div className='skillSection'>
                <h2>Skills</h2>
                <Skills />
            </div>
        </div>
    );
};

export default LJDetails;
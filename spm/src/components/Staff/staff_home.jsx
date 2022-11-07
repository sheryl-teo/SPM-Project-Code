import "./staff_home.css";
import React from 'react';
import Profile from './profile/profile';
import LJDetails from "./learning_journey_details/LJDetails";
import LearningJourneys from "./learningJourneys/learningJourneys";


const Staff = () => {
  return (
    <div>
      <h1 className='header'>
        LJPS
      </h1>
      <div>

        <div id="container">
          <div id="firstColumn"><Profile></Profile></div>
          <div id="secondColumn">
            <LearningJourneys />
            {/* <LJDetails></LJDetails> */}

          </div>
          
        </div>
        <div className="bottomright">
        <a href="/staff/learningjourneyCreation">
          Create Learning Journey
        </a>
      </div>
      </div>
      




    </div>
  );
};

export default Staff;
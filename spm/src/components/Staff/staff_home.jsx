
import React from 'react';
import Profile from './profile/profile';
import LearningJourney from './learning_journey/learningJourney';
import "./staff_home.css";


const Staff = () => {
  return (
    <div>
      <h1 className='header'>
        LJPS
      </h1>
      <div class="float-container">

        <div id="container">
          <div id="firstColumn"><Profile></Profile></div>
          <div id="secondColumn"><LearningJourney></LearningJourney></div>
        </div>

      </div>
      <a href="/staff/learningjourneyCreation">
        <img src="../../images/plus.png" alt="HTML tutorial"/>
      </a>




    </div>
  );
};

export default Staff;
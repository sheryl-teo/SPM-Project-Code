import "./staff_home.css";
import React from 'react';
import Profile from './profile/profile';
import LearningJourney from './learning_journey/learning_journey';



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
        <img src="plus.png" alt="Create Learning Journey"/>
      </a>




    </div>
  );
};

export default Staff;
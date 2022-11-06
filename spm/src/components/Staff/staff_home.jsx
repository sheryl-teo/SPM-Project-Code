import "./staff_home.css";
import React from 'react';
import Profile from './profile/profile';
import Details from "./details/details";



const Staff = () => {
  return (
    <div>
      <h1 className='header'>
        LJPS
      </h1>
      <div class="float-container">

        <div id="container">
          <div id="firstColumn"><Profile></Profile></div>
          <div id="secondColumn"><Details></Details></div>
        </div>

      </div>
      <a href="/staff/learningjourneyCreation">
        Create Learning Journey
      </a>




    </div>
  );
};

export default Staff;
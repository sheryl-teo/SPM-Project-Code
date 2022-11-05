import { BrowserRouter as Router,Link } from 'react-router-dom';
import React from 'react';


function HR() {
  return (
    <div>
      <a href="/Hr/Skills">
        <h1 className='header'>
          Skills
        </h1>
      </a>

      <a href="/Hr/Courses">
        <h1 className='header'>
          Courses
        </h1>
      </a>

      <a href="/Hr/Roles">
        <h1 className='header'>
          Roles
        </h1>
      </a>

      <Link to="/">
        <button type="button">
          Back
        </button>
      </Link>






    </div>
  );
};

export default HR;
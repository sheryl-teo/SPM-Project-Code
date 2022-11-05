import './home.css';
import React from 'react';


const Home = () => {
  return (
    <div>
      
      <p>
        <h1>WELCOME</h1>
      </p>
      <p>
        <h3>Please navigate to desired account</h3>
      </p>

      <p>
        <a href ="/Staff">
        <h3> Staff 

        </h3>
        </a>
      </p>
      

      <p>
        <a href ="/HR">
        <h3> HR 

        </h3>
        </a>
      </p>

      <p>
        <a href ="/Manager">
        <h3> Manager 

        </h3>
        </a>
      </p>
    </div>
  );
};

export default Home;

import React from 'react';
import "./learning_journey.css";

const IndivLearningJourney = () => {
  var count = 0

  return (
    <div className="IndivLearningJourneyDiv">
      <a href="/Staff/details">
        <h2>Learning Journey {count}</h2>
      </a>
    </div>
  );
};
  
export default IndivLearningJourney;
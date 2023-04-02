import React from 'react';
import './Welcome.scss';

const Welcome = ({ username }) => {
  return (
    <div className="welcome">
      <div className="text">
        <div className="title"> Welcome back, {username} </div>
        <div className="suggestion"> Complete all the quests and win a lot of points! </div>
      </div>
      <div className="monster-container">
        <img src="http://localhost:8002/monster/albastru.png" alt="blue grumpy monster" className="monster-image" />
      </div>
    </div>
  );
};

export default Welcome;

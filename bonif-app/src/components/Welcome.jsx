import React from 'react';
import './Welcome.scss';

const Welcome = ({ username, monster }) => {
  return (
    <div className="welcome">
      <div className="title"> Welcome back, {username} </div>
      <div className="suggestion"> Complete all the quests and win a lot of points </div>
      <div> {monster} </div>
    </div>
  );
};

export default Welcome;

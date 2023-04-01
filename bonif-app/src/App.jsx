import './App.scss';
import React, { useEffect, useState } from 'react';
import Quest from './components/Quest';
import Header from './components/Header';
import Welcome from './components/Welcome';
import CardSection from './components/CardSection';
import useAxiosGet from './helpers/useAxiosGet';
import PointsTracker from './components/PointsTracker';

function App() {
  //This needs to change when the authentication is set up to request for all the quests
  const quests = ['daily', 'weekly', 'monthly'];
  const questData = useAxiosGet('http://localhost:8002/quest/2');
  // const cxPoints = useAxiosGet('http://localhost:8002/customer/points/1');
  // const battlePassPoints = useAxiosGet('http://localhost:8002/battlepass/target/1');
  // console.log(cxPoints, battlePassPoints);
  // const customerData = useAxiosGet('http://localhost:8002/customer/2');

  const handleClickDots = (e) => {};

  return (
    <div className="App">
      <Header />
      <Welcome />
      {/* <PointsTracker /> */}
      <div className="quests-container">
        {quests.map((q, i) => {
          return (
            <Quest
              key={i}
              container={`quest-container${i}`}
              title="title"
              desc="desc"
              number="number"
              points="points"
              data={questData.data}
            />
          );
        })}
        <div className="points-container">
          <div className="point1">.</div>
          <div className="point2">.</div>
          <div className="point3">.</div>
        </div>
      </div>
      <CardSection />
    </div>
  );
}

export default App;

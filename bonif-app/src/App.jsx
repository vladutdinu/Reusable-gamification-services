import './App.scss';
import React, { useEffect, useState } from 'react';
import Header from './components/Header';
import Welcome from './components/Welcome';
import CardSection from './components/CardSection';
import useAxiosGet from './helpers/useAxiosGet';
import PointsTracker from './components/PointsTracker';
import Carousel from './components/Carousel';

function App() {
  //This needs to change when the authentication is set up to request for all the quests
  const quests = ['daily', 'weekly', 'monthly'];
  const questData = useAxiosGet('http://localhost:8002/quest/2');
  // const cxPoints = useAxiosGet('http://localhost:8002/customer/points/1');
  // const battlePassPoints = useAxiosGet('http://localhost:8002/battlepass/target/1');
  // console.log(cxPoints, battlePassPoints);
  // const customerData = useAxiosGet('http://localhost:8002/customer/2');

  return (
    <div className="App">
      <Header />
      <Welcome />
      {/* <PointsTracker /> */}
      <Carousel questData={questData} />
      <CardSection />
    </div>
  );
}

export default App;

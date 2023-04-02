import './App.scss';
import React from 'react';
import Header from './components/Header';
import Welcome from './components/Welcome';
import CardSection from './components/CardSection';
import useAxiosGet from './helpers/useAxiosGet';
import PointsTracker from './components/PointsTracker';
import Carousel from './components/Carousel';
import Leaderboard from 'leadsimple-kve3lq75zd';
import coffeesUrl from './assets/2cofee_cups.png';

function App() {
  //This needs to change when the authentication is set up to request for all the quests
  const questData = useAxiosGet('http://localhost:8002/quest/all/1');
  // const cxPoints = useAxiosGet('http://localhost:8002/customer/points/1');
  // const battlePassPoints = useAxiosGet('http://localhost:8002/battlepass/target/1');
  // console.log(cxPoints, battlePassPoints);
  const customerData = useAxiosGet('http://localhost:8002/customer/2');
  const userData = useAxiosGet('http://localhost:8001/user/id/1');
  const token = useAxiosGet('http://localhost:8002/token/1');
  console.log(token);
  console.log(userData);
  console.log(customerData);

  return (
    <div className="App">
      <Header />
      <Welcome />
      <PointsTracker />
      <Carousel questData={questData} />
      <CardSection qrCode={token?.data?.qr_code} name={userData?.data?.name} points={customerData?.data?.points?.points} />
      <div className="leaderboards-title">
        <img src={coffeesUrl} alt="2 cup of coffee" />
        <div className="text">
          <div className="title">Leaderboard</div>
          <div className="description">See the craziest guys of the community.</div>
        </div>
      </div>
      {/* <Leaderboard  /> */}
    </div>
  );
}

export default App;

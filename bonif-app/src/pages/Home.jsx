import Welcome from '../components/Welcome';
import Carousel from '../components/Carousel';
import CardSection from '../components/CardSection';
import useAxiosGet from '../helpers/useAxiosGet';
import coffeesUrl from '../assets/2cofee_cups.png';
import Header from '../components/Header';
import './Home.scss';
import Leaderboards from '../components/Leaderboards';

const Home = () => {
  const questData = useAxiosGet('http://localhost:8002/quest/all/1');
  const token = useAxiosGet('http://localhost:8002/token/1');
  const userData = useAxiosGet('http://localhost:8001/user/id/1');
  const customerData = useAxiosGet('http://localhost:8002/customer/1');
  console.log(questData);
  return (
    <div className="Home">
      <Header />
      <Welcome />
      {/* <PointsTracker /> */}
      <Carousel questData={questData} />
      <CardSection qrCode={token?.data?.qr_code} name={userData?.data?.name} points={customerData?.data?.points?.points} />
      <div className="leaderboards-title">
        <img src={coffeesUrl} alt="2 cup of coffee" />
        <div className="text">
          <div className="title">Leaderboard</div>
          <div className="description">See the craziest guys of the community.</div>
        </div>
      </div>
      <Leaderboards />
    </div>
  );
};

export default Home;

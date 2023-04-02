import Header from '../components/Header';
import useAxiosGet from '../helpers/useAxiosGet';
import './Coupons.scss';

const Coupons = ({ points }) => {
  const customerPoints = useAxiosGet('http://localhost:8002/customer/points/1');
  const allcoupons = useAxiosGet('http://localhost:8002/coupon/all/1');

  return (
    <div className="coupons-page">
      <Header />
      <div className="header">
        <h1>Coupons</h1>
        <p className="points"> You have {customerPoints?.data?.points} points available </p>
      </div>
      <div className="switcher">
        <div className="all-coupons"> All </div>
        <div className="active-coupons"> Active</div>
        <div className="bar-show"></div>
      </div>
    </div>
  );
};

export default Coupons;

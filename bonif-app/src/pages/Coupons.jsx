import Header from '../components/Header';
import './Coupons.scss';

const Coupons = () => {
  return (
    <div className="coupons-page">
      <Header />
      <div className="header">
        <h1>Coupons</h1>
        <p className="points"></p>
      </div>
    </div>
  );
};

export default Coupons;

import { Link } from 'react-router-dom';
import './HamburgerMenu.scss';

const HamburgerMenu = () => {
  return (
    <div className="overlay">
      <section className="hamburger-menu">
        <div className="home">
          <Link to="/"> Home </Link>
        </div>
        <div className="my-profile">
          <Link to="/myprofile"> My Profile </Link>
        </div>
        <div className="spinning-wheel">
          <Link to="/spinning-wheel"> Spinning Wheel </Link>
        </div>
        <div className="coupons">
          <Link to="coupons"> Coupons </Link>
        </div>
      </section>
    </div>
  );
};

export default HamburgerMenu;

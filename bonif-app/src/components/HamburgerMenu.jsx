import { Link } from 'react-router-dom';
import './HamburgerMenu.scss';

const HamburgerMenu = ({onClose}) => {
  return (
    <div className="overlay">
      <section className="hamburger-menu">
        <div className="home">
          <Link to="/" onClick={(e) => onClose(e)}> Home </Link>
        </div>
        <div className="my-profile">
          <Link to="/myprofile" onClick={(e) => onClose(e)}> My Profile </Link>
        </div>
        <div className="spinning-wheel">
          <Link to="/spinning-wheel" onClick={(e) => onClose(e)}> Spinning Wheel </Link>
        </div>
        <div className="coupons">
          <Link to="coupons" onClick={(e) => onClose(e)}> Coupons </Link>
        </div>
      </section>
    </div>
  );
};

export default HamburgerMenu;

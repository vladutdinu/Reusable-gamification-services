import { Link } from 'react-router-dom';
import './HamburgerMenu.scss';

const HamburgerMenu = ({ setOpenMenu }) => {
  const closeMenu = () => setOpenMenu(false);
  return (
    <div className="overlay">
      <section className="hamburger-menu">
        <div className="home">
          <Link to="/home" onClick={closeMenu}>
            Home
          </Link>
        </div>
        {/* <div className="my-profile">
          <Link to="/myprofile" onClick={closeMenu}>
            My Profile
          </Link>
        </div> */}
        <div className="spinning-wheel">
          <Link to="/spinning-wheel" onClick={closeMenu}>
            Spinning Wheel
          </Link>
        </div>
        <div className="coupons">
          <Link to="/coupons" onClick={closeMenu}>
            Coupons
          </Link>
        </div>
      </section>
    </div>
  );
};

export default HamburgerMenu;

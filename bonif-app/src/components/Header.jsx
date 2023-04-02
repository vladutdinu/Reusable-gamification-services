import React, { useState } from 'react';
import coffeeUrl from '../assets/coffee.png';
import './Header.scss';
import menuUrl from '../assets/menu.png';

const Header = () => {
  const [openMenu, setOpenMenu] = useState(false);

  return (
    <header className="header">
      <img src={coffeeUrl} alt="Coffee logo" className="coffe-logo" />
      <div className="title">Crazy Coffee</div>
      <img src={menuUrl} alt="Menu" className="hamburger" onClick={() => setOpenMenu(!openMenu)} />
    </header>
  );
};

export default Header;

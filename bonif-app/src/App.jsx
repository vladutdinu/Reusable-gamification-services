import React, { useState } from 'react';
import { Route, Routes } from 'react-router-dom';

import { LoginRegister } from './components/LoginRegister';
import { Login } from './components/Login';
import { Register } from './components/Register';
import './components/LoginRegister.scss';
import AuthContext from './context/AuthContext';
import Home from './pages/Home';
import Coupons from './pages/Coupons';

function App() {
  const [user, setUser] = useState('');
  return (
    <AuthContext.Provider value={{ user, setUser }}>
      <Routes>
        <Route path="/" element={<LoginRegister />} />
        <Route path="/login" element={<Login />} />
        <Route path="/register" element={<Register />} />
        <Route path="/home" element={<Home />} />
        <Route path="/coupons" element={<Coupons />} />
        <Route path="*" element={<LoginRegister />} />
      </Routes>
    </AuthContext.Provider>
  );
}

export default App;

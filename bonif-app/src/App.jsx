import React, { useState } from 'react';
import { Route, Routes } from 'react-router-dom';
// import Quest from './components/Quest';
// import Header from './components/Header';
// import Welcome from './components/Welcome';
// import CardSection from './components/CardSection';

import { LoginRegister } from './components/LoginRegister';
import { Login } from './components/Login';
import { Register } from './components/Register';
import './components/LoginRegister.scss';
import { AuthContext } from './context/AuthContext';
import { useAuth } from './customHooks/useAuth';
import Home from './pages/Home';

function App() {
  const { isAuthenticated } = useAuth();
  const [user, setUser] = useState('');
  return (
    <AuthContext.Provider value={{ user, setUser }}>
      <Routes>
        <Route path="/" element={<LoginRegister />} />
        <Route path="/login" element={<Login />} />
        <Route path="/register" element={<Register />} />
        <Route path="/home" element={<Home />} />
        <Route path="*" element={<LoginRegister />} />
      </Routes>
    </AuthContext.Provider>
  );
}

export default App;

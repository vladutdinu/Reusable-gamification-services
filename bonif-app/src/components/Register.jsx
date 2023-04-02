import './Login.scss';
import { useState, useEffect } from 'react';
import { useNavigate } from 'react-router-dom';
import useAxiosPost from '../customHooks/useAxiosPost';
import { useAuth } from '../customHooks/useAuth';

import { ColorRing } from 'react-loader-spinner';

export const Register = () => {
  const { data, loading, error, postData, response } = useAxiosPost('http://localhost:8001/user/signUp');
  const { login } = useAuth();
  const navigate = useNavigate();
  const [state, setState] = useState({
    name: '',
    email: '',
    password: '',
    password2: ''
  });

  const handleInputChange = (event) => {
    const { name, value } = event.target;
    setState((prevProps) => ({
      ...prevProps,
      [name]: value
    }));
  };

  const handleSubmit = async (event) => {
    event.preventDefault();
    await postData(state).then((res) => handlePageNavigation(res));
  };

  const handlePageNavigation = async (res) => {
    login(res);
    navigate('/home');
  };

  const handleArrowback = () => {
    navigate(-1);
  };
  return (
    <div className="login-container">
      <div className="nav-login">
        <div className="arrow-back" onClick={() => handleArrowback()}></div>
        <div className="small-coffee"></div>
      </div>
      <div className="text">
        <p>Hello! Register to get started</p>
      </div>
      <form onSubmit={(event) => handleSubmit(event)} className="form-container">
        <input type="text" name="name" placeholder="Username" value={state.name} onChange={handleInputChange} />
        <input type="email" name="email" placeholder="Enter email " value={state.email} onChange={handleInputChange} />
        <input type="password" name="password" placeholder="Enter password" value={state.password} onChange={handleInputChange} />
        <input
          type="password"
          name="password2"
          placeholder="Confirm Password"
          value={state.password2}
          onChange={handleInputChange}
        />

        {loading === true ? (
          <ColorRing
            visible={true}
            height="80"
            width="80"
            ariaLabel="blocks-loading"
            wrapperStyle={{}}
            wrapperClass="blocks-wrapper"
            colors={['#e15b64', '#f47e60', '#f8b26a', '#abbd81', '#849b87']}
          />
        ) : (
          <button type="submit">Register</button>
        )}
      </form>
    </div>
  );
};

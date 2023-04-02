import './Login.scss';
import { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import useAxiosPost from '../customHooks/useAxiosPost';
import { useAuth } from '../customHooks/useAuth';
export const Login = () => {
  const { data, loading, error, postData, response } = useAxiosPost('http://localhost:8001/user/signIn');
  const { login } = useAuth();
  const navigate = useNavigate();
  const [state, setState] = useState({
    email: '',
    password: ''
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
        <p>Welcome back! Glad to see you again!</p>
      </div>
      <form onSubmit={handleSubmit} className="form-container">
        <input type="text" name="email" placeholder="Email" value={state.email} onChange={handleInputChange} />
        <input type="password" name="password" placeholder="Password" value={state.password} onChange={handleInputChange} />
        <button type="submit">Login</button>
      </form>
    </div>
  );
};

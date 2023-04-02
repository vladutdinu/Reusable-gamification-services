import './Login.scss';
import { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import useAxiosPost from '../customHooks/useAxiosPost';
import axios from "axios";
import { useAuth } from '../customHooks/useAuth';
export const Login = () => {
  const { login } = useAuth();
  const navigate = useNavigate();
  const [loading, setLoading] = useState(false);
  const [responseStatus, setResponseStatus] = useState("");
  const [data, setData] = useState({
    email: "",
    password: "",
  });
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
    event.preventDefault()
    const url = "http://localhost:8001/user/logIn";
    setLoading(true);
    const payload = {
      email: state.email,
      password: state.password,
    };
    try {
        axios.post(url, payload).then((res) => {
          if(res.status === 200){
            setData(res.config.data)
            login(res.config.data)
          }
        });
    } catch (err) {
      console.log(err);
    } finally {
      setLoading(false);
    }
    if (!loading) {
      navigate("/home");
    } else if (data){
      navigate("/home")
    }
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

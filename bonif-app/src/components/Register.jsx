import "./Login.scss";
import { useState, useEffect } from "react";
import { useNavigate } from "react-router-dom";
import useAxiosPost from "../customHooks/useAxiosPost";
import { useAuth } from "../customHooks/useAuth";
import axios from "axios";
import { ColorRing } from "react-loader-spinner";

export const Register = () => {
  const { login, setAuthUser } = useAuth();
  const [loading, setLoading] = useState(false);
  const [responseStatus, setResponseStatus] = useState("");
  const [data, setData] = useState({
    name: "",
    email: "",
    id: 0,
    password: "",
  });
  const navigate = useNavigate();
  const [state, setState] = useState({
    name: "",
    email: "",
    password: "",
    password2: "",
  });

  const handleInputChange = (event) => {
    const { name, value } = event.target;
    setState((prevProps) => ({
      ...prevProps,
      [name]: value,
    }));
  };

  const handleSubmit = async (event) => {
    event.preventDefault()
    const url = "http://localhost:8001/user/signUp";
    setLoading(true);
    const payload = {
      name: state.name,
      email: state.email,
      password: state.password,
      password2: state.password2,
    };
    try {
        axios.post(url, payload).then((res) => {
        setData(res.data);
        setAuthUser(res.data);
        login(res.data);
        setResponseStatus(res.status);
      });
    } catch (err) {
      console.log(err);
    } finally {
      setLoading(false);
    }
    console.log(responseStatus);
    if (!loading && responseStatus === 200) {
      navigate("/home");
    } else if (data){
      navigate("/home")
    }
  };

  const handleArrowback = () => {
    navigate(-1);
  };
  return (
    <div className='login-container'>
      <div className='nav-login'>
        <div className='arrow-back' onClick={() => handleArrowback()}></div>
        <div className='small-coffee'></div>
      </div>
      <div className='text'>
        <p>Hello! Register to get started</p>
      </div>
      <form
        onSubmit={(event) => handleSubmit(event)}
        className='form-container'>
        <input
          type='text'
          name='name'
          placeholder='Username'
          value={state.name}
          onChange={handleInputChange}
        />
        <input
          type='email'
          name='email'
          placeholder='Enter email '
          value={state.email}
          onChange={handleInputChange}
        />
        <input
          type='password'
          name='password'
          placeholder='Enter password'
          value={state.password}
          onChange={handleInputChange}
        />
        <input
          type='password'
          name='password2'
          placeholder='Confirm Password'
          value={state.password2}
          onChange={handleInputChange}
        />

        {loading === true ? (
          <ColorRing
            visible={true}
            height='80'
            width='80'
            ariaLabel='blocks-loading'
            wrapperStyle={{}}
            wrapperClass='blocks-wrapper'
            colors={["#e15b64", "#f47e60", "#f8b26a", "#abbd81", "#849b87"]}
          />
        ) : (
          <button type='submit'>Register</button>
        )}
      </form>
    </div>
  );
};

import { useNavigate } from "react-router-dom";
import "./LoginRegister.scss";

export const LoginRegister = () => {
  const navigate = useNavigate();
  const onLogin = () => {
    navigate("/login");
  };

  const onRegister = () => {
    navigate("/register");
  };

  return (
    <div className='loginRegContainer'>
      <div className='cofee-images'>
        <div className='coffe-beans'></div>
        <div className='crazy-cofee'>
        </div>
        <div className="crazy-cofee-text"><p>Crazy coffee</p></div>
      </div>

      <div className='buttons-container'>
        <button className='login-button' onClick={() => onLogin()}>
          Login
        </button>
        <button className='register-button' onClick={() => onRegister()}>
          Register
        </button>
      </div>
    </div>
  );
};

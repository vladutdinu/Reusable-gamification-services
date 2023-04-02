import { useEffect, useState } from 'react';
import { useUser } from './useUser';
import { useLocalStorage } from './useLocalStorage';

export const useAuth = () => {
  const { user, addUser, removeUser } = useUser();
  const { getItem } = useLocalStorage();
  const [isAuthenticated, setIsAuthenthicated] = useState(false)

  useEffect(() => {
    const user = getItem('user');
    if (user) {
      addUser(JSON.parse(user));
    }
  }, []);

  const login = (user) => {
    addUser(user);
    setIsAuthenthicated(true)
  };

  const logout = () => {
    removeUser();
  };

  return { user, login, logout, isAuthenticated };
};

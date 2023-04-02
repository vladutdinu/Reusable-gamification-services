import { useState } from 'react';
import axios from 'axios';

const useAxiosPost = (url) => {
  const [data, setData] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);
  const [response, setResponse] = useState(null)

  const postData = async (body) => {
    setLoading(true);
    try {
      const response = await axios.post(url, body);
      setData(response.data)
      setResponse(response)
      
    } catch (err) {
      setError(err);
    } finally {
      setLoading(false);
    }
  };

  return { data, loading, error, postData, response };
};

export default useAxiosPost;
import React from 'react';
import { useFormContext } from 'react-hook-form';

const Input = ({ name, label, ...rest }) => {
  const { register } = useFormContext();
  return (
    <div>
      <label htmlFor={name}>{label}</label>
      <input {...register(name)} {...rest} />
    </div>
  );
};

export default Input;
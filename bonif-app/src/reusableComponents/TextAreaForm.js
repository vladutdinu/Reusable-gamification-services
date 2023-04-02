import React from 'react';
import { useFormContext } from 'react-hook-form';

const Textarea = ({ name, label, ...rest }) => {
  const { register } = useFormContext();
  return (
    <div>
      <label htmlFor={name}>{label}</label>
      <textarea {...register(name)} {...rest} />
    </div>
  );
};

export default Textarea;
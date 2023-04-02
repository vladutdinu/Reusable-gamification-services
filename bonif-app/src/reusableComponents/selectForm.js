import React from 'react';
import { useFormContext } from 'react-hook-form';

const Select = ({ name, label, options, ...rest }) => {
  const { register } = useFormContext();
  return (
    <div>
      <label htmlFor={name}>{label}</label>
      <select {...register(name)} {...rest}>
        {options.map((option) => (
          <option key={option.value} value={option.value}>
            {option.label}
          </option>
        ))}
      </select>
    </div>
  );
};

export default Select;
import React from 'react';
import { useFormContext } from 'react-hook-form';

const CheckboxGroup = ({ name, label, options, ...rest }) => {
  const { register } = useFormContext();
  return (
    <fieldset>
      <legend>{label}</legend>
      {options.map((option) => (
        <div key={option.value}>
          <input
            type="checkbox"
            id={`${name}-${option.value}`}
            value={option.value}
            {...register(name)}
            {...rest}
          />
          <label htmlFor={`${name}-${option.value}`}>{option.label}</label>
        </div>
      ))}
    </fieldset>
  );

};

export default CheckboxGroup;
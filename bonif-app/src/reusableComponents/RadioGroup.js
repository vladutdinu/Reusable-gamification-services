import React from 'react';
import { useFormContext } from 'react-hook-form';

const RadioGroup = ({ name, label, options, ...rest }) => {
  const { register } = useFormContext();
  return (
<fieldset>
      <legend>{label}</legend>
      {options.map((option) => (
        <div key={option.value}>
          <input
            type="radio"
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

export default RadioGroup;
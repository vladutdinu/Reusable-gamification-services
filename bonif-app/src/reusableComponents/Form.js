import React from 'react';
import { useForm, FormProvider } from 'react-hook-form';
import Input from './Input';

const Form = () => {
  const methods = useForm();
  const { handleSubmit } = methods;

  const onSubmit = (data) => {
    console.log(data);
  };

  return (
    <FormProvider {...methods}>
      <form onSubmit={handleSubmit(onSubmit)}>
        <Input name="firstName" label="First Name" />
        <Input name="lastName" label="Last Name" />
        <button type="submit">Submit</button>
      </form>
      </FormProvider>
  );
};

export default Form;
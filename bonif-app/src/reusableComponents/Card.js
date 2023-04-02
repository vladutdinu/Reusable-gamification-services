import React from 'react';

const Card = ({ children, ...rest }) => {
  return (
    <div {...rest}>
      {children}
    </div>
  );
};

export default Card;
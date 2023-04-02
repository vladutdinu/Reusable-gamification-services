import React from 'react';

const Modal = ({ children, isOpen, onClose, ...rest }) => {
  if (!isOpen) return null;

  return (
    <div>
      <div>
        <button onClick={onClose}>Close</button>
      </div>
      <div {...rest}>
        {children}
      </div>
    </div>
  );
};

export default Modal;
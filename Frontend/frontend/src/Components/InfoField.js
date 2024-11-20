import React from 'react';
// import './InfoField.css'; // Styles für InfoField

const InfoField = ({ message }) => {
  return (
    <div className="info-field">
      <p>{message}</p>
    </div>
  );
};

export default InfoField;
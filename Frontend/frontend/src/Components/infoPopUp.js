import React, { useState } from 'react';
import './EntryFormModal.css'; // Modal Styles
import { getCsrfToken } from "../utils/csrf"; // Function for csrf

const InfoPopUp = ({ isOpen, onClose, message }) => {
  const handleOkay = () => {
        onClose();
    };    

  if (!isOpen) return null;

  return (
    <div className="modal-overlay">
      <div className="popup-content">
        <h4> {message} </h4>
          <button className='btn-okay' onClick={handleOkay}>Okay</button>
      </div>
    </div>
  );
};

export default InfoPopUp;
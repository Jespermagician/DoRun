import React from 'react';
import './EntryFormModal.css'; // Modal Styles

const ChoicePopUp = ({ isOpen, onClose, message }) => {
  const handle = (choice) => {
    onClose(choice); 
  };

  if (!isOpen) return null;

  return (
    <div className="modal-overlay">
      <div className="popup-content">
        <h3>{message}</h3>
        <button className="modal-buttons btn-left" onClick={() => handle(true)}>OK!</button>
        <button className="modal-buttons btn-right" onClick={() => handle(false)}>Abbrechen</button>
      </div>
    </div>
  );
};

export default ChoicePopUp;

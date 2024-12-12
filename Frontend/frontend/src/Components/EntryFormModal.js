import React, { useState } from 'react';
import './EntryFormModal.css'; // Modal Styles

const EntryFormModal = ({ isOpen, onClose, onSubmit, initialData }) => {
  const [formData, setFormData] = useState(initialData || { firstname: "", lastname: "", DonoAmount: "", FixedAmount: ""  });

  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData({ ...formData, [name]: value });
  };

  const handleSubmit = () => {
    onSubmit(formData);
    onClose();
  };

  if (!isOpen) return null;

  return (
    <div className="modal-overlay">
      <div className="modal-content">
        <h3>{initialData ? "Eintrag bearbeiten" : "Neuer Eintrag"}</h3>
        <label>Vorname: <input type="text" name="firstname" value={formData.firstname} onChange={handleChange} /></label>
        <label>Nachname: <input type="text" name="lastname" value={formData.lastname} onChange={handleChange} /></label>
        <label>Email: <input type="email" name="email" value={formData.email} onChange={handleChange} /></label>
        <label>Straße: <input type="text" name="street" value={formData.street} onChange={handleChange} /></label>
        <label>Haus Nr.: <input type="text" name="houseNr" value={formData.houseNr} onChange={handleChange} /></label>
        <label>PLZ: <input type="text" name="Plz" value={formData.Plz} onChange={handleChange} /></label>
        <label>Betrag: <input type="number" name="DonoAmount" value={formData.DonoAmount} onChange={handleChange} /></label>
        <label>Festbetrag: <input type="checkbox" name="FixedAmount" value={formData.FixedAmount} onChange={handleChange} /></label>
        <div className="modal-buttons btn-left">
          <button onClick={handleSubmit}>Speichern</button>
        </div>
        <div className="modal-buttons btn-right">
          <button onClick={onClose}>Abbrechen</button>
        </div>
      </div>
    </div>
  );
};

export default EntryFormModal;
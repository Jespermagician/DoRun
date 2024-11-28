import React, { useState } from 'react';
import './EntryFormModal.css'; // Modal Styles

const EntryFormModal = ({ isOpen, onClose, onSubmit, initialData }) => {
  const [formData, setFormData] = useState(initialData || { name: "", amount: "", date: "" });

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
        <label>Name: <input type="text" name="name" value={formData.name} onChange={handleChange} /></label>
        <label>Betrag: <input type="number" name="amount" value={formData.amount} onChange={handleChange} /></label>
        <label>Datum: <input type="date" name="date" value={formData.date} onChange={handleChange} /></label>
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
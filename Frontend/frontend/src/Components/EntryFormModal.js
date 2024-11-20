import React, { useState } from 'react';
// import './EntryFormModal.css'; // Modal Styles

const EntryFormModal = ({ closeModal, addEntry }) => {
  const [entryData, setEntryData] = useState({
    name: '',
    description: '',
    category: 'General',
  });

  const handleChange = (e) => {
    const { name, value } = e.target;
    setEntryData({ ...entryData, [name]: value });
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    addEntry(entryData); // Eintrag hinzufügen
  };

  return (
    <div className="modal-overlay">
      <div className="modal-content">
        <h2>Neuen Eintrag hinzufügen</h2>
        <form onSubmit={handleSubmit}>
          <div className="form-field">
            <label>Name</label>
            <input
              type="text"
              name="name"
              value={entryData.name}
              onChange={handleChange}
              required
            />
          </div>
          <div className="form-field">
            <label>Beschreibung</label>
            <textarea
              name="description"
              value={entryData.description}
              onChange={handleChange}
              required
            />
          </div>
          <div className="form-field">
            <label>Kategorie</label>
            <select
              name="category"
              value={entryData.category}
              onChange={handleChange}
            >
              <option value="General">General</option>
              <option value="Technology">Technology</option>
              <option value="Business">Business</option>
            </select>
          </div>
          <div className="modal-actions">
            <button type="submit">Eintrag hinzufügen</button>
            <button type="button" onClick={closeModal}>
              Abbrechen
            </button>
          </div>
        </form>
      </div>
    </div>
  );
};

export default EntryFormModal;
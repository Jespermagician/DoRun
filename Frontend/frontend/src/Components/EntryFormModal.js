import React, { useState, useEffect } from 'react';
import './EntryFormModal.css'; // Modal styling
import PerfectScrollbar from "react-perfect-scrollbar";
import "react-perfect-scrollbar/dist/css/styles.css";

const EntryFormModal = ({ isOpen, onClose, onSubmit, initialData }) => {
  const [formData, setFormData] = useState(initialData || {
    firstname: "",
    lastname: "",
    email: "",
    street: "",
    houseNr: "",
    Plz: "",
    DonoAmount: "",
    FixedAmount: false
  });

  const [infoMessage, setInfoMessage] = useState("");

  useEffect(() => {
    changeInfoMessage(formData.FixedAmount);
  }, [formData.FixedAmount, formData.DonoAmount]);

  const handleChange = (e) => {
    const { name, value } = e.target;
    const updatedValue = name === "DonoAmount" ? value.replace(",", ".") : value;
    setFormData({ ...formData, [name]: updatedValue });
  };

  const handleSubmit = (e) => {
    // The button is inverted, so the value has to be flipped
    formData.FixedAmount = !formData.FixedAmount 
    e.preventDefault();
    onSubmit(formData);
    onClose();
  };

  const changeInfoMessage = (toggle) => {
    const formatted = parseFloat(formData.DonoAmount || 0).toLocaleString("de-DE", {
      style: "currency",
      currency: "EUR"
    });

    if (!toggle) {
      setInfoMessage(`Ab einem gelaufenen Kilometer werden einmalig ${formatted} gespendet.`);
    } else {
      setInfoMessage(`Es werden ${formatted} pro Kilometer gespendet.`);
    }
  };

  if (!isOpen) return null;

  return (
    <form onSubmit={handleSubmit}>
    <div className="modal-overlay">
    {/* <div className="modal-scroll-wrapper">
      <PerfectScrollbar> */}
        <div className="modal-content">
            <p className='pop-header'>
              {initialData ? "Eintrag bearbeiten" : "Neuer Eintrag"}
            </p>

            {/* Form Fields */}
            <div className="form-group">
              <label>Vorname* <input type="text" name="firstname" placeholder="Vorname eingeben" value={formData.firstname} onChange={handleChange} required /></label>
            </div>
            <div className="form-group">
              <label>Nachname* <input type="text" name="lastname" placeholder="Nachname eingeben" value={formData.lastname} onChange={handleChange} required /></label>
            </div>
            <div className="form-group">
              <label>E-Mail* <input type="email" name="email" placeholder="E-Mail-Adresse eingeben" value={formData.email} onChange={handleChange} required /></label>
            </div>
            <div className="form-group">
              <label>Straße: <input type="text" name="street" placeholder="Straße eingeben" value={formData.street} onChange={handleChange} /></label>
            </div>
            <div className="form-group">
              <label>Hausnummer: <input type="text" name="houseNr" placeholder="Hausnummer eingeben" value={formData.houseNr} onChange={handleChange} /></label>
            </div>
            <div className="form-group">
              <label>PLZ: <input type="text" name="Plz" placeholder="Postleitzahl eingeben" value={formData.Plz} onChange={handleChange} /></label>
            </div>

            {/* Betrag + Toggle in einer Zeile */}
            <div className="form-group">
              <label>Betrag*</label>
              <div className="form-group horizontal">
                <input
                  type="number"
                  name="DonoAmount"
                  min="0.00"
                  placeholder="z. B. 5.00 €"
                  value={formData.DonoAmount}
                  onChange={handleChange}
                  step={1.00}
                  required
                />
                <div className="btn btn-pill">
                  <input
                    type="checkbox"
                    name="FixedAmount"
                    className="checkbox"
                    checked={formData.FixedAmount}
                    onChange={(e) => {
                      const checked = e.target.checked;
                      setFormData({ ...formData, FixedAmount: checked });
                      changeInfoMessage(checked);
                    }}
                  />
                  <div className="knob"></div>
                  <div className="btn-bg"></div>
                </div>
              </div>
            </div>

            {/* Info message */}
            <div className="info-box">
              <p>{infoMessage}</p>
            </div>

            {/* Buttons */}
            <div className="modal-buttons">
              <button className="btn-left" type="submit">Speichern</button>
              <button className="btn-right" type="button" onClick={onClose}>Abbrechen</button>
            </div>
          </div>
        {/* </PerfectScrollbar> */}
        {/* </div> */}
      </div>
    </form>
  );
};

export default EntryFormModal;

import React, { useState, useEffect } from 'react';
import './EntryFormModal.css'; // Modal styling
import PerfectScrollbar from "react-perfect-scrollbar";
import "react-perfect-scrollbar/dist/css/styles.css";

const EntryFormModal = ({ isOpen, onClose, onSubmit, initialData }) => {
  const empty_data = {
    firstname: "",
    lastname: "",
    email: "",
    street: "",
    houseNr: "",
    Plz: "",
    DonoAmount: "",
    FixedAmount: true,
    DonoID: -1,
    iscertreq: false
  }
  const [formData, setFormData] = useState(initialData || empty_data);
  const [infoMessage, setInfoMessage] = useState("");
  const [is_cert_checked_temp, SetIs_cert_checked_temp] = useState(false);

  // Update formData whenever the modal is opened
  useEffect(() => {
    if (isOpen) {

      setFormData(initialData || empty_data);
      SetIs_cert_checked_temp(initialData ? initialData.iscertreq: false)
    }
  }, [isOpen, initialData]);

  useEffect(() => {
    changeInfoMessage(formData.FixedAmount);
  }, [formData.FixedAmount, formData.DonoAmount]);

  const handleChange = (e) => {
    const { name, value } = e.target;
    const updatedValue = name === "DonoAmount" ? value.replace(",", ".") : value;
    setFormData({ ...formData, [name]: updatedValue });
  };
  const handleClose = () => {
    setFormData(empty_data);
    onClose();
  }

  const handleSubmit = (e) => {
    console.log("iscertreq")
    console.log("iscertreq")
    console.log(is_cert_checked_temp)
    if(is_cert_checked_temp) {
      console.log("cert angefordert!")
      if(formData.street.trim() == "" || formData.houseNr.trim() == ""  || formData.Plz.trim() == "") {
          setInfoMessage("Die Adresse wird für die Spendenbescheinigung benötigt!")
          return;
        }
    }

    // The button is inverted, so the value has to be flipped
    formData.FixedAmount = !formData.FixedAmount 
    e.preventDefault();
    let temp_formData = formData;
    temp_formData.iscertreq = is_cert_checked_temp;
    setFormData(temp_formData)
    onSubmit(formData);
    changeInfoMessage(formData.FixedAmount);
    handleClose();
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
              <label>Straße: <input type="text" name="street" placeholder="Straße eingeben" value={formData.street} onChange={handleChange} required={is_cert_checked_temp} /></label>
            </div>
            <div className="form-group">
              <label>Hausnummer: <input type="text" name="houseNr" placeholder="Hausnummer eingeben" value={formData.houseNr} onChange={handleChange} required={is_cert_checked_temp} /></label>
            </div>
            <div className="form-group">
              <label>PLZ: <input type="text" name="Plz" placeholder="Postleitzahl eingeben" value={formData.Plz} onChange={handleChange} required={is_cert_checked_temp} /></label>
            </div>

            {/* Betrag + Toggle in einer Zeile */}
            <div className="form-group">
              <label>*Betrag (Eingeben und Art auswählen)</label>
              <div className="form-group horizontal">
                <input
                  type="number"
                  name="DonoAmount"
                  min={0.01}
                  max={10000}
                  placeholder="z. B. 5.00 €"
                  value={formData.DonoAmount}
                  onChange={handleChange}
                  step={0.01}
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

            <div className="check-don-cert"> 
              <input
                type="checkbox" id="check-don-cert"
                checked={is_cert_checked_temp}
                onChange={(e) => SetIs_cert_checked_temp(e.target.checked)}
              />
              <label htmlFor="check-don-cert" >
                Ja, mein*e Sponor*in möchte eine Spendenbescheinigung erhalten
              </label>
            </div>
            {/* Buttons */}
            <div className="modal-buttons">
              <button className="btn-left" type="submit">Speichern</button>
              <button className="btn-right" type="button" onClick={handleClose}>Abbrechen</button>
            </div>
          </div>
        {/* </PerfectScrollbar> */}
        {/* </div> */}
      </div>
    </form>
  );
};

export default EntryFormModal;

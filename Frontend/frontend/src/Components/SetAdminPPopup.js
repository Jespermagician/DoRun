import React, { useState } from 'react';
import './EntryFormModal.css'; // Modal Styles

const SetAdminPPopup = ({ isOpen, onClose, password, email}) => {
    
    // const [password, setPassword] = useState("");
    const [confirmPassword, setConfirmPassword] = useState("");
    const [error, setError] = useState("");

  const handlePasswordforAdmin = async (e) => {
    e.preventDefault();
    // setPassword(initialData);
    alert(password);
    alert(confirmPassword);
    if (password !== confirmPassword) {
        setError("Die Passwörter stimmen nicht überein.");
        return;
    }
    try {
      const response = await fetch("http://127.0.0.1:8000/api/resetpassword", { 
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ email, password}),
      });
      const data = await response.json();
      if (!response.ok) {
        // throw new Error(data.message || "Fehler bei der Anmeldung");
        throw new Error(data.message);
      }
    } catch (error) {
      setError(error.message);
    }
  };

  const handleChange = (e) => {
    const { value } = e.target;
    // alert(value);
    setConfirmPassword(value);
    // alert(confirmPassword);
  };

  if (!isOpen) return null;

  return (
    <div className="modal-overlay">
      <div className="popup-content">
        <h3>Setzen sie ein Passwort für den Adminnutzer</h3>
        {error && <p className="error">{error}</p>}
        <label>Passwort: <input type="password" name="password" value={password}/></label>
        <label>Passwort bestätigen: <input type="password" name="confirmpassword" onChange={handleChange}/></label>
        <div className="modal-buttons btn-left">
          <button onClick={handlePasswordforAdmin}>Speichern</button>
        </div>
        <div className="modal-buttons btn-right">
          <button onClick={onClose}>Abbrechen</button>
        </div>
      </div>
    </div>
  );
};

export default SetAdminPPopup;
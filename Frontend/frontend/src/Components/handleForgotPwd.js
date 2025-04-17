import React, { useState } from 'react';
import './EntryFormModal.css'; // Modal Styles
import { getCsrfToken } from "../utils/csrf"; // Function for csrf
import { getBackEndDomain } from "../utils/backend-domain";

const HandleForgotPwd = ({ isOpen, onClose }) => {
  const [email, setEMail] = useState("");
  const [error, setError] = useState("");
  const [success, setSuccess] = useState("");
  const [message, setMessage] = useState(""); // State for the message

  const handleMailSubmit = async (e) => {
    e.preventDefault();
    const domain = window.location.host;
    setMessage(""); 
    try {

    // Get CSRF-Token and cookie 
      const csrfToken = await getCsrfToken();
      const backEndDomain = await getBackEndDomain();
      const response = await fetch(`${backEndDomain}/mail/send-new-pwd/${email}/${domain}`, {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
          "X-CSRFToken": csrfToken, // Füge das CSRF-Token als Header hinzu
        },
        credentials: "include", // Cookies mit einbeziehen
      });

      if (!response.ok) {
        throw new Error(response.statusText);
      }

      // Weiterleitung zum Dashboard
      
      setMessage("E-Mail wurde versendet!")
    } catch (error) {
      setError(error.message);
    }
  };

  const handleChange = (e) => {
    setEMail(e.target.value);
  };

  if (!isOpen) return null;

  return (
    <div className="modal-overlay">
      <div className="popup-content">
        <h3>Geben Sie ihre E-Mail an um Ihr Passwort zu ändern!</h3>
        {error && <p className="error">{error}</p>}
        {success && <p className="success">{success}</p>}
        <form className='form-group-black' onSubmit={handleMailSubmit}>
          <label>
            E-Mail-Adresse: 
            <input
              type="email"
              name="mail"
              value={email}
              onChange={handleChange}
              required
              placeholder='example@mail.de'
            />
          </label>
          {message && <p className="message">{message}</p>} {/* Conditionally render the message */}
          <div className='center-btns'>
              <button className="modal-buttons btn-left" type="submit">Senden</button>
              <button className="modal-buttons btn-right" onClick={onClose}>Abbrechen</button>
          </div>
        </form>
      </div>
    </div>
  );
};

export default HandleForgotPwd;
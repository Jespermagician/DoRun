import "./Dashboard.css";
import React, { useState, useEffect } from 'react';
import { IoHomeOutline } from "react-icons/io5";
import { useNavigate } from "react-router-dom";
import PageHeader from "../Components/PageHeader";
import { getCsrfToken } from "../utils/csrf";

const UserSettings = () => {
  const [userid, setUserid] = useState(Number);
  const [oldPwd, setOldPwd] = useState("");
  const [newPwd, setNewPwd] = useState("");
  const [nwdPwd2, setNewPwd2] = useState("");
  const [message, setMessage] = useState(""); // State for the message
  const [message_success, setMessage_sucess] = useState(""); // State for the message
  const navigate = useNavigate();
  

  useEffect(() => {
    const userid = localStorage.getItem("DoRunUserid");
    setUserid(userid);
  }, []);

  const handleHome = () => {
    navigate("/home");
  };

  const changePassword = async (e) => {
    try {
      const csrfToken = await getCsrfToken();
      const response = await fetch("http://127.0.0.1:8000/api/reset-user-pwd", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
          "X-CSRFToken": csrfToken,
        },
        credentials: "include",
        body: JSON.stringify({
          iduser: userid,
          oldPwd: oldPwd,
          newPwd: newPwd,
        }),
      });
  
      const data = await response.json();
      setMessage(data.message);  // <-- Nachricht immer aus Backend übernehmen
  
      if (!response.ok) {
        throw new Error(data.message || "Fehler beim Ändern des Passworts!");
      }
  
      return true;
  
    } catch (error) {
      console.error("Fehler beim Ändern des Passworts:", error);
      // setMessage hier NICHT nochmal nötig, weil es oben bereits gesetzt wurde
    }
  };
  

  const handlePasswordChange = async (e) => {
    setMessage(""); // Clear the message if everything is fine
    setMessage_sucess(""); // Clear the message if everything is fine
    e.preventDefault();
    if (newPwd !== nwdPwd2) {
      setMessage("Die Passwörter stimmen nicht überein.");
      return;
    }
    if (newPwd.length < 8) {
      setMessage("Das neue Passwort muss mindestens 8 Zeichen haben.");
      return;
    }
    const hasLetter = /[a-zA-Z]/.test(newPwd); // Prüft auf Buchstaben
    const hasNumber = /\d/.test(newPwd); // Prüft auf Zahlen
    const hasSpecialChar = /[!@#$%^&*(),.?":{}|<>]/.test(newPwd); // Prüft auf Sonderzeichen
    if (!hasLetter || !hasNumber || !hasSpecialChar) {
      setMessage("Das Passwort muss mindestens einen Buchstaben, eine Zahl und ein Sonderzeichen enthalten.");
      return;
    }

      if(await changePassword(e))
      {
        setMessage(""); // Clear the message if everything is fine
        setNewPwd("");
        setNewPwd2("");
        setOldPwd("");
        setMessage_sucess("Passwort erfolgreich geändert!");
      }
  }
  

  

  return (
    <div>
      <div>
        <button className="logout-btn" onClick={handleHome}>
          <IoHomeOutline /> Home
        </button>
      </div>

      <div className="dashboard-container">
        <PageHeader title={"Einstellungen"} />

        <div className="pwd-change-section">
          <div className="form-section">
            <h3>Passwort ändern</h3>
            <form onSubmit={handlePasswordChange}>
              <div>
                <label>Altes Passwort:</label>
                <input 
                  type="password" 
                  required 
                  value={oldPwd}
                  onChange={(e) => setOldPwd(e.target.value)}
                />
              </div>
              <div>
                <label>Neues Passwort:</label>
                <input 
                  type="password" 
                  required 
                  value={newPwd}
                  onChange={(e) => setNewPwd(e.target.value)}
                />
              </div>
              <div>
                <label>Neues Passwort wiederholen:</label>
                <input 
                  type="password" 
                  required 
                  value={nwdPwd2}
                  onChange={(e) => setNewPwd2(e.target.value)}
                />
              </div>
              {message && <p className="message">{message}</p>} {/* Conditionally render the message */}
              {message_success && <p className="message-success">{message_success}</p>} {/* Conditionally render the message */}
              <button type="submit">Ändern</button>
            </form>
          </div>
          <div className="entry-list-section">
          </div>
        </div>

        <div className="content-section">
          {/* leer */}
        </div>
      </div>
    </div>
  );
};

export default UserSettings;
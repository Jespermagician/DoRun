import React, { useState, useEffect } from "react";
import { useNavigate } from "react-router-dom";
import "./Login.css"; // CSS-Datei für das Styling und Slide-Effekt
import { getCsrfToken } from "../utils/csrf"; // Function for csrf

function Register() {
  const [firstname, setFirstName] = useState("");
  const [lastname, setLastName] = useState("");
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [confirmPassword, setConfirmPassword] = useState("");
  const [error, setError] = useState("");
  const navigate = useNavigate();

  // Beispiel für Handling mit API Backend Aufruf
  const handleLogin = () => {
    navigate("/");
  };

  // Handler für die Registrierung
  const handleRegister = async (e) => {
    e.preventDefault();
    if (email === "" || password === "" || confirmPassword === "") {
      setError("Bitte alle Felder ausfüllen.");
      return;
    }
    if (password !== confirmPassword) {
      setError("Die Passwörter stimmen nicht überein.");
      return;
    }

    try {

    // Get CSRF-Token and cookie 
    const csrfToken = await getCsrfToken();

      const response = await fetch("http://127.0.0.1:8000/api/register/", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
          "X-CSRFToken": csrfToken, // Füge das CSRF-Token als Header hinzu
        },
        credentials: "include", // Cookies mit einbeziehen
        body: JSON.stringify({ firstname, lastname, email, password }),
      });

      const data = await response.json();

      if (!response.ok) {
        throw new Error(data.message || "Fehler bei der Anmeldung");
      }

      // Weiterleitung zum Dashboard
      navigate("/");
      alert("Email zu Verifizierung wurde an " + email + " gesendet");
    } catch (error) {
      setError(error.message);
    }
  };

  return (
    <div className="container register-mode">
      <div className="form-container">
        {/* Register Formular */}
        <div className="form-panel register-panel">
          <h2>Registrieren</h2>
          {error && <p className="error">{error}</p>}
          <form onSubmit={handleRegister}>
            <div className="form-group">
              <label className="login-label" htmlFor="register-firstName">Vorname</label>
              <input
                className="login-input"
                type="text"
                id="register-firstName"
                placeholder="Vorname eingeben"
                value={firstname}
                onChange={(e) => setFirstName(e.target.value)}
                required
              />
            </div>
            <div className="form-group">
              <label className="login-label" htmlFor="register-lastName">Nachname</label>
              <input
                className="login-input"
                type="text"
                id="register-lastName"
                placeholder="Nachname eingeben"
                value={lastname}
                onChange={(e) => setLastName(e.target.value)}
                required
              />
            </div>
            <div className="form-group">
              <label className="login-label" htmlFor="register-email">E-Mail-Adresse</label>
              <input
                className="login-input"
                type="email"
                id="register-email"
                placeholder="E-Mail eingeben"
                value={email}
                onChange={(e) => setEmail(e.target.value)}
                required
              />
            </div>
            <div className="form-group">
              <label className="login-label" htmlFor="register-password">Passwort</label>
              <input
                className="login-input"
                type="password"
                id="register-password"
                placeholder="Passwort eingeben"
                value={password}
                onChange={(e) => setPassword(e.target.value)}
                required
              />
            </div>
            <div className="form-group">
              <label className="login-label" htmlFor="confirm-password">Passwort bestätigen</label>
              <input
                className="login-input"
                type="password"
                id="confirm-password"
                placeholder="Passwort bestätigen"
                value={confirmPassword}
                onChange={(e) => setConfirmPassword(e.target.value)}
                required
              />
            </div>
            <button type="submit">Registrieren</button>
            <p className="switch-text">
              Bereits ein Konto? <span onClick={handleLogin}>Anmelden</span>
            </p>
          </form>
        </div>
      </div>
    </div>
  );
}

export default Register;

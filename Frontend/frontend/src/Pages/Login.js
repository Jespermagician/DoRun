import React, { useState } from "react";
import { useNavigate } from "react-router-dom";
import "./Login.css"; // CSS-Datei für das Styling und Slide-Effekt

function Login() {
  const [isLogin, setIsLogin] = useState(true); // Zustand für Anzeige des Login oder Register Formulars
  const [firstname, setFirstName] = useState("");
  const [lastname, setLastName] = useState("");
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [confirmPassword, setConfirmPassword] = useState("");
  const [error, setError] = useState("");
  const navigate = useNavigate();

  // Handler für die Umschaltung zwischen Login und Register Formular
  const toggleForm = () => {
    setIsLogin(!isLogin);
    setEmail("");
    setPassword("");
    setConfirmPassword("");
    setError("");
  };

  // Handler für die Anmeldung
  const handleLogin1 = (e) => {
    e.preventDefault();
    if (email === "" || password === "") {
      setError("Bitte alle Felder ausfüllen.");
      return;
    }
    alert("Anmeldung erfolgreich!");
  };

  // Beispiel für Handling mit API Backend Aufruf
  const handleLogin = async (e) => {
    e.preventDefault();
    try {
      const response = await fetch("http://localhost:5000/api/login", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ email, password }),
      });
      const data = await response.json();
      if (!response.ok) {
        throw new Error(data.message || "Fehler bei der Anmeldung");
      }

      // Speichere das Token (optional)
      localStorage.setItem("token", data.token);

      // Weiterleitung zum Dashboard
      navigate("/home");
    } catch (error) {
      setError(error.message);
    }
  };

  // Handler für die Registrierung
  const handleRegister = (e) => {
    e.preventDefault();
    if (email === "" || password === "" || confirmPassword === "") {
      setError("Bitte alle Felder ausfüllen.");
      return;
    }
    if (password !== confirmPassword) {
      setError("Die Passwörter stimmen nicht überein.");
      return;
    }
    alert("Registrierung erfolgreich!");
  };

  return (
    <div className={`container ${isLogin ? "login-mode" : "register-mode"}`}>
      <div className={`form-container ${isLogin ? "slide-login" : "slide-register"}`}>
        {/* Login Formular */}
        <div className="form-panel login-panel">
          <h2>Anmelden</h2>
          {error && <p className="error">{error}</p>}
          <form onSubmit={handleLogin}>
            <div className="form-group">
              <label htmlFor="login-email">E-Mail-Adresse</label>
              <input
                type="email"
                id="login-email"
                placeholder="E-Mail eingeben"
                value={email}
                onChange={(e) => setEmail(e.target.value)}
                required
              />
            </div>
            <div className="form-group">
              <label htmlFor="login-password">Passwort</label>
              <input
                type="password"
                id="login-password"
                placeholder="Passwort eingeben"
                value={password}
                onChange={(e) => setPassword(e.target.value)}
                required
              />
            </div>
            <button type="submit">Anmelden</button>
            <p className="switch-text">
              Noch kein Konto? <span onClick={toggleForm}>Registrieren</span>
            </p>
          </form>
        </div>

        {/* Register Formular */}
        <div className="form-panel register-panel">
          <h2>Registrieren</h2>
          {error && <p className="error">{error}</p>}
          <form onSubmit={handleRegister}>
            <div className="form-group">
              <label htmlFor="register-firstName">Vorname</label>
              <input
                type="text"
                id="register-firstName"
                placeholder="Vorname eingeben"
                value={firstname}
                onChange={(e) => setFirstName(e.target.value)}
                required
                />
            </div>
            <div className="form-group">
              <label htmlFor="register-lastName">Nachname</label>
              <input
                type="text"
                id="register-lastName"
                placeholder="Nachname eingeben"
                value={lastname}
                onChange={(e) => setLastName(e.target.value)}
                required
                />
            </div>
            <div className="form-group">
              <label htmlFor="register-email">E-Mail-Adresse</label>
              <input
                type="email"
                id="register-email"
                placeholder="E-Mail eingeben"
                value={email}
                onChange={(e) => setEmail(e.target.value)}
                required
              />
            </div>
            <div className="form-group">
              <label htmlFor="register-password">Passwort</label>
              <input
                type="password"
                id="register-password"
                placeholder="Passwort eingeben"
                value={password}
                onChange={(e) => setPassword(e.target.value)}
                required
              />
            </div>
            <div className="form-group">
              <label htmlFor="confirm-password">Passwort bestätigen</label>
              <input
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
              Bereits ein Konto? <span onClick={toggleForm}>Anmelden</span>
            </p>
          </form>
        </div>
      </div>
    </div>
  );
}

export default Login;
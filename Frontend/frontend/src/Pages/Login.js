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

  // Beispiel für Handling mit API Backend Aufruf
  const handleLogin = async (e) => {
    e.preventDefault();
    if (email === "" || password === "") {
      setError("Bitte alle Felder ausfüllen.");
      return;
    }
    try {
      const response = await fetch("http://127.0.0.1:8000/api/login/", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ email, password }),
      });
      const data = await response.text();
      if (!response.ok) {
        // throw new Error(data.message || "Fehler bei der Anmeldung");
        throw new Error(data.message);
      }

      // Speichere das Token (optional)
      // localStorage.setItem("token", data.token);

      // Weiterleitung zum Dashboard
      navigate("/home");
    } catch (error) {
      setError(error.message);
    }
  };

  // Handler für die Registrierung
  const handleRegister = () => {
    navigate("/register");
  };

  return (
    <div className="container login-mode">
      <div className="form-container">
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
              Noch kein Konto? <span onClick={handleRegister}>Registrieren</span>
            </p>
          </form>
        </div>
      </div>
    </div>
  );
}

export default Login;
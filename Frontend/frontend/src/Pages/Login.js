import React, { useState } from "react";
import { useNavigate } from "react-router-dom";
import "./Login.css"; // CSS-Datei für das Styling und Slide-Effekt

function Login() {
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [userid, setUserid] = useState("");
  const [isAuth, setIsAuth] = useState(Boolean);
  const [error, setError] = useState("");
  const navigate = useNavigate();

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
      const data = await response.json();
      if (!response.ok) {
        // throw new Error(data.message || "Fehler bei der Anmeldung");
        throw new Error(data.message);
      }
      else if (data.UserIsAuth===true) {
        setUserid(data.userid)
        localStorage.setItem("userid", userid);
        setIsAuth(data.UserIsAuth)
        localStorage.setItem("token", data.userIsAuth);
        // setError(data.message)
        navigate("/home");
      }
      else {
        // setError(data.message)
      }

      setError(data.message)

      // Speichere das Token (optional)
      // localStorage.setItem("token", data.token);

      
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
              <label className="login-label" htmlFor="login-email">E-Mail-Adresse</label>
              <input
                className="login-input"
                type="email"
                id="login-email"
                placeholder="E-Mail eingeben"
                value={email}
                onChange={(e) => setEmail(e.target.value)}
                required
              />
            </div>
            <div className="form-group">
              <label className="login-label" htmlFor="login-password">Passwort</label>
              <input 
                className="login-input"
                type="password"
                id="login-password"
                placeholder="Passwort eingeben"
                value={password}
                onChange={(e) => setPassword(e.target.value)}
                required
              />
            </div>
            <button className="login-button" type="submit">Anmelden</button>
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
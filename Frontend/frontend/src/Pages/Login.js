import React, { useState } from "react";
import { useNavigate } from "react-router-dom";
import "./Login.css"; // CSS-Datei für das Styling und Slide-Effekt
import SetAdminPPopup from "../Components/SetAdminPPopup";
import HandleForgotPwd from "../Components/handleForgotPwd"; // Popup für Passwort vergessen
import { getCsrfToken } from "../utils/csrf"; // Function for csrf
import { getBackEndDomain } from "../utils/backend-domain";

function Login() {
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [userid, setUserid] = useState("");
  const [isAuth, setIsAuth] = useState(Boolean);
  const [error, setError] = useState("");
  const navigate = useNavigate();
  const [PopupOpen, setPopupOpen] = useState(false);
  const [PopupForgotPwdOpen, setPopupForgotPwdOpen] = useState(false);

  // Beispiel für Handling mit API Backend Aufruf
  const handleLogin = async (e) => {
    e.preventDefault();
    if (email === "" || password === "") {
      setError("Bitte alle Felder ausfüllen.");
      return;
    }
    try {
      // Get CSRF-Token and cookie 
      const csrfToken = await getCsrfToken();
      const backEndDomain = await getBackEndDomain();
      const response = await fetch(backEndDomain + "/api/login/", { 
        method: "POST",
        headers: { 
          "Content-Type": "application/json",
          "X-CSRFToken": csrfToken, 
        },
        credentials: "include",
        body: JSON.stringify({ email, password }),
      });
      const data = await response.json();
      if (!response.ok) {
        // throw new Error(data.message || "Fehler bei der Anmeldung");
        setError(data.message);
        throw new Error(data.message);
      }
      else if (data.userid===-99) {
        setPopupOpen(true);
      }
      // else if (data.Role===1 || data.Role===2) {
      //   localStorage.setItem("DoRunUserid", data.userid);
      //   setIsAuth(data.UserIsAuth);
      //   localStorage.setItem("DoRunToken", data.userIsAuth);
      //   navigate("/admin");
      // }
      else if (data.UserIsAuth===true) {
        // setUserid(data.userid)
        // alert(data.userid);
        // alert(userid);
        // alert(data.Role);
        localStorage.setItem("DoRunRole", data.Role);
        localStorage.setItem("DoRunUserid", data.userid);
        setIsAuth(data.UserIsAuth)
        localStorage.setItem("DoRunToken", data.userIsAuth);
        // setError(data.message)
        navigate("/home");
      }
      else {
        // setError(data.message)
      }

      // setError(data.message)

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

  const handleForgorPwd = () => {
    setPopupForgotPwdOpen(true);
  }

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
            <p className="pwd-forget" onClick={handleForgorPwd}><span>Passwort vergessen?</span></p>
            <button className="login-button" type="submit">Anmelden</button>
            <p className="switch-text">
              Noch kein Konto? <span onClick={handleRegister}>Registrieren</span>
            </p>
          </form>
        </div>
      </div>
      <SetAdminPPopup
          isOpen={PopupOpen}
          onClose={() => setPopupOpen(false)}
          password={password}
          email={email}
        />
      <HandleForgotPwd
        isOpen={PopupForgotPwdOpen}
        onClose={() => setPopupForgotPwdOpen(false)}
        />
    </div>
  );
}

export default Login;
import './Impressum.css';
// import React from 'react';
import { useNavigate } from 'react-router-dom';



const Impressum = () => {
  const navigate = useNavigate();
  return (
    <div className="impressum-wrapper">
      <div className="impressum-container">
        <div className="impressum-header">
          <button onClick={() => navigate(-1)}>Zurück</button>
          <button onClick={() => navigate("/home")}>Home</button>
        </div>
        <h1>Impressum</h1>

        <h2>Kontakt</h2>
        <p>Tom Atolix</p>
        <p>Schlossalle 42b</p>
        <p>01099 Hodenhausen</p>
        <p>olix1999@gmail.com</p>

        <h2>Überschrift h2</h2>

        <h3>1. Abschnitt</h3>
        <p>
          Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. 
          Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. 
          Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. 
          Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.
        </p>

        <h3>2. Abschnitt</h3>
        <p>
          Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. 
          Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.
        </p>

        <h3>3. Abschnitt</h3>
        <p>
          Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. 
          Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.
          Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur.
          Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.
          Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.
        </p>
      </div>
    </div>
  );
};

export default Impressum;

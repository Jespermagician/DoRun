import React from "react";
import { Navigate } from "react-router-dom";

function ProtectedRoute({ children, role}) {
  const token = localStorage.getItem("DoRunToken"); // Prüfe Authentifizierung

  if (!token) {
    // Wenn kein Token, leite zur Login-Seite weiter
    return <Navigate to="/" />;
  }
  else if (role==="1" || role==="2") {
    return <Navigate to="/Admin" />
  }

  // Ansonsten zeige die geschützte Seite
  return children;
}

export default ProtectedRoute;

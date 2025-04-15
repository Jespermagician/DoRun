import React from "react";
import { Navigate } from "react-router-dom";
import Admin from './Pages/Admin';
import Dashboard from "./Pages/Dashboard";
import KmRecord from "./Pages/kmRecord";

function ProtectedRoute({ children}) {
  const token = localStorage.getItem("DoRunToken"); // Prüfe Authentifizierung
  const userRole = localStorage.getItem("DoRunRole");

  if (!token) {
    return <Navigate to="/" />;
  }
  else if (userRole==="1" || userRole==="2") {
    if (children.type === Admin) {
      return children;
    }
    else if (children.type === KmRecord) {
      return children;
    }
    else {
      return <Navigate to="/admin" />
    }
  }
  else if(userRole==="3") {
    if (children.type === Dashboard) {
      return children;
    }
    else {
      return <Navigate to="/home" />
    }
  }
  else {
    alert("Default");
    return <Navigate to="/" />;
  }

}

export default ProtectedRoute;

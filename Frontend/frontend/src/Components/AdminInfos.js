import React from "react";
import "./InfoField.css";

const AdminInfos = ({ user }) => {
  return (
    <div className="info-field">
      <h2 className="h2">Adminansicht</h2>
      <p>
        <strong>Admin-Name:</strong> {user.name}
      </p>
      <p>
        <strong>Admin-Email:</strong> {user.email}
      </p>
    </div>
  );
};

export default AdminInfos;

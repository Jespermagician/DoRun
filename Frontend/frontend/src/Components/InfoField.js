import React from "react";
import "./InfoField.css";

const InfoField = ({ user }) => {
  return (
    <div className="info-field">
      <h3>Benutzerinformationen</h3>
      <p>
        <strong>Name:</strong> {user.name}
      </p>
      <p>
        <strong>Email:</strong> {user.email}
      </p>
    </div>
  );
};

export default InfoField;

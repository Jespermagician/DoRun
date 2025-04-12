import React from "react";
import "./InfoField.css";

// Page header based on .\InfoField.css, but without information 

const PageHeader = ({ title }) => {
  return (
    <div className="info-field">
      <h1>{ title }</h1>
    </div>
  );
};

export default PageHeader;

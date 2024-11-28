import React from "react";
import "./StatsChart.css";

const StatsChart = ({ totalDonations }) => {
  return (
    <div className="stats-display">
      <h3>Gesamtspenden</h3>
      <div className="donations-amount">
        <span>{totalDonations} €</span>
      </div>
    </div>
  );
};

export default StatsChart;

import React from "react";
import "./StatsChart.css";

const StatsChart = ({ totalDonations }) => {
  return (
    <div>
      <h3 className="donation-Header">Gesamtspenden</h3>
      <div className="stats-display">
        <div className="donations-amount">
          <span>{totalDonations} €</span>
       </div>
      </div>
    </div>
  );
};

export default StatsChart;

import React, { useMemo } from "react";
import "./StatsChart.css";


const StatsChart = ({ totalDonations, totalKilometer, entries }) => {

  return (
    <div>
      <h3 className="donation-Header">Gesamtspenden / Kilometer</h3>
      <div className="stats-display">
        <div className="donations-amount">
          <span>{(totalDonations ?? 0).toFixed(2)} €</span>
          <br/>
          <span>{(totalKilometer ?? 0).toFixed(2)} km</span>
        </div>
      </div>
    </div>
  );
  
};


export default StatsChart;

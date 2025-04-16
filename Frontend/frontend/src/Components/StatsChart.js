import React from "react";
import "./StatsChart.css";

const StatsChart = ({ totalDonations, totalKilometer, entries }) => {
  const calcTotalMoneyPerKm = () => {
    let rate = 0;
    entries.forEach((entry) => {
      if (!entry.FixedAmount) {
        rate += entry.donation;
      }
    })
    return rate ? rate : 0;
};
  const calcTotalMoneyFixxed = () => {
    let rate = 0;
    entries.forEach((entry) => {
      if (entry.FixedAmount) {
        rate += entry.donation;
      }
    })
    return rate ? rate : 0;
};
  return (
    <div>
      <h3 className="donation-Header">Gesamtspenden</h3>
      <div className="stats-display">
        <div className="donations-amount">
          <span>{totalDonations ? totalDonations : 0} €</span> 
          <span> {totalKilometer ? totalKilometer : 0} km</span> 
          <hr/>
          {entries && <span> {calcTotalMoneyPerKm()} € pro KM</span>}
          <hr/>
          {entries && <span> {calcTotalMoneyFixxed()} € ab 1 km</span>}
       </div>
      </div>
    </div>
  )
};

export default StatsChart;

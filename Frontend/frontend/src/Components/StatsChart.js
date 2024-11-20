import React from 'react';
import { Line } from 'react-chartjs-2';
import { Chart as ChartJS, Title, Tooltip, Legend, CategoryScale, LinearScale, BarElement, LineElement, PointElement } from 'chart.js';

// Chart.js für die Liniencharts vorbereiten
ChartJS.register(
  Title,
  Tooltip,
  Legend,
  CategoryScale,
  LinearScale,
  BarElement,
  LineElement,
  PointElement
);

const StatsChart = () => {
  // Beispiel-Daten für das Diagramm
  const data = {
    labels: ['Jan', 'Feb', 'Mär', 'Apr', 'Mai', 'Jun', 'Jul'],
    datasets: [
      {
        label: 'Monatlicher Umsatz',
        data: [30, 45, 60, 70, 90, 120, 150],
        borderColor: 'rgba(75, 192, 192, 1)',
        backgroundColor: 'rgba(75, 192, 192, 0.2)',
        fill: true,
        tension: 0.4,
      },
    ],
  };

  const options = {
    responsive: true,
    plugins: {
      legend: {
        position: 'top',
      },
      title: {
        display: true,
        text: 'Monatliche Umsatzentwicklung',
      },
    },
  };

  return (
    <div className="stats-chart-container">
      <Line data={data} options={options} />
    </div>
  );
};

export default StatsChart;
import "./Dashboard.css";
import React, { useState } from 'react';
import { useNavigate } from "react-router-dom";
import StatsChart from '../Components/StatsChart';
import EntryList from '../Components/EntryList';
import InfoField from '../Components/InfoField';
import EntryFormModal from '../Components/EntryFormModal';

const Dashboard = () => {
    const [entries, setEntries] = useState([]);
    const [isModalOpen, setIsModalOpen] = useState(false); // Zustand für das Modal
  
    const addEntry = (entry) => {
      setEntries([...entries, entry]);
      setIsModalOpen(false); // Modal schließen nach dem Hinzufügen
    };
  
    const openModal = () => {
      setIsModalOpen(true); // Modal öffnen
    };
  
    const closeModal = () => {
      setIsModalOpen(false); // Modal schließen
    };
  
    return (
      <div className="dashboard-container">
        {/* Info-Feld oben */}
        <InfoField message="Neue Benachrichtigungen verfügbar!" />
  
        <div className="dashboard-body">
          <div className="left-side">
            {/* Diagramm mit Stats */}
            <StatsChart />
          </div>
          <div className="right-side">
            {/* Einträge Liste und Formular */}
            <EntryList entries={entries} openModal={openModal} />
          </div>
        </div>
  
        {/* Modal für Eintragsformular */}
        {isModalOpen && (
          <EntryFormModal closeModal={closeModal} addEntry={addEntry} />
        )}
      </div>
    );
  };
  
  export default Dashboard;
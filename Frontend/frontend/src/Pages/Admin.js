import "./Dashboard.css";
import React, { useState, useEffect } from 'react';
import { FaDoorOpen, FaMailBulk } from "react-icons/fa";
import { useNavigate } from "react-router-dom";
import StatsChart from '../Components/StatsChart';
import UserList from '../Components/UserList';
import InfoField from '../Components/InfoField';
import EntryFormModal from '../Components/EntryFormModal';
import AdminInfos from "../Components/AdminInfos";

const Admin = () => {
  const [entries, setEntries] = useState([]);
  const [modalOpen, setModalOpen] = useState(false);
  const [currentEntry, setCurrentEntry] = useState(null);
  const navigate = useNavigate();
  const [info, setInfo] = useState(null); // State für Info-Daten
  const [loading, setLoading] = useState(true); // State für Ladeanzeige
  const [error, setError] = useState(null); // State für Fehler

  const user = {name:"Jannik Schweitzer", email:"jannikschweitzer.js@gmail.com"};

  const handleLogOut = () => {
    navigate("/");
  };
  
  const handleAddEntry = () => {
    setCurrentEntry(null); // Kein aktueller Eintrag (Neuer Eintrag wird erstellt)
    setModalOpen(true); // Modal zum Hinzufügen eines Eintrags öffnen
  };

  return (
    <div>
      <div>
        <button className="logout-btn" onClick={handleLogOut}>
          {<FaDoorOpen/>}  Logout
        </button>
        <button className="sendmails-btn" >
          {<FaMailBulk/>} Send Donation Request
        </button>
      </div>
      <div className="dashboard-container">
        <div>
          <AdminInfos user={user}/>
        </div>
        <div className="content-section">
          {/* Infofeld für Gesamtspenden */}
          <div className="stats-section">
            <StatsChart totalDonations={entries.reduce((sum, entry) => sum + parseFloat(entry.donation || 0), 0)} />
          </div>

          {/* Eintragsliste */}
          <div className="entry-list-section">
            <UserList
              entries={entries}
              handleAddEntry={handleAddEntry}
              handleEditEntry={(entry) => {
                setCurrentEntry(entry); // Zu bearbeitenden Eintrag setzen
                setModalOpen(true); // Modal öffnen
              }}
              handleDeleteEntry={(id) => setEntries(entries.filter((entry) => entry.id !== id))}
            />
          </div>
        </div>
      </div>
    </div>
  );
};

export default Admin;
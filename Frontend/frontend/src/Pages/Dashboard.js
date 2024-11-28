import "./Dashboard.css";
import React, { useState } from 'react';
import { FaEdit, FaTrash, FaDoorOpen } from "react-icons/fa";
import { useNavigate } from "react-router-dom";
import StatsChart from '../Components/StatsChart';
import EntryList from '../Components/EntryList';
import InfoField from '../Components/InfoField';
import EntryFormModal from '../Components/EntryFormModal';

const Dashboard = () => {
  const [entries, setEntries] = useState([]);
  const [modalOpen, setModalOpen] = useState(false);
  const [currentEntry, setCurrentEntry] = useState(null);
  const navigate = useNavigate();

  const user = {name:"Jannik", email:"jannikschweitzer.js@gmail.com"};

  const handleLogOut = () => {
    navigate("/");
  };
  
  const handleAddEntry = () => {
    setCurrentEntry(null); // Kein aktueller Eintrag (Neuer Eintrag wird erstellt)
    setModalOpen(true); // Modal zum Hinzufügen eines Eintrags öffnen
  };

  const handleModalSubmit = (newEntry) => {
    if (currentEntry) {
      // Bearbeiteten Eintrag aktualisieren
      setEntries(
        entries.map((entry) =>
          entry.id === currentEntry.id ? { ...entry, ...newEntry } : entry
        )
      );
    } else {
      // Neuen Eintrag hinzufügen
      setEntries([...entries, { id: Date.now(), ...newEntry }]);
    }
    setModalOpen(false); // Modal schließen
  };

  return (
    <div>
      <div>
        <button className="logout-btn" onClick={handleLogOut}>
          {<FaDoorOpen/>}  Logout
        </button>
      </div>
      <div className="dashboard-container">
        <div>
          <InfoField user={user}/>
        </div>
        <div className="content-section">
          {/* Infofeld für Gesamtspenden */}
          <div className="stats-section">
            <StatsChart totalDonations={entries.reduce((sum, entry) => sum + parseFloat(entry.amount || 0), 0)} />
          </div>

          {/* Eintragsliste */}
          <div className="entry-list-section">
            <EntryList
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
        
        {/* Formular Modal zum Bearbeiten/Hinzufügen von Einträgen */}
        <EntryFormModal
          isOpen={modalOpen}
          onClose={() => setModalOpen(false)}
          onSubmit={handleModalSubmit}
          initialData={currentEntry}
        />
      </div>
    </div>
  );
};

export default Dashboard;
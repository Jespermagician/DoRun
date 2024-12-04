import "./Dashboard.css";
import React, { useState, useEffect } from 'react';
import { FaDoorOpen } from "react-icons/fa";
import { useNavigate } from "react-router-dom";
import StatsChart from '../Components/StatsChart';
import EntryList from '../Components/EntryList';
import InfoField from '../Components/InfoField';
import EntryFormModal from '../Components/EntryFormModal';

const Dashboard = () => {
  const [entries, setEntries] = useState([]);
  const [modalOpen, setModalOpen] = useState(false);
  const [currentEntry, setCurrentEntry] = useState(null);
  const [userid, setUserid] = useState("");
  const navigate = useNavigate();
  const [info, setInfo] = useState(null); // State für Info-Daten
  const [loading, setLoading] = useState(true); // State für Ladeanzeige
  const [error, setError] = useState(null); // State für Fehler

  const user = {name:"Jannik Schweitzer", email:"jannikschweitzer.js@gmail.com"};

  // useEffect(() => {
  //   const fetchInfo = async () => {
  //     try {
  //       const response = await fetch('http://127.0.0.1:8000/api/home');
  //       if (!response.ok) {
  //         throw new Error(`HTTP-Error! Status: ${response.status}`);
  //       }
  //       const data = await response.json(); // Antwort in JSON umwandeln
  //       setInfo(data); // Daten speichern
  //       alert(data)
  //       setLoading(false); // Laden beendet
  //     } catch (err) {
  //       setError(err.message); // Fehler speichern
  //       setLoading(false);
  //     }
  //   };

  //   fetchInfo(); // Funktion aufrufen
  // }, []); // Leer, damit der Effekt nur einmal ausgeführt wird

  // if (loading) return <div>Lade Info...</div>; // Ladeanzeige
  // if (error) return <div>Fehler: {error}</div>; // Fehleranzeige

  useEffect(() => {
    setUserid(localStorage.getItem("userid"));
    const handleUserInfos = async (e) => {
      try {
        const response = await fetch("http://127.0.0.1:8000/api/home", { 
          method: "POST",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify({ userid }),
        });
        const data = await response.json();
        if (!response.ok) {
          // throw new Error(data.message || "Fehler bei der Anmeldung");
          throw new Error(data.message);
        }
  
        // Speichere das Token (optional)
        // localStorage.setItem("token", data.token);
  
        // Weiterleitung zum Dashboard
        // navigate("/home");
      } catch (error) {
        // setError(error.message);
      }
    };

    handleUserInfos();
  }, []);


  // const user = {name:info.firstname, email:"jannikschweitzer.js@gmail.com"};

  const handleLogOut = () => {
    localStorage.removeItem("token")
    navigate("/");
  };
  
  const handleAddEntry = () => {
    setCurrentEntry(null); // Kein aktueller Eintrag (Neuer Eintrag wird erstellt)
    setModalOpen(true); // Modal zum Hinzufügen eines Eintrags öffnen
  };

  const handleModalSubmit = (newEntry) => {
    if (currentEntry) {
      // Bearbeiteten Eintrag aktualisieren
      // alert(currentEntry.id);
      setEntries(
        entries.map((entry) =>
          entry.id === currentEntry.id ? { ...entry, ...newEntry } : entry
        )
      );
    } else {
      // Neuen Eintrag hinzufügen
      // alert(currentEntry);
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
            <StatsChart totalDonations={entries.reduce((sum, entry) => sum + parseFloat(entry.donation || 0), 0)} />
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
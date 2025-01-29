import "./Dashboard.css";
import React, { useState, useEffect } from 'react';
import { FaDoorOpen } from "react-icons/fa";
import { useNavigate } from "react-router-dom";
import StatsChart from '../Components/StatsChart';
import EntryList from '../Components/EntryList';
import InfoField from '../Components/InfoField';
import EntryFormModal from '../Components/EntryFormModal';
import { getCsrfToken } from "../utils/csrf"; // Function for csrf

const Dashboard = () => {
  const [entries, setEntries] = useState([]);
  const [modalOpen, setModalOpen] = useState(false);
  const [currentEntry, setCurrentEntry] = useState(null);
  const [userid, setUserid] = useState(Number);
  const navigate = useNavigate();
  const [info, setInfo] = useState(null); // State für Info-Daten
  const [loading, setLoading] = useState(true); // State für Ladeanzeige
  const [error, setError] = useState(null); // State für Fehler
  const [user, setUser] = useState({});
  const [totalDonations, setTotalDonations] = useState(Number);
  const [donoid, setDonoid] = useState(null);

  let isFetched = false;

  useEffect(() => {
    setEntries([]);
    // setUserid(localStorage.getItem("userid"));
    var userid = localStorage.getItem("DoRunUserid");
    setUserid(userid);
    // alert(userid);
    const handleUserInfos = async (e) => {
      try {
        // Get CSRF-Token and cookie 
        const csrfToken = await getCsrfToken();

        const response = await fetch("http://127.0.0.1:8000/api/home", { 
          method: "POST",
          headers: { 
            "Content-Type": "application/json",
            "X-CSRFToken": csrfToken,
          },
          credentials: "include",
          body: JSON.stringify({userid}),
        });
        const data = await response.json();
        if (!response.ok) {
          // throw new Error(data.message || "Fehler bei der Anmeldung");
          throw new Error("Fehler beim erhalten der User Daten!");
        }
        // alert(data.entries[0].UserFirstname);
        setUser({name:(data.entries[0].UserFirstname + " " + data.entries[0].UserLastname), email:data.entries[0].UserEmail});
        setTotalDonations(data.totalDonations);
        if (data.entries.length === 1) {
          // alert("Nur der User Eintrag ist vorhanden!")
        }
        else {
          const remainingEntries = data.entries.slice(1);
          setEntries((prevEntries) => [
            ...prevEntries,
            ...remainingEntries.map((entry) => ({ id: entry.email, ...entry })),
          ]);
        }
        // alert(data.totalDonations);
        // alert(totalDonations);
        // Speichere das Token (optional)
        // localStorage.setItem("token", data.token);
  
        // Weiterleitung zum Dashboard
        // navigate("/home");
      } catch (error) {
        // setError(error.message);
      }
    };

    if (!isFetched) {
      handleUserInfos();
      isFetched = true;
    }
  }, []);


  // const user = {name:data.firstname, email:"jannikschweitzer.js@gmail.com"};

  const handleLogOut = () => {
    localStorage.removeItem("DoRunToken")
    localStorage.removeItem("DoRunUserid");
    localStorage.removeItem("DoRunRole")
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

  const handleAddAndEditDonoEntries = async (updatedEntries) => {
    try {
      const response = await fetch("http://127.0.0.1:8000/api/UpdateDonations", { 
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(updatedEntries),
      });
      // const data = await response.json();
      if (!response.ok) {
        // throw new Error(data.message || "Fehler bei der Anmeldung");
        // throw new Error(data.message);
        return
      }
    } catch (error) {
      setError(error.message);
    }
  };

  const handleModalSubmit2 = (newEntry) => {
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
      alert(newEntry.firstname);
      setEntries([...entries, { id: userid, ...newEntry }]);
      alert(entries.firstname);
      handleAddAndEditDonoEntries();
    }
    setModalOpen(false); // Modal schließen
  }

  const handleModalSubmit3 = (newEntry) => {
    if (currentEntry) {
      // Bearbeiteten Eintrag aktualisieren
      setEntries((prevEntries) =>
        prevEntries.map((entry) =>
          entry.donoid === currentEntry.donoid ? { ...entry, ...newEntry } : entry
        )
      );
    } else {
      // Neuen Eintrag hinzufügen
      setDonoid(null);
      setEntries((prevEntries) => {
        const updatedEntries = [...prevEntries, { Userid: userid, DonoID: donoid, ...newEntry }];
        handleAddAndEditDonoEntries(updatedEntries); // Hier auf aktuellen Stand zugreifen
        return updatedEntries;
      });
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
            {/* <StatsChart totalDonations={totalDonations} /> */}
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
          onSubmit={handleModalSubmit3}
          initialData={currentEntry}
        />
      </div>
    </div>
  );
};

export default Dashboard;
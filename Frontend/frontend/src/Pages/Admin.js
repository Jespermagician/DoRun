import "./Dashboard.css";
import React, { useState, useEffect } from 'react';
import { FaDoorOpen, FaMailBulk } from "react-icons/fa";
import { useNavigate } from "react-router-dom";
import StatsChart from '../Components/StatsChart';
import UserList from '../Components/UserList';
import AdminInfos from "../Components/AdminInfos";

const Admin = () => {
  const [entries, setEntries] = useState([]);
  const [modalOpen, setModalOpen] = useState(false);
  const [currentEntry, setCurrentEntry] = useState(null);
  const navigate = useNavigate();
  const [info, setInfo] = useState(null); // State für Info-Daten
  const [loading, setLoading] = useState(true); // State für Ladeanzeige
  const [error, setError] = useState(null); // State für Fehler
  const [user, setUser] = useState({});
  const [roleid, setRoleid] = useState({});
  const [kilometers, setKilometers] = useState({});

  let isFetched = false;
  var userid = localStorage.getItem("DoRunUserid");

  useEffect(() => {
    setEntries([]);
    // setUserid(localStorage.getItem("userid"));
    // var userid = localStorage.getItem("DoRunUserId");
    // alert(userid);
    const handleAdminInfos = async (e) => {
      try {
        const response = await fetch("http://127.0.0.1:8000/api/adminhome", { 
          method: "POST",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify({userid}),
        });
        const data = await response.json();
        if (!response.ok) {
          // throw new Error(data.message || "Fehler bei der Anmeldung");
          throw new Error("Fehler beim erhalten der User Daten!");
        }
        // alert(data.entries[0].UserFirstname);
        setUser({name:(data.entries[0].UserFirstname + " " + data.entries[0].UserLastname), email:data.entries[0].UserEmail});
        // setTotalDonations(data.totalDonations);
        if (data.entries.length === 1) {
          alert("Nur der User Eintrag ist vorhanden!")
        }
        else {
          const remainingEntries = data.entries.slice(1);
          setEntries((prevEntries) => [
            ...prevEntries,
            ...remainingEntries.map((entry) => ({ id: entry.userid, ...entry })),
          ]);
        }
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
      handleAdminInfos();
      isFetched = true;
    }
    // handleAdminInfos();
  }, []);

  const handleUserMails = async (e) => {
    // e.preventDefault();
    try {
      const response = await fetch("http://127.0.0.1:8000/mail/runinfo", { 
        method: "POST",
        headers: { "Content-Type": "application/json" },
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

  const handleDonatorMails = async (e) => {
    // e.preventDefault();
    try {
      const response = await fetch("http://127.0.0.1:8000/mail/sponinfo", { 
        method: "POST",
        headers: { "Content-Type": "application/json" },
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

  const handleSendMails = () => {
    handleUserMails();
    handleDonatorMails();
  }

  const handleUserEntriesChange = async (e) => {
    try {
      const response = await fetch("http://127.0.0.1:8000/api/UpdateUsers", { 
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({userid, roleid, kilometers}),
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

  return (
    <div>
      <div>
        <button className="logout-btn" onClick={handleLogOut}>
          {<FaDoorOpen/>}  Logout
        </button>
        <button className="sendmails-btn" onClick={handleSendMails}>
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
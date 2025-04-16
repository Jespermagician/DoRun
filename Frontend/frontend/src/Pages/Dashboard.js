import "./Dashboard.css";
import React, { useState, useEffect } from 'react';
import { FaDoorOpen } from "react-icons/fa";
import { CiSettings } from "react-icons/ci";
import { useNavigate } from "react-router-dom";
import StatsChart from '../Components/StatsChart';
import EntryList from '../Components/EntryList';
import InfoField from '../Components/InfoField';
import InfoPopUp from "../Components/infoPopUp";
import EntryFormModal from '../Components/EntryFormModal';
import { getCsrfToken } from "../utils/csrf"; // Function for csrf
import { getBackEndDomain } from "../utils/backend-domain";

const Dashboard = () => {
  const [entries, setEntries] = useState([]);
  const [modalOpen, setModalOpen] = useState(false);
  const [currentEntry, setCurrentEntry] = useState(null);
  const [userid, setUserid] = useState(0);
  const navigate = useNavigate();
  const [info, setInfo] = useState(null); // State für Info-Daten
  const [loading, setLoading] = useState(true); // State für Ladeanzeige
  const [error, setError] = useState(null); // State für Fehler
  const [user, setUser] = useState({});
  const [userData, setUserData] = useState({});
  // const [totalDonations, setTotalDonations] = useState(Number);
  const [donoid, setDonoid] = useState(null);
  const [infoPopUpdOpen, setInfoPopUpdOpen] = useState(false); // State für Info-Feld
  const [infoPopUpMessage, setInfoPopUpMessage] = useState(""); // State für Info-Feld-Nachricht
  // const [newEntry, setNewEntry] = useState([])

  let isFetched = false;

  useEffect(() => {
    const initFetech = async () => {
      setEntries([]);
      const id = parseInt(localStorage.getItem("DoRunUserid"))
      console.log("userid is: ", id);
      setUserid(id);
      await handleUserInfos(id); // Falls handleUserInfos async ist
    }

    if (!isFetched) {
      initFetech();
      isFetched = true;
    }
  
  }, []);

  const handleUserInfos = async (pUserid) => {
    try {
      // Get CSRF-Token and cookie 
      const csrfToken = await getCsrfToken();
      const backEndDomain = await getBackEndDomain();
      console.log("userids asdasdis: ", pUserid);
      const response = await fetch(backEndDomain + "/api/home", { 
        method: "POST",
        headers: { 
          "Content-Type": "application/json",
          "X-CSRFToken": csrfToken,
        },
        credentials: "include",
        body: JSON.stringify({userid: pUserid}),
      });
      const data = await response.json();
      if (!response.ok) {
        // throw new Error(data.message || "Fehler bei der Anmeldung");
        throw new Error("Fehler beim erhalten der User Daten!");
      }
      // alert(data.entries[0].UserFirstname);
      setUserData(data.entries[0]);
      setUser({name:(data.entries[0].UserFirstname + " " + data.entries[0].UserLastname), email:data.entries[0].UserEmail});
      // setTotalDonations(data.totalDonations);
      if (data.entries.length === 1) {
        // alert("Nur der User Eintrag ist vorhanden!")
      }
      else {
        const remainingEntries = data.entries.slice(1); 
        setEntries(() => [
          ...remainingEntries.map((entry) => ({
              id: entry.email, 
              donation: parseFloat(entry.donation),
              firstname: entry.firstname,
              lastname: entry.lastname,
              email: entry.email,
              donoid: parseInt(entry.donoid),
              verified: Boolean(entry.verified),
              FixedAmount: Boolean(entry.fixedamount),
              createdat: entry.createdat,
              housenr: entry.housenr,
              street: entry.street,
              postcode: entry.postcode
            })),
          ]);
          console.log("Entries: ", entries);
      }
    } catch (error) {
      // setError(error.message);;
    }
  };


  // const user = {name:data.firstname, email:"jannikschweitzer.js@gmail.com"};

  const handleLogOut = () => {
    localStorage.removeItem("DoRunToken")
    localStorage.removeItem("DoRunUserid");
    localStorage.removeItem("DoRunRole")
    navigate("/");
  };
  const openSettings = () => {
    navigate("/user-settings"); 
  }
  
  const handleAddEntry = () => {
    setCurrentEntry(null); // Kein aktueller Eintrag (Neuer Eintrag wird erstellt)
    setModalOpen(true); // Modal zum Hinzufügen eines Eintrags öffnen
  };

  const handleAddAndEditDonoEntries = async (updatedEntries, email) => {
    try {
      const csrfToken = await getCsrfToken();
      const backEndDomain = await getBackEndDomain();
      const response = await fetch(backEndDomain + "/api/UpdateDonations", { 
        method: "POST",
        headers: { 
          "Content-Type": "application/json",
          "X-CSRFToken": csrfToken,
        },
        credentials: "include",
        body: JSON.stringify(updatedEntries),
      });
      // const data = await response.json();
      if (!response.ok) {
        return
      }
      setInfoPopUpMessage(`E-Mail wurde an ${email} versendet, um den Eintrag zu verifizieren`)
      setInfoPopUpdOpen(true)
      await handleUserInfos(userid);
    } catch (error) {
      setError(error.message);
    }
  };

  const handleModalSubmit = (newEntry) => {
    console.log("current entry " + currentEntry)
    const frontendDomain = window.location.host;
    if (currentEntry) {
      
      console.log("new entry hier: " + newEntry)
      console.log("new entry hier:DonoAmount: " + newEntry.DonoAmount)

      const updatedEntries = [
        { Userid: userid, 
          ...newEntry,
          verified: false,
          frontendDomain: frontendDomain, 
        }
      ];
      handleAddAndEditDonoEntries(updatedEntries, newEntry.email);
    } else {
      // Neuen Eintrag hinzufügen
      setDonoid(null);
      setEntries((prevEntries) => {
        // prevEntries gives errors and is shit 
        const updatedEntries = [{ Userid: userid, DonoID: donoid, ...newEntry, frontendDomain: frontendDomain, }];
        handleAddAndEditDonoEntries(updatedEntries, newEntry.email); // Hier auf aktuellen Stand zugreifen
        
        return updatedEntries;
      });
    }
    setModalOpen(false); // Modal schließen
  };

  const handleDeleteEntry = async (newEntryID) => {
    try {
      const csrfToken = await getCsrfToken();
      const backEndDomain = await getBackEndDomain();
      const response = await fetch(backEndDomain + "/api/DelDonoRec", { 
        method: "POST",
        headers: { 
          "Content-Type": "application/json",
          "X-CSRFToken": csrfToken,
        },
        credentials: "include",
        body: JSON.stringify([{donoid: newEntryID}]),
      });
      
      if (!response.ok) {
        return
      }
      handleUserInfos(userid);
    } catch (error) {
      setError(error.message);
    }
  };

  return (
    <div>
      <div>
        <button className="logout-btn" onClick={handleLogOut}>
          {<FaDoorOpen/>}  Logout
        </button>
        <button className="sendmails-btn " onClick={openSettings}>
          {<CiSettings/>} 
        </button>
      </div>
      <div className="dashboard-container">
        <div>
          <InfoField user={user}/>
        </div>
        <div className="content-section">
          {/* Infofeld für Gesamtspenden */}
          <div className="stats-section">
            {/* <StatsChart totalDonations={entries.reduce((sum, entry) => sum + parseFloat(entry.donation || 0), 0)} /> */}
            <StatsChart totalDonations={userData.totalDonations} totalKilometer={userData.totalKilometer} entries={entries}/>
            {/* <StatsChart totalDonations={totalDonations} /> */}
          </div>

          {/* Eintragsliste */}
          <div className="entry-list-section">
            <EntryList
              entries={entries}
              handleAddEntry={handleAddEntry}
              handleEditEntry={(entry) => {
                const temp = {
                  firstname: entry.firstname,
                  lastname: entry.lastname,
                  email: entry.email,
                  street: entry.street,
                  houseNr: entry.housenr,
                  Plz: entry.postcode,
                  DonoAmount: entry.donation,
                  FixedAmount: entry.FixedAmount,
                  DonoID: entry.donoid
                }
                console.log("emrty temp: ", temp);
                setCurrentEntry(temp); // Zu bearbeitenden Eintrag setzen
                setModalOpen(true); // Modal öffnen
              }}
              handleDeleteEntryApi={(donId) => handleDeleteEntry(donId)}
              iduser={userid}
            />
          </div>
        </div>
        
        {/* Formular Modal zum Bearbeiten/Hinzufügen von Einträgen */}
        <EntryFormModal
          isOpen={modalOpen}
          onClose={() => setModalOpen(false)}
          onSubmit={(_newEntry) => {
            console.log("_newEntry")
            console.log(_newEntry)
            handleModalSubmit(_newEntry)
          }}
          initialData={currentEntry}
        />
        <InfoPopUp
          isOpen={infoPopUpdOpen}
          onClose={() => {
            setInfoPopUpdOpen(false)}
          }
          message={infoPopUpMessage} />
      </div>
    </div>
  );
};

export default Dashboard;
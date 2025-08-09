import React, { useState, useEffect, useMemo }  from "react";
import PerfectScrollbar from "react-perfect-scrollbar";
import { FaEdit, FaTrash} from "react-icons/fa";
import { MdMailOutline } from "react-icons/md";
import { FaCircleInfo } from "react-icons/fa6";
import { IoRefreshOutline } from "react-icons/io5";
import "react-perfect-scrollbar/dist/css/styles.css";
import { getCsrfToken } from "../utils/csrf";
import "./EntryList.css";
import InfoPopUp from "../Components/infoPopUp";
import { getBackEndDomain } from "../utils/backend-domain";
import ChoicePopUp from "../Components/ChoicePopUp"
import { useNavigate } from "react-router-dom";

const EntryList = ({ entries, handleEditEntry, handleDeleteEntryApi, handleAddEntry, iduser }) => {
  const [cooldown, setCooldown] = useState({});
  const [infoPopUpdOpen, setInfoPopUpdOpen] = useState(false); // State für Info-Feld
  const [infoPopUpMessage, setInfoPopUpMessage] = useState(""); // State für Info-Feld-Nachricht
  const [confirmDeleteOpen, setconfirmDeleteOpen] = useState(false);
  const [choosenDelEntry, setChoosenDelEntry] = useState({});
  const navigate = useNavigate();

  const handleRemind = async (entry) => {
    setCooldown(prev => ({
      ...prev,
      [entry.donoid]: Date.now() + 120000
    }));

    try {
      const csrfToken = await getCsrfToken();
      const backEndDomain = await getBackEndDomain();
      const domain = window.location.host;
      const response = await fetch(`${backEndDomain}/mail/sendmail/don/${iduser}/${entry.donoid}/${domain}`, {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
          "X-CSRFToken": csrfToken,
        },
        credentials: "include"
      });
      if (!response.ok) {
        throw new Error("Mail konnte nicht versendet werden");
      }
      // alert(`E-Mail an ${entry.firstname} ${entry.lastname} wurde versendet!`);
      setInfoPopUpMessage(`E-Mail an ${entry.firstname} ${entry.lastname} wurde versendet!`);
      setInfoPopUpdOpen(true);

    } catch (error) {
      console.error("Fehler beim Ändern des Passworts:", error);
      // setMessage hier NICHT nochmal nötig, weil es oben bereits gesetzt wurde
    }
  };

  const handleDelEntry = (entry) => {
    setChoosenDelEntry(entry);
    setconfirmDeleteOpen(true);
  }
  
  const isCooldownActive = (entryId) => {
    return !cooldown[entryId] || cooldown[entryId] < Date.now();
  };
  const isVerified = (verified) => {return verified ? "green-left" : "red-left"};

  const totalPerKm = useMemo(() => {
    let rate = 0;
    entries.forEach((entry) => {
      if (!entry.FixedAmount && entry.verified) {
        rate += entry.donation;
      }
    });
    return parseFloat(rate.toFixed(2)) || 0;
  }, [entries]);

  const totalFixed = useMemo(() => {
    let rate = 0;
    entries.forEach((entry) => {
      if (entry.FixedAmount && entry.verified) {
        rate += entry.donation;
      }
    });
    return parseFloat(rate.toFixed(2)) || 0;
  }, [entries]);

  return (
    <div className="entry-list-container">
      <h3>Sponsoreneinträge</h3>
      <li className="entry-info">
        <div className="entry-details">
          <span className="span-indent">Name</span>
          <span className="span-indent">Mail</span>
          <span className="span-indent">Spende</span>
          <span className="span-indent">Spendenart</span>
          <span className="span-indent">Verifiziert</span>
        </div>
      </li>

      <PerfectScrollbar>
        <ul className="entry-list">
          {entries.length === 0 ? (
            <li className="no-entries">
              <p>Keine Einträge vorhanden.</p>
            </li>
          ) : (
            entries.map((entry) => (
              <li key={entry.donoid} className={`entry-item ${isVerified(entry.verified)}`}>
                <div className="entry-details">
                  {/* <span className="span-indent">{entry.donoid}</span> */}
                  <span className="span-indent">{entry.firstname} {entry.lastname}</span>
                  <span className="span-indent">{entry.email}</span>
                  <span className="span-indent">{(entry.donation ?? 0).toFixed(2)} €</span>
                  <span className="span-indent">{entry.FixedAmount? "Festbetrag" : "Pro Kilometer"}</span>
                  <span className="span-indent">{entry.verified? "Ja": "Nein"}</span>
                </div>
                <div className="entry-actions">
                  {!entry.verified && isCooldownActive(entry.donoid) && (
                    <button className="edit-btn" onClick={() => handleRemind(entry)} title="Verifizierung neu senden">
                      <MdMailOutline />
                    </button>
                  )}
                  <button className="edit-btn"  title="Eintrag bearbeiten" onClick={() => handleEditEntry(entry)}><FaEdit/></button>
                  <button className="delete-btn" title="Eintrag löschen" onClick={() => handleDelEntry(entry)}><FaTrash/></button>
                </div>
              </li>
            ))
          )}
        </ul>
      </PerfectScrollbar>
      <li className="entry-info">
        <div className="entry-details">
          <span className="span-indent">Festbetrag Insgesamt: {totalFixed.toFixed(2)} €</span>
          <span className="span-indent">Pro KM Insgesamt: {totalPerKm.toFixed(2)} €</span>
          {!entries.every(entry => entry.verified) && (
            <span className="span-indent verify-message">Einträge müssen verifiziert werden!</span>
          )}
        </div>
      </li>
      <div className="button-format-dash">
        {/* Der Button bleibt immer sichtbar */}
        <button className="add-entry-btn" onClick={handleAddEntry}>
          Neuen Eintrag hinzufügen
        </button>
        <button className="extra-info-btn" onClick={() => navigate("/info")}>
          <FaCircleInfo />
        </button>
      </div>
      <InfoPopUp
      isOpen={infoPopUpdOpen}
      onClose={() => setInfoPopUpdOpen(false)}
      message={infoPopUpMessage} />
      <ChoicePopUp
        isOpen={confirmDeleteOpen}
        message={
          `Wollen Sie den Eintrag von ${choosenDelEntry.firstname} ${choosenDelEntry.lastname} löschen?`
        }
        onClose={(choice) => {
          if (choice) {
            handleDeleteEntryApi(choosenDelEntry.donoid);
          }
          setconfirmDeleteOpen(false)
        }}
      />
    </div>
  );
};

export default EntryList;
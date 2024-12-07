import React from "react";
import PerfectScrollbar from "react-perfect-scrollbar";
import { FaEdit, FaTrash} from "react-icons/fa";
import "react-perfect-scrollbar/dist/css/styles.css";
import "./EntryList.css";

const EntryList = ({ entries, handleEditEntry, handleDeleteEntry, handleAddEntry }) => {
  return (
    <div className="entry-list-container">
      <h3>Spendeneinträge</h3>
      <PerfectScrollbar>
        <ul className="entry-list">
          {entries.length === 0 ? (
            <li className="no-entries">
              <p>Keine Einträge vorhanden.</p>
            </li>
          ) : (
            entries.map((entry) => (
              <li key={entry.id} className="entry-item">
                <div className="entry-details">
                  <span className="span-indent">{entry.firstname} {entry.lastname}</span>
                  <span>{entry.email}</span>
                  <span>{entry.donation}€</span>
                  <span>{entry.fixedamount === true ? "Festbetrag" : "Pro Kilometer"}</span>
                </div>
                <div className="entry-actions">
                  <button className="edit-btn" onClick={() => handleEditEntry(entry)}><FaEdit/></button>
                  <button className="delete-btn" onClick={() => handleDeleteEntry(entry.id)}><FaTrash/></button>
                </div>
              </li>
            ))
          )}
        </ul>
      </PerfectScrollbar>
      {/* Der Button bleibt immer sichtbar */}
      <button className="add-entry-btn" onClick={handleAddEntry}>
        Neuen Eintrag hinzufügen
      </button>
    </div>
  );
};

export default EntryList;
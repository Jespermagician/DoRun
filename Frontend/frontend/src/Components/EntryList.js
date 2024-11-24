import React from 'react';
import './EntryList.css'; // EntryList Styles

const EntryList = ({ entries, openModal }) => {
  return (
    <div className="entry-list">
      <h3>Neue Einträge</h3>
      <button className="add-entry-button" onClick={openModal}>
        Neuer Eintrag
      </button>

      <ul>
        {entries.map((entry, index) => (
          <li key={index}>{entry.name}</li>
        ))}
      </ul>
    </div>
  );
};

export default EntryList;
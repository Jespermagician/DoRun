import "./Info.css";
import React from 'react';

const Info = () => {
  return (
    <div className="info-container-outer">
      <div className="info-container">
        <h1 className="title">🏃‍♂️ Hungerlauf 2025 am 24. Mai</h1>

        <p className="text-paragraph">
          Dieses Jahr findet der Hungerlauf <strong className="important-text">digital</strong> statt. 🌐
        </p>

        <p className="text-paragraph">
          Diese Webseite dient als dein digitaler <strong className="important-text">Laufzettel</strong> zur Anmeldung. ✅
        </p>

        <h2>Registrierung & Sponsor*innen</h2>
        <p className="text-paragraph">
          Du kannst dich hier anmelden und unter deinen Einträgen deine <strong className="important-text">Sponsor*innen</strong> hinzufügen. 💪
        </p>

        <p className="text-paragraph">
          Wichtige Info: Deine Sponsor*innen erhalten eine Bestätigungsmail, die sie bestätigen müssen. 
          Andernfalls werden die Einträge nicht berücksichtigt. 📧
        </p>

        <h2 className="subtitle">Spendenbescheinigungen</h2>
        <p className="text-paragraph">
          Falls deine Sponsor*innen eine <strong className="important-text">Spendenbescheinigung</strong> wünschen, musst du dies bei der Eingabe des Eintrags angeben. 
          Achte darauf, ihre <strong className="important-text">Adresse korrekt</strong> einzutragen. 🏠
        </p>

        <h2 className="subtitle">Anmeldung vor Ort</h2>
        <p className="text-paragraph">
          Die Anmeldung auf der Webseite ist <strong className="important-text">nicht automatisch</strong> für den Hungerlauf gültig. 
          Du musst am 24. Mai persönlich vorbeikommen, um dich zu registrieren und deine <strong className="important-text">Startnummer</strong> zu erhalten. 🎟️
        </p>

        <h2 className="subtitle">Kilometer sammeln</h2>
        <p className="text-paragraph">
          Du kannst dann deine <strong className="important-text">Kilometer</strong> laufen und am Ende bei der Anmeldung die gelaufenen Kilometer angeben. 
          Diese werden direkt in deinem Nutzerkonto vermerkt. 📊
        </p>

        <h2 className="subtitle">Nach dem Lauf</h2>
        <p className="text-paragraph">
          Nach dem Lauf erhältst du eine <strong className="important-text">Info-Mail</strong>, die dich über den Abschluss des Events informiert. 📩
        </p>

        <p className="text-paragraph">
          Auch deine Sponsor*innen bekommen eine E-Mail, in der sie direkt die <strong className="important-text">IBAN-Adresse</strong> finden und direkt an die Allianz Mission spenden können. 💸
        </p>

        <h2 className="subtitle">Viel Erfolg!</h2>
        <p className="text-paragraph">
          Wir freuen uns schon auf den Lauf und wünschen dir <strong className="important-text">viel Erfolg</strong>! ✨
        </p>

        <p className="text-paragraph">
          Dein Hungerlauf Team 🙌
        </p>
    </div>
    </div>
  );
};

export default Info;

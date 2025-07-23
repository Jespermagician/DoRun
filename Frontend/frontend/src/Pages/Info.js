import "./Info.css";
import React from 'react';
import { useNavigate } from 'react-router-dom';


const Info = () => {
  const navigate = useNavigate();
  return (
    <div className="info-wrapper-root">
      <div className="info-container-outer">
        <div className="info-container">
          <div className="back-btn-wrapper">
            <button className="btn-back-from-info" onClick={() => navigate(-1)}>Zurück</button>
          </div>          
          
          <h1 className="title">🏃‍♂️ Spendenlauf am 30. Februar 2026</h1>

          <p className="text-paragraph">
            Dieses Spendenlauf findet <strong className="important-text">digital</strong> statt. 🌐
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
            Auch deine Sponsor*innen bekommen eine E-Mail, in der sie direkt die <strong className="important-text">IBAN-Adresse</strong> finden und direkt spenden können. 💸
          </p>

          <h2 className="subtitle">Festbetrag / Pro Kilometer</h2>
          <p className="text-paragraph">
            Ein Sponsor kann zwischen einem <strong className="important-text">Festbetrag</strong>, welcher ab einem gelaufenem Kilometer gilt, oder einem Betrag <strong className="important-text">pro Kilometer</strong> wählen. 
            Dies wird bei der Eingabe des Eintrags über folgendem Button ausgewählt:
            <img src="button-don.png" alt="Festbetrag oder pro Kilometer" className="info-image" />
          </p>

          <h2 className="subtitle">Was mache ich wenn ein*e Sponsor*in keine E-Mail-Adresse besitzt?</h2>
          <p className="text-paragraph">
            Leider gibt es dafür keine extra Lösung. Im besten Fall musst du deine Eigene E-Mail-Adresse angeben und nach dem Lauf die Spende einsammeln bzw. den/die Sponsor*in informieren.
          </p>

          <h2 className="subtitle">Wichtig!</h2>
          <p className="text-paragraph">
            Beachten Sie bittem, dass Ihre Sponsor*innen die Einträge per E-Mail bestätigen!
          </p>

          <h2 className="subtitle">Viel Erfolg!</h2>
          <p className="text-paragraph">
            Wir freuen uns schon auf den Lauf und wünschen dir <strong className="important-text">viel Erfolg</strong>! ✨
          </p>

          
          <h2 className="subtitle">Weiteres</h2>
          <p className="text-paragraph">
            Mehr Informationen findest du auf der Webseite <a href="https://youtu.be/dQw4w9WgXcQ" target="_blank" rel="noopener noreferrer">dieser Domain</a>.
          </p>
          <br />
          <p className="text-paragraph">
            Bei weiteren Fragen kannst du dich gerne an <a href="mailto:test@Spendenlauf.de">test@test.de</a> wenden
          </p>
          
      </div>
      </div>
    </div>
  );
};

export default Info;

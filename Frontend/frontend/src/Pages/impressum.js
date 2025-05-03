import './Impressum.css';
import React from 'react';
import { useNavigate } from 'react-router-dom';



const Impressum = () => {
  const navigate = useNavigate();
  return (
    <div className="impressum-wrapper">
      <div className="impressum-container">
        <div className="impressum-header">
          <button onClick={() => navigate(-1)}>Zurück</button>
          <button onClick={() => navigate("/home")}>Home</button>
        </div>
        <h1>Impressum</h1>

        <h2>Kontakt</h2>
        <p>Ev. Jugend im Kirchenkreis Siegen-Wittgenstein</p>
        <p>Solidarraum 7b</p>
        <p>Ernst-August-Platz 3</p>
        <p>57271 Hilchenbach</p>
        <p>evjugend7@kirchenkreis-siwi.de</p>

        <h2>Verantwortlich für den Inhalt dieser Website:</h2>
        <p>Ev. Kirchenkreis Siegen-Wittgenstein</p>
        <p>Volker Peterek  & Susanne Lanatowitz</p>
        <p>Burgstr. 21</p>
        <p>57072 Siegen</p>
        <p>Tel.: 0271 / 5004 - 292</p>
        <p>E-Mail: volker.peterek@kirchenkreis-siwi.de</p>

        <h2>Verantwortlich für redaktionell-journalistische Inhalte gem. § 18 MStV:</h2>
        <p>Ev. Kirchenkreis Siegen-Wittgenstein</p>
        <p>Jugendbüro Solidarraum 7</p>
        <p>Manuela Halberstadt, Ulrike Ermisch</p>
        <p>Hermann-Manskopf-Weg 5</p>
        <p>57223 Kreuztal</p>
        <p>E-Mail: evjugend7@kirchenkreis-siwi.de</p>

        <h2>Rechtliche Hinweise</h2>

        <h3>1. Haftungsbeschränkung</h3>
        <p>
          Die Inhalte dieser Website werden mit größtmöglicher Sorgfalt erstellt. Der Anbieter übernimmt jedoch keine
          Gewähr für die Richtigkeit, Vollständigkeit und Aktualität der bereitgestellten Inhalte. Namentlich gekennzeichnete
          Beiträge geben die Meinung des jeweiligen Autors und nicht immer die Meinung des Anbieters wieder.
        </p>

        <h3>2. Externe Links</h3>
        <p>
          Diese Website enthält Verknüpfungen zu Websites Dritter ("externe Links"). Diese Websites unterliegen der Haftung
          der jeweiligen Betreiber. Der Anbieter hat bei der erstmaligen Verknüpfung der externen Links die fremden Inhalte
          daraufhin überprüft, ob etwaige Rechtsverstöße bestehen. Zu dem Zeitpunkt waren keine Rechtsverstöße ersichtlich.
          Der Anbieter hat keinerlei Einfluss auf die aktuelle und zukünftige Gestaltung und auf die Inhalte der
          verknüpften Seiten. Das Setzen von externen Links bedeutet nicht, dass sich der Anbieter die hinter dem Verweis
          oder Link liegenden Inhalte zu Eigen macht. Eine ständige Kontrolle der externen Links ist für den Anbieter ohne
          konkrete Hinweise auf Rechtsverstöße nicht zumutbar. Bei Kenntnis von Rechtsverstößen werden jedoch derartige
          externe Links unverzüglich gelöscht.
        </p>

        <h3>3. Urheber- und Leistungsschutzrechte</h3>
        <p>
          Die auf dieser Website veröffentlichten Inhalte unterliegen dem deutschen Urheber- und Leistungsschutzrecht. Jede
          vom deutschen Urheber- und Leistungsschutzrecht nicht zugelassene Verwertung bedarf der vorherigen schriftlichen
          Zustimmung des Anbieters oder jeweiligen Rechteinhabers. Dies gilt insbesondere für Vervielfältigung, Bearbeitung,
          Übersetzung, Einspeicherung, Verarbeitung bzw. Wiedergabe von Inhalten in Datenbanken oder anderen elektronischen
          Medien und Systemen. Inhalte und Rechte Dritter sind dabei als solche gekennzeichnet. Die unerlaubte
          Vervielfältigung oder Weitergabe einzelner Inhalte oder kompletter Seiten ist nicht gestattet und strafbar.
          Lediglich die Herstellung von Kopien und Downloads für den persönlichen, privaten und nicht kommerziellen Gebrauch
          ist erlaubt.
        </p>

        <h3>4. E-Mail-Kommunikation</h3>
        <p>
          Die Evangelische Kirche von Westfalen verwendet zur Zeit keine elektronische Verschlüsselung und keine
          elektronischen Signaturen. Wir weisen darauf hin, dass unverschlüsselte E-Mails über das Internet unter Umständen
          auch von Unbefugten gelesen werden können. Vertrauliche Mitteilungen oder Dokumente, die eine "besondere
          Schriftform" erfordern und/oder fristgebunden sind, dürfen deshalb nicht per E-Mail übermittelt werden. Bitte
          übermitteln Sie diese Dokumente per Post oder Telefax.
        </p>
        <p>
          Wenn Sie uns eine E-Mail senden, so wird Ihre E-Mail-Adresse nur für die Korrespondenz mit Ihnen verwendet.
        </p>

        <h3>5. Datenschutz</h3>
        <p>
          Die Verwendung der Kontaktdaten des Impressums zur gewerblichen Werbung ist ausdrücklich nicht erwünscht, es sei
          denn der Anbieter hatte zuvor seine schriftliche Einwilligung erteilt oder es besteht bereits eine
          Geschäftsbeziehung. Der Anbieter und alle auf dieser Website genannten Personen widersprechen hiermit jeder
          kommerziellen Verwendung und Weitergabe ihrer Daten.
        </p>
      </div>
    </div>
  );
};

export default Impressum;

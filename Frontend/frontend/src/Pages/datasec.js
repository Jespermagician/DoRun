import React from "react";
import "./Impressum.css"; // CSS-Datei für das Styling
import { useNavigate } from 'react-router-dom';

const DataPrivacy = () => {
    const navigate = useNavigate();
  return (
    <div className="impressum-wrapper">
      <div className="impressum-container">
        <div className="layout-20">
          <div className="layout-20-inner pt-3 pb-2 bg-c2 use-parallax">
            <div className="main-inner">
              <div className="area-20-1 s4">
                <div className="layout-2">
                  <div className="area-2-1 s3">
                  <div className="impressum-header">
                    {/* <button onClick={() => navigate(-1)}>Zurück</button> */}
                    <button onClick={() => navigate("/home")}>Home</button>
                    </div>
                    <h1 className="headline_1">Datenschutzerklärung</h1>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>

        <div className="layout-20">
          <div className="layout-20-inner mt-2 mb-4 use-parallax">
            <div className="main-inner">
              <div className="area-20-1 s4">
                <div className="template_box datenschutz_kk">
                  <div className="layout-2">
                    <div className="area-2-1 s3">
                      
                      <div class="area-2-1 s3"><div class="wysiwyg_1   "><p><a href="#DS100"><strong>Web-Datenschutzerklärung des Ev. Kirchenkreises Siegen-Wittgenstein</strong></a></p>
<ol>
<li><a href="#DS110">Umfang, Zweck und Rechtsgrundlage der Datenverarbeitung (§ 17 Abs. 1 Nr. 3 DSG-EKD)</a>
<ol style={{ "list-style-type": "lower-alpha;" }}>
<li><a href="#DS120">Besuch unserer Webseite</a></li>
<li><a href="#DS130">Protokollierung - Server-Logfiles</a></li>
<li><a href="#DS140">Cookies</a></li>
<li><a href="#DS150">Einbindung von Diensten zur statistischen Auswertung - Matomo</a></li>
<li><a href="#DS160">Open Street Map</a></li>
<li><a href="#DS170">Soziale Netzwerke</a><br /><a href="#DS180">Facebook und Instagram</a><br /><a href="#DS190">YouTube</a></li>
<li><a href="#DS200">Kontaktaufnahme</a></li>
<li><a href="#DS210">Stellenausschreibungen und Bewerbungsverfahren</a></li>
<li><a href="#DS220">Spenden</a></li>
</ol>
</li>
<li><a href="#DS230">Empfänger / Kategorien von Empfängern der personenbezogenen Daten (§ 17 Abs. 1 Nr. 4 DSG-EKD)</a></li>
<li><a href="#DS240">Dauer der Speicherung und Löschung personenbezogener Daten (§§ 17 Abs. 2 Nr. 1, 21 DSG-EKD)</a></li>
<li><a href="#DS250">Ihre Rechte als betroffene Person (§ 17 Abs. 2 Nr. 2 DSG-EKD)</a>
<ol style={{ "list-style-type": "lower-alpha;" }}>
<li><a href="#DS260">Recht auf Auskunft gem. § 19 DSG-EKD</a></li>
<li><a href="#DS270">Recht auf Berichtigung gem. § 20 DSG-EKD</a></li>
<li><a href="#DS280">Recht auf Löschung gem. § 21 DSG-EKD</a></li>
<li><a href="#DS290">Recht auf Einschränkung der Verarbeitung gem. § 22 DSG-EKD</a></li>
<li><a href="#DS300">Recht auf Widerspruch gegen die Verarbeitung gem. § 25 DSG-EKD</a></li>
<li><a href="#DS310">Recht auf Datenübertragbarkeit gem. § 24 DSG- EKD</a></li>
<li><a href="#DS320">Recht auf Widerruf einer erteilten Einwilligung zur Verarbeitung personenbezogener Daten gem. § 11 Abs. 3 DSG-EKD</a></li>
</ol>
</li>
<li><a href="#DS330">Verantwortliche Stelle (§ 17 Abs. 1 Nr. 1 DSG-EKD)</a></li>
<li><a href="#DS340">Unser örtlicher externer Datenschutzbeauftragter (§ 17 Abs. 1 Nr. 2 DSG-EKD)</a></li>
<li><a href="#DS350">Recht auf Beschwerde bei der zuständigen Aufsichtsbehörde (§ 17 Abs. 2 Nr. 3 DSG-EKD)</a></li>
<li><a href="#DS360">Sicherheit</a>
<ol style={{ "list-style-type": "lower-alpha;" }}>
<li><a href="#DS370">Technische und organisatorische Maßnahmen</a></li>
<li><a href="#DS380">E-Mail</a></li>
<li><a href="#DS390">TLS-Verschlüsselung (Transport Layer Security)</a></li>
</ol>
</li>
<li><a href="#DS400">Links zu anderen Webseiten</a></li>
<li><a href="#DS410">Begriffsbestimmungen</a><br /><a href="#DS420">Betroffene Person</a><br /><a href="#DS430">Verarbeitung</a><br /><a href="#DS440">Einschränkung der Verarbeitung</a><br /><a href="#DS450">Profiling</a><br /><a href="#DS460">Pseudonymisierung</a><br /><a href="#DS470">Verantwortlicher oder für die Verarbeitung Verantwortlicher</a><br /><a href="#DS480">Auftragsverarbeiter</a><br /><a href="#DS490">Empfänger</a><br /><a href="#DS500">Dritter</a><br /><a href="#DS510">Einwilligung</a></li>
<li><a href="#DS520">Schlussbestimmung</a></li>
</ol>
<p><br /><strong><a href="#DS530">Ev. Kirchenkreis Siegen-Wittgenstein - Datenschutzerklärung für Soziale Netzwerke</a></strong><br /><a href="#DS540"><strong>Informationspflichten bei der Erhebung personenbezogener Daten (§ 17 DSG-EKD)</strong></a></p>
<ol style={{ "list-style-type": "upper-roman" }}>
<li><a href="#DS550">Facebook und Instagram</a><br />
<ol>
<li><a href="#DS560">Verantwortliche Stelle (§ 17 Abs. 1 Nr. 1 DSG-EKD)</a></li>
<li><a href="#DS570">Datenschutzbeauftragter (§ 17 Abs. 1 Nr. 2 DSG-EKD)</a><br />
<ol style={{ "list-style-type": "lower-alpha;" }}>
<li><a href="#DS580">Örtlicher externer Datenschutzbeauftragter des Ev. Kirchenkreises Siegen-Wittgenstein</a></li>
<li><a href="#DS590">Datenschutzbeauftragter von Facebook Ireland</a></li>
</ol>
</li>
<li><a href="#DS600">Umfang, Zweck und Rechtsgrundlage der Datenverarbeitung (§ 17 Abs. 1 Nr. 3 und Nr. 4 DSG-EKD)</a><br />
<ol style={{ "list-style-type": "lower-alpha;" }}>
<li><a href="#DS610">Datenverarbeitung durch Facebook Ireland</a></li>
<li><a href="#DS620">Datenverarbeitung durch den Ev. Kirchenkreis Siegen-Wittgenstein</a></li>
<li><a href="#DS630">Datenverarbeitung durch den Ev. Kirchenkreis Siegen-Wittgenstein und Instagram/Facebook Ireland - Statistiken &amp; Seiten-Insights</a></li>
</ol>
</li>
<li><a href="#DS640">Ihre Rechte als betroffene Person (§ 17 Abs. 2 Nr. 2 und Nr. 3 DSG-EKD)</a></li>
<li><a href="#DS650">Recht auf Widerspruch gegen die Verarbeitung gem. § 25 DSG-EKD</a></li>
<li><a href="#DS660">Recht auf Beschwerde bei der zuständigen Aufsichtsbehörde gem. § 46 DSG-EKD</a></li>
</ol>
</li>
<li><a href="#DS670">YouTube</a><br />
<ol>
<li><a href="#DS680">Verantwortliche Stelle (§ 17 Abs. 1 Nr. 1 DSG-EKD)</a></li>
<li><a href="#DS690">Datenschutzbeauftragter (§ 17 Abs. 1 Nr. 2 DSG-EKD)</a><br />
<ol style={{ "list-style-type": "lower-alpha;" }}>
<li><a href="#DS700">Örtlicher externer Datenschutzbeauftragter des Ev. Kirchenkreises Siegen-Wittgenstein</a></li>
<li><a href="#DS710">Datenschutzbeauftragter von Google Ireland</a></li>
</ol>
</li>
<li><a href="#DS720">Umfang, Zweck und Rechtsgrundlage der Datenverarbeitung (§ 17 Abs. 1 Nr. 3 und Nr. 4 DSG-EKD)</a><br />
<ol style={{ "list-style-type": "lower-alpha;" }}>
<li><a href="#DS730">Datenverarbeitung durch Google Ireland</a></li>
<li><a href="#DS740">Datenverarbeitung durch den Ev. Kirchenkreis Siegen-Wittgenstein</a></li>
<li><a href="#DS750">Datenverarbeitung durch den Ev. Kirchenkreis Siegen-Wittgenstein und Google Ireland - YouTube Analytics &amp; Statistiken</a></li>
</ol>
</li>
<li><a href="#DS760">Ihre Rechte als betroffene Person (§ 17 Abs. 2 Nr. 2 und Nr. 3 DSG-EKD)</a></li>
<li><a href="#DS770">Recht auf Widerspruch gegen die Verarbeitung gem. § 25 DSG-EKD</a></li>
<li><a href="#DS780">Recht auf Beschwerde bei der zuständigen Aufsichtsbehörde gem. § 46 DSG-EKD</a></li>
</ol>
</li>
</ol>
<p>&nbsp;</p>
<p>&nbsp;</p>
<div class="hr_box">&nbsp;</div>
<p><strong><a id="DS100" name="DS100"></a>Web-Datenschutzerklärung des Ev. Kirchenkreises Siegen-Wittgenstein</strong></p>
<p>&nbsp;</p>
<p>Der Ev. Kirchenkreis Siegen-Wittgenstein nimmt als Betreiber dieser Seite den Schutz Ihrer personenbezogenen Daten sehr ernst. Wir behandeln Ihre Daten vertraulich und entsprechend der gesetzlichen Datenschutzvorschriften sowie dieser Datenschutzerklärung.</p>
<p>&nbsp;</p>
<p>Informationspflichten bei der Erhebung personenbezogener Daten (§ 17 DSG-EKD)</p>
<p>Für den Ev. Kirchenkreis Siegen-Wittgenstein als verantwortliche Stelle der Evangelischen Kirche gilt <u>nicht</u> die Europäische Datenschutz-Grundverordnung (EU DS-GVO<a href="#sdfootnote1sym" name="sdfootnote1anc"><sup>1</sup></a>), sondern ausschließlich Kirchenrecht (Art. 91 EU DS-GVO i.V.m. Art. 140 GG<a href="#sdfootnote2sym" name="sdfootnote2anc"><sup>2</sup></a>, Art. 137 Abs. 3 WRV<a href="#sdfootnote3sym" name="sdfootnote3anc"><sup>3</sup></a>, § 2 Abs. 1 DSG-EKD). In Folge dessen werden alle Daten nach den Vorgaben des Gesetzes über den Datenschutz der Evangelischen Kirche in Deutschland (DSG-EKD) verarbeitet. Das DSG-EKD baut auf den Vorgaben der Europäischen Datenschutz-Grundverordnung (EU DS-GVO) auf und ist am 24.05.2018 in Kraft getreten.</p>
<p>Außerdem gilt bezüglich der Speicherung von Informationen und bezüglich des Zugriffs auf Informationen in Endeinrichtungen z.B. mittels Cookies, seit dem 01.12.2021 das Telekommunikation Digitale Dienste Datenschutzgesetz (TDDDG). Das TDDDG dient dem Schutz der Privatsphäre und Vertraulichkeit bei der Nutzung von Endeinrichtungen, wie er durch Art. 7 der Grundrechte Charta gewährleistet wird, unabhängig davon, ob personenbezogene Daten verarbeitet werden.</p>
<p>Im Folgenden informieren wir sie nach den Vorgaben des § 17 DSG-EKD, wie wir im Rahmen der Nutzung unserer Webseite rechtskonform Ihre personenbezogenen Daten verarbeiten. Da wir alle Daten selbst erheben, kommt eine darüberhinausgehende Informationspflicht nach § 18 DSG-EKD in Bezug auf eine Datenerhebung mittels Dritter für uns nicht in Betracht.</p>
<p>&nbsp;</p>
<p><strong><a id="DS110" name="DS110"></a>1. Umfang, Zweck und Rechtsgrundlage der Datenverarbeitung<br />(§ 17 Abs. 1 Nr. 3 DSG-EKD)</strong></p>
<p><strong><a id="DS120" name="DS120"></a>a. Besuch unserer Webseite</strong></p>
<p>Mit unserer Webseite möchten wir über uns und unsere Tätigkeiten informieren. Im Zusammenhang mit unserer Webseite verarbeiten wir personenbezogene Daten grundsätzlich nur, soweit dies zur Bereitstellung, Nutzung und Optimierung unserer Webseite sowie zur Wahrung von kirchlichen und berechtigten Interessen erforderlich ist (§ 6 Nr. 4 i.V.m. Nr. 8 DSG-EKD). Darüber hinaus verarbeiten wir Ihre Daten im Zusammenhang mit unserer Webseite nur, soweit Rechtsvorschriften dies erlauben (§ 6 Nr. 1 DSG-EKD) oder Sie hierin ausdrücklich eingewilligt haben (§ 6 Nr. 2 DSG-EKD).</p>
<p>&nbsp;</p>
<p><strong><a id="DS130" name="DS130"></a>b. Protokollierung - Server-Logfiles</strong></p>
<p>Rechnerbezogene Daten werden zu Zwecken der Identifikation und Nachverfolgung unzulässiger Zugriffsversuche auf unsere Webserver protokolliert und gespeichert.</p>
<p>Um die Stabilität und Sicherheit zu gewährleisten werden auf dem Server automatisiert Protokolle (sog. Logfiles) erfasst. Alle Logfiles werden täglich rotiert, Logs vom Vortag werden archiviert und stehen für die jeweils genannte Vorhaltezeit zur Verfügung.</p>
<p>Webserver-Logfile<br />Enthält: Domain, IP, Anfragen, Useragent (clientseitige Anwendung, z.B. Browser), Timestamp (Datum und Uhrzeit des Zugriffs), Status Code (200 bedeutet OK, 404 bedeutet die aufgerufene Seite oder Datei kann nicht gefunden werden usw.)<br />Vorhaltezeit: 3 Tage</p>
<p>Die Speicherung der Protokolldaten erfolgt auf der Rechtsgrundlage von § 6 Nr. 4 i.V.m. Nr. 8 DSG-EKD. Diese Daten werden NUR im Falle eines unerlaubten Zugriffs ausgewertet. Die Auswertung erfolgt durch Mitarbeitende des Kirchenkreises sowie durch technische Dienstleister und Administratoren der Evangelischen Kirche von Westfalen.</p>
<p>&nbsp;</p>
<p><strong><a id="DS140" name="DS140"></a>c. Cookies</strong></p>
<p><a name="Bookmark"></a>Unsere Webseite verwendet Cookies. Cookies sind kleine Textdateien, die auf Ihrem Endgerät abgelegt werden und die Ihr Browser speichert. Sie richten auf Ihrem Endgerät keinen Schaden an und enthalten keine Viren. Cookies dienen dazu, unseren Webauftritt nutzerfreundlicher, effektiver und sicherer zu machen.</p>
<p>Die meisten der von uns verwendeten Cookies werden nur für die technische Auslieferung der Seiten verwendet und nach dem Ende Ihres Besuchs automatisch gelöscht. Andere Cookies bleiben auf Ihrem Endgerät gespeichert, bis Sie diese löschen. Diese Cookies ermöglichen es uns, Ihren Browser beim nächsten Besuch wiederzuerkennen.</p>
<p>Die meisten Browser sind so eingestellt, dass sie Cookies automatisch akzeptieren. Sie können Ihren Browser so einstellen, dass Sie über die Platzierung von Cookies informiert werden und Cookies nur im Einzelfall erlauben, die Annahme von Cookies für bestimmte Fälle oder generell ausschließen sowie das automatische Löschen von Cookies beim Schließen des Browsers aktivieren. So wird der Gebrauch von Cookies für Sie transparent.</p>
<p><a name="Bookmark1"></a>Technisch notwendige Cookies, die zum Betrieb bzw. zur Anzeige der Webseite unbedingt erforderlich sind, werden auf der Rechtsgrundlage von § 25 Abs. 2 Nr. 2 TDDDG gespeichert. Die Speicherung solcher Cookies erfolgt im Interesse einer technisch fehlerfreien und optimierten Bereitstellung unserer Webseite.</p>
<p>Alle anderen Cookies (z.B. solche zur Analyse Ihres Nutzerverhaltens) werden auf der Rechtsgrundlage von § 25 Abs. 1 TDDDG gespeichert, wenn Sie uns dazu Ihre Einwilligung erteilen. Beim Besuch unserer Webseite erscheint eine Opt-In-Checkbox, in der Sie Ihre Einwilligung zur Speicherung von Cookies erklären können. Ihre Einwilligung können Sie jederzeit mit Wirkung für die Zukunft widerrufen, indem Sie die Cookie-Einstellungen erneut aufrufen und dort die Opt-Out-Checkbox nutzen. Der Widerruf betrifft nur die zukünftige Speicherung von Cookies, nicht jedoch die - mit Ihrer Einwilligung - bereits gespeicherten Cookies. Diese müssen Sie selbst manuell oder über die automatische Browsereinstellung entfernen.</p>
<p>&nbsp;</p>
<p><strong><a id="DS150" name="DS150"></a>d. Einbindung von Diensten zur statistischen Auswertung - Matomo</strong></p>
<p>Die ständige Optimierung unserer Webseite liegt uns sehr am Herzen. Daher werden rechnerbezogene Daten gespeichert, um - anonymisiert - Trends zu verzeichnen, Zugriffsdaten auf unsere Webseite statistisch auszuwerten und bei der Entwicklung und Verbesserung unserer Webseite zu helfen. Wir nutzen dazu den Analysedienst "Matomo". Anbieter ist die InnoCraft Ltd., 150 Willis St, 6011 Wellington, New Zealand.</p>
<p>Unsere Webseite verwendet Matomo <u>ohne den Einsatz von Cookies</u> zur Analyse Ihres Nutzerverhaltens. Do-not-Track Unterstützung ist aktiviert. Wird unsere Webseite aufgerufen, so werden von Matomo folgende Daten erfasst:<br />Für die Analyse werden neben dem Zugriff auf die Seite und der anonymisierten IP-Adresse noch folgende Daten erfasst: Datum und Zeit der Anfrage, Seitentitel der aufgerufenen Seite, Bildschirmauflösung des Clientensystems, lokaler Zeitzone, URL der vorher aufgerufenen Seite (Referrer-URL), URL von angeklickten und heruntergeladenen Dateien, URL von angeklickten externen Domains, Geolocation des Clienten (Land, Region, Stadt), (Haupt-)Sprache des benutzen Browsers, User Agent des benutzten Browsers.</p>
<p>Ihre IP-Adresse wird unmittelbar nach der Erfassung mit Hilfe des von Matomo zur Verfügung gestellten Plugins "PrivacyManager" anonymisiert, indem ein oder mehrere Oktette maskiert werden. Mit der Anonymisierung handelt es sich bei Ihrer IP-Adresse nicht mehr um ein personenbezogenes Datum. Eine Zuordnung zum aufrufenden Rechner und eine Auswertung der IP-Adresse in Bezug auf den Nutzer ist durch die Anonymisierung nicht mehr möglich.</p>
<p>Der Einsatz von Matomo ohne Cookies erfolgt im Interesse einer technisch fehlerfreien und optimierten Bereitstellung unserer Webseite auf der Rechtsgrundlage von § 6 Nr. 4 i.V.m. Nr. 8 DSG-EKD. Sie können selbstverständlich der Analyse Ihres Nutzungsverhaltens widersprechen. Am Ende dieser Datenschutzerklärung finden Sie dazu eine Opt-Out-Möglichkeit, bitte klicken Sie dort den entsprechenden Button an.</p>
<p>Weitere Informationen und die geltenden Datenschutzbestimmungen von Innocraft bzw. Matomo können unter https://www.innocraft.com/privacy bzw. https://matomo.org/privacy-policy/ abgerufen werden.</p>
<p>&nbsp;</p></div>
<div class="wysiwyg_1   "><p>&nbsp;</p>
<p><strong><a id="DS160" name="DS160"></a>e. Open Street Map</strong></p>
<p>In unsere Webseiten sind Karten des Open-Source-Mapping-Werkzeugs "OpenStreetMap" (OSM) eingebunden (<a href="https://www.openstreetmap.org">https://www.openstreetmap.org</a>), die auf Grundlage der Open Database Lizenz (ODbL) durch die OpenStreetMap Foundation (OSMF, St John's Innovation Centre, Cowley Road, Cambridge, CB4 0WS, United Kingdom) angeboten werden.</p>
<p>Wenn Sie eine unserer Webseiten aufrufen, auf denen eine OpenStreetMap Karte eingebunden ist, werden von OpenStreetMap Datenverarbeitungsvorgänge in Gang gesetzt. Zu den verarbeiteten Daten zählen mindestens Ihre IP-Adresse und der verwendete Browser. Diese Informationen werden in der Regel an einen Server von OpenStreetMap übertragen und dort gespeichert. Wir haben keine weiteren Informationen und keinen Einfluss auf eine Verarbeitung Ihrer personenbezogenen Daten durch OpenStreetMap und darauf, dass der Anbieter die geltenden Datenschutzbestimmungen einhält. Mehr Informationen zum Umgang mit Nutzerdaten finden Sie in der Datenschutzerklärung der OSMF: <a href="https://wiki.osmfoundation.org/wiki/Privacy_Policy">https://wiki.osmfoundation.org/wiki/Privacy_Policy</a>.</p>
<p>Rechtsgrundlage für die mit der Einbettung von OpenStreetMap-Karten verbundene Datenverarbeitung ist eine von Ihnen erteilte Einwilligung gem. § 25 Abs. 1 TDDDG. OpenStreetMap verarbeitet Ihre Daten auch auf Servern im Ausland, z.B. in Frankreich und in Großbritannien.</p>
<p>In Frankreich und anderen EU-Ländern gilt - wie in Deutschland - die EU-Datenschutzgrundverordnung (DSGVO). Großbritannien ist am 31.01.2020 aus der EU ausgetreten.</p>
<p>Die EU-Kommission hat Großbritannien durch ein Angemessenheitsbeschluss gem. Art. 45 Abs. 3 DSGVO als sicheres Drittland eingestuft. Das Datenschutzniveau wurde als angemessen hoch von der EU-Kommission eingestuft, sodass ein Datentransfer zwischen der EU und Großbritannien auf der Grundlage von Art. 24 Abs. 1 DSGVO rechtmäßig erfolgen kann.</p>
<p>&nbsp;</p>
<p><strong><a id="DS170" name="DS170"></a>f. Soziale Netzwerke</strong></p>
<p><strong><a id="DS180" name="DS180"></a>Facebook und Instagram</strong></p>
<p>Zum Teilen von Seiten in sozialen Netzwerken wie Facebook und Instagram etc. bieten diese Unternehmen sog. Social Plugins an. Diese übertragen bereits beim Aufruf einer Seite, auf der ein solches Social Plugin eingebettet ist, Daten über das Nutzungsverhalten des jeweiligen Nutzers an die Betreiber der sozialen Netzwerke.</p>
<p>Aus diesem Grund verwenden wir auf unserer Webseite keine Social Plugins, sondern die von der Zeitschrift c't entwickelte datenschutzfreundlichen Shariff Social-Media-Buttons (<a href="https://www.heise.de/ct/artikel/Shariff-Social-Media-Buttons-mit-Datenschutz-2467514.html">https://www.heise.de/ct/artikel/Shariff-Social-Media-Buttons-mit-Datenschutz-2467514.html</a>). Damit werden Daten (unter anderem die Information, von welcher Webseite Sie zu Facebook oder Instagram gelangt sind und Ihre IP-Adresse) erst an die Betreiber der sozialen Netzwerke übertragen, wenn Sie als Nutzer auf die Schaltfläche zum Teilen klicken. Falls Sie in Ihrem Facebook- oder Instagram-Account eingeloggt sind, ermöglichen Sie Facebook, Ihr Nutzerverhalten direkt Ihrem persönlichen Profil zuzuordnen. Das können Sie verhindern, indem Sie sich aus Ihrem Facebook- oder Instagram-Account ausloggen. Weitere Informationen zum Datenschutz bei Facebook und Instagram finden Sie in den Datenrichtlinien und Cookie-Richtlinien von Facebook und Instagram unter: <a href="https://de-de.facebook.com/privacy/explanation">https://de-de.facebook.com/privacy/explanation</a>, <a href="https://help.instagram.com/519522125107875/?helpref=hc_fnav&amp;bc%5b0%5d=Instagram%20Help&amp;bc%5b1%5d=Privacy%20and%20Safety%20Center">https://help.instagram.com/519522125107875/?helpref=hc_fnav&amp;bc[0]=Instagram%20Help&amp;bc[1]=Privacy%20and%20Safety%20Center</a>, <a href="https://de-de.facebook.com/policies/cookies/">https://de-de.facebook.com/policies/cookies/</a>, <a href="https://help.instagram.com/1896641480634370">https://help.instagram.com/1896641480634370</a>.</p>
<p>Anbieter von Facebook und Instagram in Deutschland ist die Meta Platforms Ireland Limited, 4 Grand Canal Square, Grand Canal Harbour, Dublin 2, Ireland. Der Mutterkonzern von Meta Platforms ist die Meta Platforms Inc., 1 Hacker Way, Menlo Park, California 94025, USA. Daten und Informationen von Nutzern werden von Meta Platforms Ireland Limited in der EU und von Meta Platforms Inc. in Drittländern wie den USA verarbeitet. Mit Ihrer Einwilligung bzw. dem Klick auf die Shariff-Schaltfläche zum Teilen dokumentieren Sie, dass Sie mit einer Übertragung personenbezogener Daten an das gewählte soziale Netzwerk und damit auch mit einer Datenübertragung an Drittländer (außerhalb der EU) einverstanden sind. Rechtsgrundlage für diese Datenverarbeitung ist § 6 Nr. 2 bzw. § 10 Abs. 2 Nr. 1 DSG-EKD. Daneben sind auf unseren Webseiten Links zu Facebook vorhanden.</p>
<p>Weitere Informationen zur Verarbeitung personenbezogener Daten durch Facebook/Instagram und bzgl. der Datenverarbeitung beim Besuch unserer Facebook-Seite und unseres Instagram-Accounts finden Sie in unserer "Datenschutzerklärung für Soziale Netzwerke" <em>(Link).</em></p>
<p>&nbsp;</p>
<p><strong><a id="DS190" name="DS190"></a>YouTube</strong></p>
<p>Auf unserer Webseite sind Videos über den Anbieter YouTube integriert und Links zu YouTube-Videos angegeben. Die Videos wurden unter Nutzung des von YouTube angebotenen "erweiterten Datenschutzmodus" eingebettet. Laut dem Unternehmen selbst werden von YouTube dabei zunächst keine Cookies gespeichert, es sei denn, Sie sehen sich das Video an. Wenn Sie sich das Video ansehen, werden durch YouTube Cookies gespeichert und Datenverarbeitungsvorgänge in konkret unbekanntem Umfang in Gang gesetzt, sofern Sie dazu zuvor Ihre Einwilligung erteilt haben. YouTube ist wiederum mit dem Google DoubleClick-Netzwerk verbunden. Durch das Google DoubleClick-Netzwerk werden bereits Cookies gesetzt und Daten und Informationen verarbeitet, wenn Sie eine Webseite aufrufen, in der ein YouTube-Video eingebettet ist, sofern Sie dazu zuvor Ihre Einwilligung erteilt haben. Dies erfolgt unabhängig davon, ob Sie über ein YouTube-Nutzerkonto verfügen, in das Sie eingeloggt sind, oder ob kein Nutzerkonto besteht. Falls Sie in Ihrem YouTube-Account eingeloggt sind, ermöglichen Sie YouTube, Ihr Nutzerverhalten direkt Ihrem persönlichen Profil zuzuordnen. Das können Sie verhindern, indem Sie sich aus Ihrem YouTube-Account ausloggen. Weitere Informationen zum Datenschutz bei YouTube finden Sie in der Datenschutzerklärung von YouTube unter: <a href="https://www.google.de/intl/de/policies/privacy">https://www.google.de/intl/de/policies/privacy</a>.</p>
<p>Anbieter von YouTube ist die Google Ireland Limited, Gordon House, Barrow Street, Dublin 4, Irland. Der Mutterkonzern von YouTube ist die Google LLC, 1600 Amphitheatre Parkway, Mountain View, California 94043. Daten und Informationen von Nutzern werden von YouTube und Google in der EU und in Drittländern wie den USA verarbeitet. Rechtsgrundlage für die mit der Einbettung von YouTube-Videos verbundene Datenverarbeitung ist § 6 Nr. 2 DSG-EKD bzw. § 10 Abs. 2 Nr. 1 DSG-EKD. Mit Ihrer Einwilligung dokumentieren Sie, dass Sie mit einer übertragung personenbezogener Daten an YouTube und Google und damit auch mit einer Datenübertragung an Drittländer (außerhalb der EU) einverstanden sind. Daneben sind auf unseren Webseiten Links zu YouTube vorhanden.</p>
<p>Die Einwilligung in das Speichern und Auslesen von Informationen gemäß § 25 Abs. 1 TDDDG und die Einwilligung in die Verarbeitung von personenbezogenen Daten gemäß § 6 Nr. 2 DSG-EKD bzw. § 10 Abs. 2 Nr. 1 DSG-EKD kann durch dieselbe Handlung erteilt werden (Bündelung von Einwilligungen).</p>
<p>Weitere Informationen zur Datenverarbeitung durch YouTube/Google und bzgl. der Datenverarbeitung beim Besuch unseres YouTube-Kanals finden Sie in unserer "Datenschutzerklärung für Soziale Netzwerke" <em>(Link).</em></p>
<p>&nbsp;</p>
<p><strong><a id="DS200" name="DS200"></a>g. Kontaktaufnahme</strong></p>
<p><a name="Bookmark2"></a><a name="Bookmark3"></a>Wenn Sie uns kontaktieren möchten, nutzen Sie bitte die angegebenen Kontaktdaten. Nehmen Sie mit uns telefonisch, per E-Mail oder postalisch Kontakt auf, werden die von Ihnen dabei mitgeteilten personenbezogenen Daten (z.B. Ihr Name, Ihre E-Mail-Adresse / Telefonnummer / Adresse, das Datum der Kontaktaufnahme und der Inhalt der Nachricht, die Sie übermitteln) von uns gespeichert. Die Daten werden streng zweckgebunden ausschließlich zur Bearbeitung Ihrer Anfrage benutzt. Rechtsgrundlage für diese Datenverarbeitung ist § 6 Nr. 4 i.V.m. Nr. 8 DSG-EKD. Unser kirchliches / berechtigtes Interesse liegt hier darin, Ihre Anfragen und sonstigen Anliegen möglichst zeitnah, umfassend und zu Ihrer Zufriedenheit zu bearbeiten. Die Daten werden gelöscht, wenn der Zweck für die Verarbeitung entfällt, d. h. konkret, nachdem der Kontakt mit Ihnen endgültig beendet ist. Zwingende gesetzliche Aufbewahrungsfristen bleiben davon unberührt.</p>
<p>&nbsp;</p>
<p><strong><a id="DS210" name="DS210"></a>h. Stellenausschreibungen und Bewerbungsverfahren</strong></p>
<p>Der Ev. Kirchenkreis Siegen-Wittgenstein verarbeitet personenbezogene Daten von Bewerbern, die diese in Bewerbungen auf offene Stellen angeben. Der Zweck einer Bewerbung ist das Anstreben eines Beschäftigungsverhältnisses mit dem Ev. Kirchenkreis Siegen-Wittgenstein. Der Rechtsgrund für die damit verbundene Verarbeitung der Bewerberdaten ergibt sich aus § 49 Abs. 1 i.V.m. § 4 Nr. 20 lit. h) DSG-EKD. Ihre personenbezogenen Daten werden dabei vertraulich behandelt und ausschließlich zum Zweck der Bewerbungsabwicklung verarbeitet.</p>
<p>Es ist zur Abwicklung des Bewerbungsprozesses unabdingbar, dass Mitarbeiterinnen und Mitarbeiter des Personalbereichs, des jeweiligen Fachbereichs und von ggf. zuständigen Gremien, wie z.B. der Schwerbehindertenvertretung, Zugriff auf Ihre personenbezogenen Daten haben.</p>
<p>Ihre personenbezogenen Daten werden über die Bewerbung auf eine konkrete Stelle oder einen konkreten Einstellungstermin hinaus verarbeitet, um Sie bei anderen auf Ihr Profil passenden Stellen zu kontaktieren, wenn Sie uns dazu Ihre Einwilligung erteilen.</p>
<p>Es gelten die allgemeinen Aufbewahrungs- und Löschfristen. Wir speichern Ihre personenbezogenen Daten grundsätzlich so lange, wie dies für die Entscheidung über Ihre Bewerbung erforderlich ist und darüber hinaus nur, soweit ein anderer Rechtsgrund für die weitergehende Speicherung besteht. Ein solcher anderer Rechtsgrund kann insbesondere aus steuerrechtlichen und buchhalterischen Pflichten oder aus der Abwehr möglicher Rechtsansprüche, insbesondere nach dem Allgemeinen Gleichbehandlungsgesetz (AGG), folgen.</p>
<p>Soweit Sie einer weiteren Datenverarbeitung für andere auf Ihr Profil möglicherweise passenden Stellen nicht zugestimmt haben, löschen wir Ihre Daten spätestens sechs Monate nach Abschluss des Bewerbungsverfahrens. Falls Sie in die Berücksichtigung für weitere Stellen eingewilligt oder sich ohne zeitliche Einschränkung initiativ beworben haben, speichern wir Ihre personenbezogenen Daten für einen Zeitraum von maximal drei Jahren, beginnend mit dem Ende des Jahres, in dem Sie Ihre Einwilligung uns gegenüber erklärt oder Ihre Bewerbung initiativ eingereicht haben. Im Fall einer erfolgreichen Bewerbung übernehmen wir Ihre Bewerbungsunterlagen in Ihre Personalakte.</p>
<p>&nbsp;</p>
<p><strong><a id="DS220" name="DS220"></a>i. Spenden</strong></p>
<p>Viele der evangelischen Gemeinde verbundene Menschen machen durch ihre Spenden Projekte möglich, die sonst vielleicht nicht zustande gekommen wären. Es bieten sich zahlreiche Möglichkeiten, die Arbeit unseres Kirchenkreises und unserer Gemeinden zu unterstützen, sei es durch das Spenden von Zeit oder von Geld.</p>
<p>Für finanzielle Spenden sind Bankverbindungen auf unserer Webseite angegeben. Falls Sie sich entschließen zu spenden, werden Ihr Name, Ihre Kontodaten und der gespendete Betrag, ggf. auch Ihre Adresse, von uns verarbeitet. Der Zweck dieser Verarbeitung ist die reibungslose Abwicklung von Spenden, das Erfüllen gesetzlicher Verpflichtungen und auf Wunsch auch die Ausstellung einer Spendenquittung. Diese Datenverarbeitung ist für die Wahrnehmung einer Aufgabe, die im kirchlichen und öffentlichen Interesse liegt, erforderlich. Damit ist sie gem. § 6 Nr. 4 DSG-EKD i.V.m. Nr. 8 und Art. 6 Abs. 1 UAbs. 1 lit. e) EU DS-GVO rechtmäßig.</p>
<p>&nbsp;</p>
<p><strong><a id="DS230" name="DS230"></a>2. Empfänger / Kategorien von Empfängern der personenbezogenen Daten<br />(§ 17 Abs. 1 Nr. 4 DSG-EKD)</strong></p>
<p>Empfänger der mit der Nutzung des Webauftritts verbundenen Daten ist ausschließlich der Ev. Kirchenkreis Siegen-Wittgenstein. Ihre Daten werden von uns vertraulich behandelt und grundsätzlich nicht an Dritte weitergegeben, weder an Empfänger innerhalb Deutschlands oder der Europäischen Union, noch an Empfänger in Drittstaaten. Die Daten werden nicht kommerziell genutzt, es wird auch kein Profiling betrieben.</p>
<p>Unter Umständen bedienen wir uns aber externer Dienstleister, die personenbezogene Daten in unserem Auftrag verarbeiten. Diese gelten als Auftragsverarbeiter i.S.d. § 30 DSG-EKD. Bei der Weitergabe von Daten an diese Partner wird deshalb stets ein Auftragsverarbeitungsvertrag gemäß den gesetzlichen Vorgaben geschlossen, um die Kontrolle und den Schutz der Daten zu gewährleisten.</p>
<p>Der Ev. Kirchenkreis Siegen-Wittgenstein wird personenbezogene Daten an auskunftsberechtigte Institutionen (Behörden) übermitteln, wenn sie oder die Evangelische Kirche von Westfalen durch Rechtsvorschriften oder per Gerichtsbeschluss dazu verpflichtet ist.</p>
<p>&nbsp;</p>
<p><strong><a id="DS240" name="DS240"></a>3.</strong> <strong>Dauer der Speicherung und Löschung personenbezogener Daten<br />(§ 17 Abs. 2 Nr. 1, 21 DSG-EKD)</strong></p>
<p>Die Dauer der Speicherung personenbezogener Daten hängt von gesetzlichen Vorgaben und dem Zweck der Datenspeicherung ab. Grundsätzlich gilt: Ist der Zweck der Datenverarbeitung nicht mehr gegeben, werden Ihre Daten von uns gelöscht. Für Stellen der Evangelischen Kirche von Westfalen gilt in Bezug auf die Löschung personenbezogener Daten der betreffende Aufbewahrungs- und Kassationsplan sowie die zugehörige Aufbewahrungs- und Kassationsordnung für kirchliche Archive.</p>
<p>Wir sind daneben gem. § 21 Abs. 1 DSG-EKD verpflichtet, Ihre personenbezogenen Daten zu löschen und Sie haben das Recht, eine solche Löschung von uns zu verlangen, wenn einer der folgenden Gründe zutrifft:</p>
<ol style={{ "list-style-type": "lower-alpha;" }}>
<li>
<p>Die Kenntnis der personenbezogenen Daten ist für den Verantwortlichen zur Erfüllung der in seiner Zuständigkeit liegenden Aufgaben nicht mehr erforderlich.</p>
</li>
<li>
<p>Sie widerrufen Ihre Einwilligung, auf die sich die Verarbeitung stützte, und es fehlt an einer anderweitigen Rechtsgrundlage für die Verarbeitung.</p>
</li>
<li>
<p>Sie legen Widerspruch gegen die Verarbeitung ein und es liegen keine vorrangigen berechtigten Gründe für die Verarbeitung vor.</p>
</li>
<li>
<p>Die Speicherung Ihrer personenbezogenen Daten ist unzulässig.</p>
</li>
<li>
<p>Die Löschung der personenbezogenen Daten ist zur Erfüllung einer rechtlichen Verpflichtung erforderlich, dem der Verantwortliche unterliegt.</p>
</li>
<li>
<p>Sie verlangen die Löschung personenbezogener Daten, die bei elektronischen Angeboten erhoben wurden, die Minderjährigen direkt gemacht worden sind.</p>
</li>
</ol>
<p>Diese Verpflichtung zur Löschung bzw. das Recht auf Löschung besteht jedoch gem. § 21 Abs. 3 DSG-EKD ausnahmsweise nicht, soweit die Datenverarbeitung erforderlich ist</p>
<ol style={{ "list-style-type": "lower-alpha;" }}>
<li>
<p>zur Ausübung des Rechts auf freie Meinungsäußerung und Information;</p>
</li>
<li>
<p>zur Erfüllung einer rechtlichen Verpflichtung, die die Verarbeitung nach kirchlichem oder staatlichem Recht, dem der Verantwortliche unterliegt, erfordert, oder zur Wahrnehmung einer Aufgabe, die im kirchlichen Interesse liegt oder in Ausübung hoheitlicher Gewalt erfolgt, die dem Verantwortlichen übertragen wurde;</p>
</li>
<li>
<p>aus Gründen des öffentlichen Interesses im Bereich der öffentlichen Gesundheit;</p>
</li>
<li>
<p>für im kirchlichen Interesse liegende Archivzwecke, wissenschaftliche oder historische Forschungszwecke oder für statistische Zwecke, soweit das zuvor genannte Recht auf Löschung voraussichtlich die Verwirklichung der Ziele dieser Verarbeitung unmöglich macht oder ernsthaft beeinträchtigt, oder</p>
</li>
<li>
<p>zur Geltendmachung von Rechtsansprüchen sowie zur Ausübung oder Verteidigung von Rechten.</p>
</li>
</ol>
<p>&nbsp;</p>
<p><strong><a id="DS250" name="DS250"></a>4. Ihre Rechte als betroffene Person (§ 17 Abs. 2 Nr. 2 DSG-EKD)</strong></p>
<p>Das Datenschutzgesetz der Evangelischen Kirche in Deutschland gibt dem einzelnen Bürger verschiedene Möglichkeiten, den Umgang mit seinen personenbezogenen Daten selbst zu überprüfen und zu beeinflussen.</p>
<p>Sie haben als von der Verarbeitung personenbezogener Daten betroffene Person folgende Rechte:</p>
<p>&nbsp;</p>
<p><strong><a id="DS260" name="DS260"></a>a) Recht auf Auskunft gem. § 19 DSG-EKD </strong></p>
<p>Sofern personenbezogene Daten verarbeitet werden, können Sie gem. § 19 Abs. 1 DSG-EKD jederzeit unentgeltlich Auskunft über diese personenbezogenen Daten und über folgende Informationen verlangen:</p>
<ol>
<li>
<p>die Verarbeitungszwecke;</p>
</li>
<li>
<p>die Kategorien personenbezogener Daten, die verarbeitet werden;</p>
</li>
<li>
<p>die Empfänger oder Kategorien von Empfängern, gegenüber denen die personenbezogenen Daten offengelegt worden sind oder noch offengelegt werden;</p>
</li>
<li>
<p>falls möglich die geplante Dauer, für die die personenbezogenen Daten gespeichert werden, oder, falls dies nicht möglich ist, die Kriterien für die Festlegung dieser Dauer;</p>
</li>
<li>
<p>das Bestehen eines Rechts auf Berichtigung oder Löschung der Sie betreffenden personenbezogenen Daten oder auf Einschränkung der Verarbeitung durch den Verantwortlichen oder eines Widerspruchsrechts gegen diese Verarbeitung;</p>
</li>
<li>
<p>das Bestehen eines Beschwerderechts bei der Datenschutzaufsicht;</p>
</li>
<li>
<p>wenn die personenbezogenen Daten nicht bei der betroffenen Person erhoben werden, alle verfügbaren Informationen über die Herkunft der Daten.</p>
</li>
</ol>
<p>&nbsp;</p>
<p><strong><a id="DS270" name="DS270"></a>b) Recht auf Berichtigung gem. § 20 DSG-EKD </strong></p>
<p>Sie haben das Recht, von uns unverzüglich die Berichtigung Sie betreffender unrichtiger personenbezogener Daten zu verlangen. Unter Berücksichtigung der Zwecke der Verarbeitung haben Sie das Recht, die Vervollständigung unvollständiger personenbezogener Daten - auch mittels einer ergänzenden Erklärung - zu verlangen.</p>
<p>&nbsp;</p>
<p><strong><a id="DS280" name="DS280"></a>c) Recht auf Löschung gem. § 21 DSG-EKD </strong></p>
<p>Details zum Recht auf Löschung finden sie oben unter Punkt 3 dieser Datenschutzerklärung.</p>
<p>&nbsp;</p>
<p><strong><a id="DS290" name="DS290"></a>d) Recht auf Einschränkung der Verarbeitung gem. § 22 DSG-EKD </strong></p>
<p>Sie haben gem. § 22 Abs. 1 DSG-EKD das Recht, von uns die Einschränkung der Verarbeitung Ihrer personenbezogenen Daten zu verlangen, wenn eine der folgenden Voraussetzungen gegeben ist:</p>
<ol>
<li>
<p>die Richtigkeit der personenbezogenen Daten wird von Ihnen bestritten, und zwar für eine Dauer, die es uns ermöglicht, die Richtigkeit der personenbezogenen Daten zu überprüfen;</p>
</li>
<li>
<p>die Verarbeitung ist unrechtmäßig, Sie lehnen die Löschung der personenbezogenen Daten ab und verlangen stattdessen die Einschränkung der Nutzung der personenbezogenen Daten;</p>
</li>
<li>
<p>wir benötigen die personenbezogenen Daten für die Zwecke der Verarbeitung nicht länger, Sie benötigen sie jedoch zur Geltendmachung von Rechtsansprüchen oder zur Ausübung oder Verteidigung von Rechten, oder</p>
</li>
<li>
<p>Sie haben Widerspruch gegen die Verarbeitung eingelegt und es steht noch nicht fest, ob unsere berechtigten Gründe gegenüber Ihren überwiegen.</p>
</li>
</ol>
<p>Wurde die Verarbeitung gemäß den oben genannten Voraussetzungen eingeschränkt, so werden diese personenbezogenen Daten - von ihrer Speicherung abgesehen - nur mit Einwilligung der betroffenen Person oder zur Geltendmachung von Rechtsansprüchen oder zur Ausübung oder Verteidigung von Rechten oder zum Schutz der Rechte einer anderen natürlichen oder juristischen Person oder aus Gründen eines wichtigen kirchlichen Interesses verarbeitet.</p>
<p>&nbsp;</p>
<p><strong><a id="DS300" name="DS300"></a>e) Recht auf Widerspruch gegen die Verarbeitung gem. § 25 DSG-EKD </strong></p>
<p>Sie haben das Recht, aus Gründen, die sich aus Ihrer besonderen Situation ergeben, jederzeit gegen die Verarbeitung Sie betreffender personenbezogener Daten, die aufgrund von § 6 Nr. 1, 3, 4, 8 DSG-EKD erfolgt, Widerspruch einzulegen; dies gilt auch für ein auf diese Bestimmungen gestütztes Profiling. Wir verarbeiten die personenbezogenen Daten in diesem Fall nicht mehr, es sei denn, wir können ein zwingendes kirchliches Interesse für die Verarbeitung nachweisen, das Interesse einer dritten Person an der Verarbeitung überwiegt, oder eine Rechtsvorschrift verpflichtet uns zur Verarbeitung der Daten.</p>
<p>&nbsp;</p>
<p><strong><a id="DS310" name="DS310"></a>f) Recht auf Datenübertragbarkeit gem. § 24 DSG- EKD </strong></p>
<p>Sie haben das Recht, die Sie betreffenden personenbezogenen Daten, die Sie uns bereitgestellt haben, in einem strukturierten, gängigen und maschinenlesbaren Format zu erhalten, und Sie haben das Recht, diese Daten einem anderen Verantwortlichen ohne Behinderung durch uns zu übermitteln, sofern</p>
<p>1) die Verarbeitung auf einer Einwilligung oder auf einem Vertrag beruht und</p>
<p>2) die Verarbeitung mithilfe automatisierter Verfahren erfolgt.</p>
<p>Bei der Ausübung des Rechts auf Datenübertragbarkeit haben Sie das Recht zu erwirken, dass die personenbezogenen Daten direkt von einem Verantwortlichen zu einem anderen Verantwortlichen übermittelt werden, soweit dies technisch machbar ist. Dieses Recht gilt nicht für eine Verarbeitung, die für die Wahrnehmung einer Aufgabe erforderlich ist, die im kirchlichen Interesse liegt oder in Ausübung kirchlicher Gewalt erfolgt, die dem Verantwortlichen übertragen wurde.</p>
<p>&nbsp;</p>
<p><strong><a id="DS320" name="DS320"></a>g) Recht auf Widerruf einer erteilten Einwilligung zur Verarbeitung personenbezogener Daten gem. § 11 Abs. 3 DSG-EKD</strong></p>
<p>Sofern die Verarbeitung der personenbezogenen Daten auf einer von Ihnen erteilten Einwilligung beruht, haben Sie jederzeit das Recht, die Einwilligung ohne Angabe von Gründen zu widerrufen. Der Widerruf gilt nur für die Zukunft. Durch den Widerruf der Einwilligung wird die Rechtmäßigkeit der aufgrund der Einwilligung bis zum Widerruf erfolgten Verarbeitung nicht berührt.</p>
<p><a name="Bookmark4"></a>Möchten Sie eines der soeben beschriebenen Rechte ausüben, wenden Sie sich bitte an die unter Punkt 5 dieser Datenschutzerklärung angegebene Adresse.</p>
<p>&nbsp;</p>
<p><strong><a id="DS330" name="DS330"></a>5. Verantwortliche Stelle (§ 17 Abs. 1 Nr. 1 DSG-EKD)</strong></p>
<p>Verantwortlich für die Verarbeitung personenbezogener Daten auf dieser Webseite ist:</p></div><div class="html_box">
						<div style={{ "margin": "1em 0;"  }}>
							<p>Ev. Kirchenkreis Siegen-Wittgenstein</p>
<p>Jugendbüro Solidarraum 7</p>
<p>Manuela Halberstadt</p>
<p>Ulrike Ermisch</p>
<p>Hermann-Manskopf-Weg 5</p>
<p>57223 Kreuztal</p>
<p>evjugend7[at]kirchenkreis-siwi.de</p>
						</div>
						<div style={{ "margin": "1em 0;"  }}>
							<p>Der Evangelische Kirchenkreis Siegen-Wittgenstein ist eine Körperschaft des öffentlichen Rechts. Er wird vertreten durch die Superintendentin, Kerstin Grünert.</p>
						</div>
					</div><div class="wysiwyg_1   "><div id="N8504746_editor" class="wysiwyg_1 datenschutz">
<p><strong><a id="DS340" name="DS340"></a>6. Unser örtlicher externer Datenschutzbeauftragter (§ 17 Abs. 1 Nr. 2 DSG-EKD)</strong></p>
<p>Als Datenschutzbeauftragter gem. § 36 DSG-EKD wurde bestellt:</p>
<p>Dirk Fromm</p>
<p>Jurist, zertifizierter Datenschutzbeauftragter und Datenschutzauditor (TüV PersCert)</p>
<p>Information Security Officer - ISO/IEC 27001 (TüV PersCert)</p>
<p>CE21 - Gesellschaft für Kommunikationsberatung mbH</p>
<p>Bergfeldstraße 11, 83607 Holzkirchen</p>
<p>Auskunft über Niederlassung NRW:</p>
<p>Donnerbachweg 1, 53332 Bornheim</p>
<p>Tel.: +49 89 7167211-30</p>
<p>Fax: +49 2227 904541</p>
<p>E-Mail: dirk.fromm@ce21.de</p>
<p>&nbsp;</p>
<p><strong><a id="DS350" name="DS350"></a>7. Recht auf Beschwerde bei der zuständigen Aufsichtsbehörde<br />(§ 17 Abs. 2 Nr. 3 DSG-EKD)</strong></p>
<p>Neben den oben aufgezählten Rechten haben Sie unbeschadet eines anderweitigen Rechtsbehelfs das Recht auf Beschwerde bei der Datenschutzaufsicht der Evangelischen Kirche. Die zuständige Stelle ist:</p>
<p><strong><a id="DS351" name="DS351"></a>Der Beauftragte für den Datenschutz der Evangelischen Kirche in Deutschland</strong><br />Außenstelle Dortmund</p>
<p>Friedhof 4</p>
<p>44135 Dortmund</p>
<p>Telefon: +49 (0)231 533827-0</p>
<p>Fax: +49 (0)231 533827-20</p>
<p>E-Mail: mitte-west@datenschutz.ekd.de</p>
<p>Internet: https://datenschutz.ekd.de/</p>
<p>&nbsp;</p>
<p><strong><a id="DS360" name="DS360"></a>8. Sicherheit</strong></p>
<p><strong><a id="DS370" name="DS370"></a>a. Technische und organisatorische Maßnahmen</strong></p>
<p><a name="Bookmark5"></a>Der Ev. Kirchenkreis Siegen-Wittgenstein setzt technische und organisatorische Maßnahmen i.S.d. § 27 DSG-EKD ein, um Ihre zur Verfügung gestellten Daten vor zufälliger oder vorsätzlicher Manipulation, Verlust, Zerstörung oder dem Zugriff unberechtigter Personen zu schützen. Unsere Sicherheitsmaßnahmen werden entsprechend der technologischen Entwicklung fortlaufend verbessert.</p>
<p>&nbsp;</p>
<p><strong><a id="DS380" name="DS380"></a>b. E-Mail</strong></p>
<p>Wenn Sie uns eine E-Mail senden, so wird Ihre E-Mail-Adresse nur für die Korrespondenz mit Ihnen verwendet. Ein Verschlüsselungsverfahren wird nicht eingesetzt. Der E-Mail-Verkehr erfolgt über das ungesicherte Internet. Wir weisen darauf hin, dass das Internet viele Angriffsgefahren birgt und eine absolut sichere übertragung nicht gewährleistet werden kann. Ein lückenloser Schutz der Daten vor dem Zugriff durch Dritte ist nicht möglich. Senden Sie uns deshalb bitte keine vertraulichen oder streng vertraulichen Daten per E-Mail zu.</p>
<p>&nbsp;</p>
<p><strong><a id="DS390" name="DS390"></a>c. TLS-Verschlüsselung (Transport Layer Security)</strong></p>
<p>Unsere Webseite nutzt aus Gründen der Sicherheit und zum Schutz der übertragung vertraulicher Inhalte, wie zum Beispiel der Anfragen, die Sie an uns als Seitenbetreiber senden, eine TLS-Verschlüsselung. Eine verschlüsselte Verbindung erkennen Sie daran, dass die Adresszeile des Browsers von "http://" auf "https://" wechselt und an dem Schloss-Symbol in Ihrer Browserzeile. Wenn die TLS-Verschlüsselung aktiviert ist, können die Daten, die Sie an uns übermitteln, nicht von Dritten mitgelesen werden.</p>
<p>&nbsp;</p>
<p><strong><a id="DS400" name="DS400"></a>9. Links zu anderen Webseiten</strong></p>
<p>Unsere Webseite enthält Links zu anderen Webseiten. Wir haben keinerlei Einfluss auf deren Inhalte und darauf, dass deren Betreiber die geltenden Datenschutzbestimmungen einhalten. Zweck und Umfang einer ggf. erfolgenden Datenerhebung, weiteren Verarbeitung und Nutzung der Daten durch den jeweiligen Dritten, der die entsprechende Webseite betreibt, sowie Ihre diesbezüglichen Rechte und Einstellungsmöglichkeiten zum Schutz Ihrer Privatsphäre entnehmen Sie bitte den Datenschutzhinweisen des Dritten. Auch auf die aktuelle und zukünftige Gestaltung oder die Urheberschaft von Inhalten der verlinkten Seiten haben wir keinerlei Einfluss. Es wird hiermit erklärt, dass zum Zeitpunkt der Linksetzung keine illegalen Inhalte auf den zu verlinkenden Seiten erkennbar waren. Wir distanzieren uns ausdrücklich von allen Inhalten, die möglicherweise straf- oder haftungsrechtlich relevant sind oder gegen die guten Sitten verstoßen. Für illegale, fehlerhafte oder unvollständige Inhalte und für Schäden, die aus der Nutzung oder Nichtnutzung anderer Websites entstehen, haftet allein der Anbieter der Seite, auf welche verwiesen wurde.</p>
<p>&nbsp;</p>
<p><strong><a id="DS410" name="DS410"></a>10. Begriffsbestimmungen</strong></p>
<p>Der Gesetzgeber fordert, dass personenbezogene Daten auf rechtmäßige Weise, nach Treu und Glauben und in einer transparenten, für die betroffene Person nachvollziehbaren Weise verarbeitet werden. Unsere Datenschutzerklärung soll deshalb für jede interessierte Person einfach lesbar und verständlich sein. Um dies zu gewährleisten, möchten wir zuletzt die verwendeten Begrifflichkeiten erläutern.</p>
<p>Wir verwenden in dieser Datenschutzerklärung unter anderem die folgenden Begriffe:</p>
<p><strong><a id="DS420" name="DS420"></a>Betroffene Person</strong></p>
<p>Betroffene Person ist jede identifizierte oder identifizierbare natürliche Person, deren personenbezogene Daten von uns verarbeitet werden.</p>
<p><strong><a id="DS430" name="DS430"></a>Verarbeitung</strong></p>
<p>Verarbeitung ist jeder mit oder ohne Hilfe automatisierter Verfahren ausgeführte Vorgang oder jede solche Vorgangsreihe im Zusammenhang mit personenbezogenen Daten, wie das Erheben, das Erfassen, die Organisation, das Ordnen, die Speicherung, die Anpassung oder Veränderung, das Auslesen, das Abfragen, die Verwendung, die Offenlegung durch übermittlung, Verbreitung oder eine andere Form der Bereitstellung, den Abgleich oder die Verknüpfung, die Einschränkung, das Löschen oder die Vernichtung von Daten.</p>
<p><strong><a id="DS440" name="DS440"></a>Einschränkung der Verarbeitung</strong></p>
<p>Einschränkung der Verarbeitung ist die Markierung gespeicherter personenbezogener Daten mit dem Ziel, ihre künftige Verarbeitung einzuschränken.</p>
<p><strong><a id="DS450" name="DS450"></a>Profiling</strong></p>
<p>Profiling ist jede Art der automatisierten Verarbeitung personenbezogener Daten, die darin besteht, dass diese personenbezogenen Daten verwendet werden, um bestimmte persönliche Aspekte, die sich auf eine natürliche Person beziehen, zu bewerten, insbesondere, um Aspekte bezüglich Arbeitsleistung, wirtschaftlicher Lage, Gesundheit, persönlicher Vorlieben, Interessen, Zuverlässigkeit, Verhalten, Aufenthaltsort oder Ortswechsel dieser natürlichen Person zu analysieren oder vorherzusagen.</p>
<p><strong><a id="DS460" name="DS460"></a>Pseudonymisierung</strong></p>
<p>Pseudonymisierung ist die Verarbeitung personenbezogener Daten in einer Weise, auf welche die personenbezogenen Daten ohne Hinzuziehung zusätzlicher Informationen nicht mehr einer spezifischen betroffenen Person zugeordnet werden können, sofern diese zusätzlichen Informationen gesondert aufbewahrt werden und technischen und organisatorischen Maßnahmen unterliegen, die gewährleisten, dass die personenbezogenen Daten nicht einer identifizierten oder identifizierbaren natürlichen Person zugewiesen werden können.</p>
<p><strong><a id="DS470" name="DS470"></a>Verantwortlicher oder für die Verarbeitung Verantwortlicher</strong></p>
<p>Verantwortlicher oder für die Verarbeitung Verantwortlicher ist die natürliche oder juristische Person, Behörde, Einrichtung, kirchliche Stelle i.S.d. § 2 Abs. 1 S. 1 DSG-EKD oder sonstige Stelle, die allein oder gemeinsam mit anderen über die Zwecke und Mittel der Verarbeitung von personenbezogenen Daten entscheidet.</p>
<p><strong><a id="DS480" name="DS480"></a>Auftragsverarbeiter</strong></p>
<p>Auftragsverarbeiter ist eine natürliche oder juristische Person, Behörde, Einrichtung, kirchliche oder sonstige Stelle, die personenbezogene Daten im Auftrag des Verantwortlichen verarbeitet.</p>
<p><strong><a id="DS490" name="DS490"></a>Empfänger</strong></p>
<p>Empfänger ist eine natürliche oder juristische Person, Behörde, Einrichtung, kirchliche oder sonstige Stelle, der personenbezogene Daten offengelegt werden, unabhängig davon, ob es sich bei ihr um einen Dritten handelt oder nicht.</p>
<p><strong><a id="DS500" name="DS500"></a>Dritter</strong></p>
<p>Dritter ist eine natürliche oder juristische Person, Behörde, Einrichtung, kirchliche oder sonstige Stelle außer der betroffenen Person, dem Verantwortlichen, dem Auftragsverarbeiter und den Personen, die unter der unmittelbaren Verantwortung des Verantwortlichen oder des Auftragsverarbeiters befugt sind, die personenbezogenen Daten zu verarbeiten.</p>
<p><strong><a id="DS510" name="DS510"></a>Einwilligung</strong></p>
<p>Einwilligung ist jede von der betroffenen Person freiwillig für den bestimmten Fall in informierter Weise und unmissverständlich abgegebene Willensbekundung in Form einer Erklärung oder einer sonstigen eindeutigen bestätigenden Handlung, mit der die betroffene Person zu verstehen gibt, dass sie mit der Verarbeitung der sie betreffenden personenbezogenen Daten einverstanden ist.</p>
<p>&nbsp;</p>
<p><strong><a id="DS520" name="DS520"></a>11. Schlussbestimmung</strong></p>
<p>Durch die Weiterentwicklung unserer Webseite oder die Implementierung neuer Technologien kann es notwendig werden, diese Datenschutzerklärung zu ändern. Wir behalten uns vor, diese Datenschutzerklärung jederzeit mit Wirkung für die Zukunft zu ändern. Es gilt immer die zum Zeitpunkt Ihres Besuchs abrufbare Fassung.</p>
<p>Weitere Informationen, z.B. zum Urheberrecht, finden Sie im Impressum.</p>
<div id="sdfootnote1">
<p><a href="#sdfootnote1anc" name="sdfootnote1sym">1</a> Die Europäische Datenschutz-Grundverordnung 2016/679 (EU DS-GVO) ist am 25.05.2018 in Kraft getreten und hat an diesem Tag alle alten deutschen Datenschutzgesetze nahtlos abgelöst.</p>
</div>
<div id="sdfootnote2">
<p><a href="#sdfootnote2anc" name="sdfootnote2sym">2</a> Grundgesetz der Bundesrepublik Deutschland vom 23.05.1949 (BGBl. S. 1).</p>
</div>
<div id="sdfootnote3">
<p><a href="#sdfootnote3anc" name="sdfootnote3sym">3</a> Teil des Grundgesetzes, Die Verfassung des Deutschen Reichs ("Weimarer Reichsverfassung") vom 11. August 1919, (Reichsgesetzblatt 1919, S. 1383).</p>
<p>&nbsp;</p>
<div class="hr_box">&nbsp;</div>
<p>&nbsp;</p>
<p><strong><a id="DS530" name="DS530"></a>Ev. Kirchenkreis Siegen-Wittgenstein - Datenschutzerklärung für Soziale Netzwerke</strong></p>
<p>&nbsp;</p>
<p><a name="Bookmark"></a><strong><a id="DS540" name="DS540"></a>Informationspflichten bei der Erhebung personenbezogener Daten (§ 17 DSG-EKD)</strong></p>
<p><a name="Bookmark1"></a><a name="Bookmark2"></a><a name="_Hlk36727344"></a> In dieser Datenschutzerklärung informieren wir Sie gemäß den Vorgaben des § 17 des Gesetzes über den Datenschutz der Evangelischen Kirche in Deutschland (DSG-EKD) über die Verarbeitung personenbezogener Daten beim Besuch und bei der Interaktion mit der von uns betriebenen Facebook-Seite, dem von uns betriebenen Instagram-Profil und dem von uns betriebenen YouTube-Kanal. Personenbezogene Daten sind alle Daten, mit denen Sie persönlich identifiziert werden können.</p>
<p>Für den Ev. Kirchenkreis Siegen-Wittgenstein als verantwortliche Stelle der Evangelischen Kirche gilt <u>nicht</u> die Europäische Datenschutz-Grundverordnung (DSGVO), sondern ausschließlich Kirchenrecht (Art. 91 DSGVO i.V.m. Art. 140 GG, Art. 137 Abs. 3 WRV, § 2 Abs. 1 DSG-EKD). In Folge dessen werden alle Daten nach den Vorgaben des DSG-EKD verarbeitet. Das DSG-EKD baut auf den Vorgaben der DSGVO auf und ist am 24.05.2018 in Kraft getreten.</p>
<p>&nbsp;</p>
<p><strong><a id="DS550" name="DS550"></a>I. Facebook und Instagram</strong></p>
<p>&nbsp;</p>
<p><a name="Bookmark3"></a>Facebook ist Anbieter sowohl von Facebook als auch von Instagram. Aus diesem Grund gilt diese Datenschutzerklärung für unsere Facebook-Seite <u>und</u> unser Instagram-Profil.</p>
<p>&nbsp;</p>
<p><a name="Bookmark4"></a><a id="DS560" name="DS560"></a>1. <strong>Verantwortliche Stelle (§ 17 Abs. 1 Nr. 1 DSG-EKD)</strong></p>
<p>Soweit wir die von Ihnen über unsere Facebook-Seite und unser Instagram-Profil übermittelten Daten ausschließlich selbst verarbeiten und allein über die Zwecke und Mittel der Verarbeitung entscheiden, ist verantwortliche Stelle für die Datenverarbeitung im Sinne des DSG-EKD</p>
<p><a name="Bookmark5"></a></p>
</div>
</div></div><div class="html_box">
						<div style={{ "margin": "1em 0;"  }}>
							<p>Ev. Kirchenkreis Siegen-Wittgenstein</p>
<p>Jugendbüro Solidarraum 7</p>
<p>Manuela Halberstadt</p>
<p>Ulrike Ermisch</p>
<p>Hermann-Manskopf-Weg 5</p>
<p>57223 Kreuztal</p>
<p>evjugend7[at]kirchenkreis-siwi.de</p>
						</div>
						<div style={{ "margin": "1em 0;"  }}>
							<p>Der Evangelische Kirchenkreis Siegen-Wittgenstein ist eine Körperschaft des öffentlichen Rechts. Er wird vertreten durch die Superintendentin, Kerstin Grünert.</p>
						</div>
					</div><div class="wysiwyg_1   "><div id="N1342525_editor" class="wysiwyg_1 datenschutz">
<div id="sdfootnote3">
<p><a name="Bookmark6"></a>Soweit die von Ihnen über unsere Facebook-Seite und unser Instagram-Profil übermittelten Daten ausschließlich von Facebook verarbeitet werden und Facebook allein über die Zwecke und Mittel der Verarbeitung entscheidet, ist verantwortliche Stelle für die Datenverarbeitung im Sinne des DSG-EKD der Anbieter von Facebook und Instagram in Deutschland:</p>
<p>Facebook Ireland Limited</p>
<p>4 Grand Canal Square</p>
<p>Grand Canal Harbour, Dublin 2</p>
<p>Ireland.</p>
<p><a name="Bookmark7"></a>Soweit die von Ihnen über unsere Facebook-Seite und unser Instagram-Profil übermittelten Daten von uns und Facebook Ireland verarbeitet werden und wir an der Entscheidung über die Zwecke und Mittel der Verarbeitung beteiligt sind, sind wir und Facebook Ireland nach dem Urteil des Europäischen Gerichtshofs vom 5. Juni 2018 in der Rechtssache C210/16 (<a href="http://curia.europa.eu/juris/document/document.jsf?text=&amp;docid=202543&amp;pageIndex=0&amp;doclang=DE">http://curia.europa.eu/juris/document/document.jsf?text=&amp;docid=202543&amp;pageIndex=0&amp;doclang=DE</a>) gemeinsam Verantwortliche für die Datenverarbeitung i.S.d. Art. 26 DSGVO bzw. § 29 DSG-EKD. Eine solche gemeinsame Verantwortlichkeit besteht für die Datenverarbeitung, die durch den Betrieb unserer Facebook-Seite und unseres Instagram-Profils ermöglicht wird. Dies gilt vor allem für die Erstellung von "Seiten-Insights" und Statistiken durch Facebook, die dann dem Betreiber einer Facebook-Seite zur Verfügung gestellt werden. Auch für Instagram-Profile werden von Facebook "Seiten-Insights" und Statistiken erstellt und den Instagram-Profil-Betreibern zur Verfügung gestellt. Weitere Informationen zu den "Seiten-Insights" finden Sie unten unter Punkt 3.c. dieser Erklärung.</p>
<p>&nbsp;</p>
<p><a name="Bookmark8"></a><strong><a id="DS570" name="DS570"></a>2. Datenschutzbeauftragter (§ 17 Abs. 1 Nr. 2 DSG-EKD)</strong></p>
<p><strong><a id="DS580" name="DS580"></a>a. Örtlicher externer Datenschutzbeauftragter des Ev. Kirchenkreises Siegen-Wittgenstein<br /></strong></p>
<p>Dirk Fromm</p>
<p>Jurist, zertifizierter Datenschutzbeauftragter und Datenschutzauditor (TüV PersCert)</p>
<p>Information Security Officer - ISO/IEC 27001 (TüV PersCert)</p>
<p>CE21 - Gesellschaft für Kommunikationsberatung mbH</p>
<p>Bergfeldstraße 11, 83607 Holzkirchen</p>
<p>Auskunft über Niederlassung NRW:</p>
<p>Donnerbachweg 1, 53332 Bornheim</p>
<p>Tel.: +49 89 7167211-30</p>
<p>Fax: +49 2227 904541</p>
<p>E-Mail: dirk.fromm@ce21.de</p>
<p>&nbsp;</p>
<p><strong><a id="DS590" name="DS590"></a>b. Datenschutzbeauftragter von Facebook Ireland</strong></p>
<p>Den Datenschutzbeauftragten von Facebook Ireland können Sie über ein von Facebook Ireland bereitgestelltes Formular kontaktieren: <a href="https://www.facebook.com/help/contact/540977946302970">https://www.facebook.com/help/contact/540977946302970</a>.</p>
<p>&nbsp;</p>
<p><a name="Bookmark9"></a> <a id="DS600" name="DS600"></a><strong>3. Umfang, Zweck und Rechtsgrundlage der Datenverarbeitung<br />(§ 17 Abs. 1 Nr. 3 und Nr. 4 DSG-EKD)</strong></p>
<p><strong><a id="DS610" name="DS610"></a>a. Datenverarbeitung durch Facebook Ireland</strong></p>
<p><a name="Bookmark10"></a><a name="_Hlk36559303"></a><a name="Bookmark12"></a><a name="Bookmark11"></a><a name="_Hlk36565548"></a> Bei jedem Aufruf unserer Facebook-Seite oder unseres Instagram-Profils (über den auf unserer Webseite bereitgestellten Link oder auf andere Weise) werden durch Facebook personenbezogene Daten verarbeitet. Informationen zur Verarbeitung personenbezogener Daten durch Facebook finden Sie in den Datenrichtlinien von Facebook und Instagram unter: <a href="https://de-de.facebook.com/privacy/explanation"><u>https://de-de.facebook.com/privacy/explanation</u></a>, <a href="https://help.instagram.com/519522125107875/?helpref=hc_fnav&amp;bc%5b0%5d=Instagram%20Help&amp;bc%5b1%5d=Privacy%20and%20Safety%20Center">https://help.instagram.com/519522125107875/?helpref=hc_fnav&amp;bc[0]=Instagram%20Help&amp;bc[1]=Privacy%20and%20Safety%20Center</a>. Zusätzliche Informationen zu den Rechtsgrundlagen, auf die Facebook sich für diese Datenverarbeitung stützt, finden Sie unter: <a href="https://www.facebook.com/about/privacy/legal_bases">https://www.facebook.com/about/privacy/legal_bases</a>. Wir haben keine über diese Informationen von Facebook und Instagram hinausgehende Kenntnis davon, in welchem Umfang, zu welchen Zwecken, für welche Dauer und an welchem Ort Daten von Facebook verarbeitet werden, ob und wie Facebook seine Pflicht zur Löschung von Daten erfüllt, an wen Daten weitergegeben werden, wie Daten von Facebook mit anderen Daten und Informationen zusammengeführt, analysiert und vermarktet werden und ob und in welchem Maß von Facebook Profiling durchgeführt wird.</p>
<p>Zudem werden bei jedem Aufruf unserer Facebook-Seite oder unseres Instagram-Profils (über den auf unserer Webseite bereitgestellten Link oder auf andere Weise) durch Facebook Cookies gesetzt. Unternehmen und Institutionen können Facebook-Technologien und -Produkte in ihre Webseiten und Apps einbinden (z.B. Social Plugins). Wenn Sie Webseiten besuchen oder Apps nutzen, die von Unternehmen und Institutionen bereitgestellt werden, die solche Facebook-Technologien/-Produkte verwenden, werden auch dabei durch Facebook Cookies und Tracking-Technologien eingesetzt. Dadurch ist Facebook in der Lage, Ihr Nutzerverhalten weit über die Facebook-Webseiten hinaus nachzuvollziehen und zu analysieren. Weitere Informationen zum Einsatz von Cookies durch Facebook finden Sie in den Cookie-Richtlinien von Facebook und Instagram unter: <a href="https://de-de.facebook.com/policies/cookies/">https://de-de.facebook.com/policies/cookies/</a>, <a href="https://help.instagram.com/1896641480634370">https://help.instagram.com/1896641480634370</a>. Sie können in Ihren Browser-Einstellungen individuell festlegen, ob und welche Cookies gespeichert werden dürfen und wann diese gelöscht werden. An dieser Stelle möchten wir darauf hinweisen, dass der Besuch unserer Facebook-Seite und unseres Instagram-Profils auch möglich ist, wenn Ihr Browser Cookies blockiert.</p>
<p><a name="Bookmark13"></a> Die Verarbeitung personenbezogener Daten, das Setzen von Cookies und die Verwendung von Tracking-Technologien durch Facebook geschieht unabhängig davon, ob Sie in Ihr Facebook- und/oder Instagram-Nutzerkonto eingeloggt sind oder überhaupt über eines verfügen. Falls Sie in Ihrem Facebook- und/oder Instagram-Nutzerkonto eingeloggt sind, ermöglichen Sie Facebook, Ihr Nutzerverhalten geräteübergreifend direkt Ihrem persönlichen Profil zuzuordnen. Das können Sie nach Aussage des Unternehmens verhindern, indem Sie sich aus Ihrem Facebook- bzw. Instagram-Nutzerkonto ausloggen.</p>
<p><a name="Bookmark15"></a><a name="_Hlk35517612"></a> Anbieter von Facebook und Instagram in Deutschland ist die Facebook Ireland Limited, 4 Grand Canal Square, Grand Canal Harbour, Dublin 2, Ireland. Der Mutterkonzern von Facebook Ireland ist die Facebook Inc., 1 Hacker Way, Menlo Park, California 94025, USA. Personenbezogene Daten und sonstige Informationen werden von Facebook in Länder der EU und auch in die USA und andere Drittländer übermittelt - in denen ein niedrigeres Datenschutzniveau als in der EU herrschen kann - und dort von Facebook und seinen Partnern verarbeitet. Facebook hat sich im Rahmen des EU-US Privacy Shields, das ein angemessenes Datenschutzniveau für Datenübermittlungen in die USA sicherstellen soll, für die Unternehmensbereiche Workplace Premium und Werbeanzeigen &amp; Messungen zertifiziert (<a href="https://www.privacyshield.gov/participant?id=a2zt0000000GnywAAC"><u>https://www.privacyshield.gov/participant?id=a2zt0000000GnywAAC</u></a>, <a href="https://www.facebook.com/about/privacyshield"><u>https://www.facebook.com/about/privacyshield</u></a>).</p>
<p><a name="Bookmark14"></a> Wir haben keinen Einfluss auf eine Verarbeitung Ihrer Daten durch Facebook und darauf, dass Facebook die geltenden Datenschutzbestimmungen einhält.</p>
<p>&nbsp;</p>
<p><strong><a id="DS620" name="DS620"></a>b. Datenverarbeitung durch den Ev. Kirchenkreis Siegen-Wittgenstein<br /></strong></p>
<p>Bitte prüfen Sie sorgfältig, welche personenbezogenen Daten Sie uns über Facebook und Instagram übermitteln. Wenn Sie vermeiden möchten, dass Facebook von Ihnen übermittelte Daten verarbeitet, nehmen Sie bitte auf anderem Weg Kontakt zu uns auf. Unsere Kontaktdaten finden Sie oben unter Punkt 1 dieser Erklärung oder im Impressum.</p>
<p>Wir verarbeiten Ihre Daten im Zusammenhang mit unserer Facebook-Seite und unserem Instagram-Profil zu Zwecken der Kommunikation und gegebenenfalls zur Durchführung vorvertraglicher oder vertraglicher Maßnahmen.</p>
<p><a name="Bookmark16"></a>Wir verarbeiten personenbezogene Daten, wenn Sie über unsere Facebook-Seite oder über Instagram-Profil Kontakt zu uns aufnehmen und Inhalte wie Fotos und Videos mit uns teilen, sei es durch das Kommentieren eines Beitrags oder durch das Senden einer Nachricht. Nehmen Sie mit uns über unsere Facebook-Seite oder über unser Instagram-Profil Kontakt auf, werden der Inhalt Ihrer Nachricht sowie die sonstigen dabei übermittelten personenbezogenen Daten von uns verarbeitet. Bitte beachten Sie, dass uns zusätzlich zu den von Ihnen aktiv übermittelten Daten und Inhalten auch weitere Informationen zu Ihrem Nutzer-Profil, Ihren Beiträgen und beispielsweise "Gefällt-mir"-Angaben zugänglich sein können. Der Zugang zu diesen Informationen ist abhängig von den Privatsphäre-Einstellungen, die Sie in Ihrem Facebook-/Instagram-Nutzerkonto vorgenommen haben. Wie Sie Ihre Privatsphäre-Einstellungen prüfen und ändern können, erläutern Facebook und Instagram hier: <a href="https://de-de.facebook.com/help/193677450678703">https://de-de.facebook.com/help/193677450678703</a>, <a href="https://help.instagram.com/285881641526716?helpref=page_content">https://help.instagram.com/285881641526716?helpref=page_content</a>.</p>
<p><a name="Bookmark18"></a><a name="_Hlk36727543"></a><a name="Bookmark17"></a> Die Daten werden von uns streng zweckgebunden ausschließlich zur Kommunikation mit Ihnen bzw. zur Bearbeitung Ihres Anliegens benutzt. Rechtsgrundlage für diese Datenverarbeitung ist § 6 Nr. 4 i.V.m. Nr. 8 DSG-EKD. Unser im Rahmen einer Interessenabwägung überwiegendes berechtigtes / kirchliches Interesse liegt hier darin, mit Ihnen zu kommunizieren und auf Ihre Anfragen und sonstigen Anliegen zu reagieren. Soweit wir dazu in der Lage sind und sofern wir die Daten auch außerhalb der sozialen Netzwerke verarbeitet haben (z.B. indem wir Ihnen eine E-Mail gesendet haben), werden die von Ihnen aktiv mitgeteilten Daten von uns gelöscht, wenn der Zweck für die Verarbeitung entfällt, d. h. konkret, nachdem der Kontakt mit Ihnen endgültig beendet ist. Dies gilt nicht für Daten, die systemseitig von Facebook im Rahmen unserer Kommunikation gespeichert werden; auf die Löschung dieser Daten haben wir keinen Einfluss. Zwingende gesetzliche Aufbewahrungsfristen bleiben davon unberührt.</p>
<p>&nbsp;</p>
<p><a name="Bookmark21"></a> <strong><a id="DS630" name="DS630"></a>c. Datenverarbeitung durch den Ev. Kirchenkreis Siegen-Wittgenstein und Instagram/Facebook Ireland<br />- Statistiken &amp; Seiten-Insights</strong></p>
<p><a name="_Hlk36562050"></a> Wie oben bereits erwähnt, sind wir und Facebook gemeinsam Verantwortliche für die Datenverarbeitung i.S.d. Art. 26 DSGVO bzw. § 29 DSG-EKD im Rahmen der Bereitstellung und Nutzung von "Seiten-Insights".</p>
<p>"Seiten-Insights" sind von Facebook für die Betreiber von Facebook-Seiten und Instagram-Profilen bereitgestellte Analysen in statistischer Form, die Auswertungen darüber enthalten, welche Personen(gruppen) auf welche Weise mit der jeweiligen Seite bzw. Profil und den darin enthaltenen Inhalten interagieren. Die "Seiten-Insights" zeigen uns beispielsweise die Reichweite unserer Seite und unseres Profils, die Interaktion mit unseren Beiträgen sowie Handlungen, demografische Daten (z.B. Alter, Geschlecht, Standort) und weitere Informationen der Besucher sowie Anzahl und Art der Aufrufe. Facebook benutzt bestimmte "Events", die aus Datenpunkten bestehen, - z.B. das Ansehen oder Abonnieren unserer Seite / unseres Profils oder das Kommentieren eines unserer Beiträge durch einen Nutzer - sowie die bei der Interaktion mit unserer Seite / unserem Profil erfassten personenbezogenen Daten, die von Facebook-Servern protokolliert werden, um die "Seiten-Insights" zu erstellen.</p>
<p><a name="_Hlk36727570"></a><a name="_Hlk36721929"></a> Unsere gemeinsame Verantwortlichkeit mit Facebook umfasst die Erstellung dieser Events und deren Zusammenführung in "Seiten-Insights", die uns als Seiten-Betreiber zur Verfügung gestellt werden. Rechtsgrundlage für diese Datenverarbeitung ist auf unserer Seite § 6 Nr. 4 i.V.m. Nr. 8 DSG-EKD. Die Verarbeitung der Daten dient der Wahrung unserer im Rahmen einer Interessenabwägung überwiegenden berechtigten kirchlichen Interessen an einer Optimierung unserer Außendarstellung und Kommunikation sowie unseres Marketings über unsere Facebook-Seite und unser Instagram-Profil, die uns durch die "Seiten-Insights" ermöglicht wird. Wir als Betreiber der Seite / des Profils haben keinen Zugriff auf die personenbezogenen Daten, die im Rahmen von Events verarbeitet werden, sondern nur auf die zusammengefassten "Seiten-Insights". Die Events, die von den Facebook-Servern protokolliert werden, um "Seiten-Insights" zu erstellen, werden ausschließlich von Facebook bestimmt und können von uns als Betreiber der Facebook-Seite bzw. des Instagram-Profils weder eingerichtet, noch bearbeitet oder auf andere Weise beeinflusst werden.</p>
<p><a name="Bookmark19"></a><a name="Bookmark20"></a> Gemäß § 29 Abs. 1 S. 2 DSG-EKD sind gemeinsam Verantwortliche gesetzlich verpflichtet, eine Vereinbarung zu treffen, die in transparenter Form festlegt, welcher Verantwortliche welche datenschutzrechtlichen Pflichten nach der DSGVO bzw. dem DSG-EKD erfüllt. Aus diesem Grund hat Facebook Ireland uns als Facebook-Seiten-Betreiber eine solche Vereinbarung über die gemeinsame Verantwortlichkeit in Form einer "Seiten-Insights-Ergänzung bezüglich des Verantwortlichen" angeboten. Dieser Vereinbarung haben wir durch den weiteren Betrieb unserer Facebook-Seite zugestimmt. Die Vereinbarung ist hier abrufbar: <a href="https://de-de.facebook.com/legal/terms/page_controller_addendum">https://de-de.facebook.com/legal/terms/page_controller_addendum</a>. In der Vereinbarung ist festgelegt, dass Facebook Ireland die Erfüllung der Verpflichtungen aus der DSGVO bzw. aus dem DSG-EKD für die Verarbeitung von "Insights-Daten" übernimmt. Dazu zählen die Erfüllung der Informationspflichten aus Art. 12 und 13 DSGVO / §§ 17 und 18 DSG-EKD, die Reaktion auf eine Geltendmachung von Rechten der Betroffenen gem. Art. 15 - 21 DSGVO / §§ 19 - 25 DSG-EKD sowie Melde- und Benachrichtigungspflichten im Falle einer Datenschutzverletzung gem. Art. 33 und 34 DSGVO / §§ 32 und 33 DSG-EKD. Die Vereinbarung ergänzt die Nutzungsbedingungen (<a href="https://www.facebook.com/legal/terms">https://www.facebook.com/legal/terms</a>, <a href="https://help.instagram.com/581066165581870?ref=dp">https://help.instagram.com/581066165581870?ref=dp</a>) und die Richtlinien für Seiten, Gruppen und Veranstaltungen (<a href="https://www.facebook.com/policies/pages_groups_events">https://www.facebook.com/policies/pages_groups_events#</a>), denen wir zugestimmt haben, um unsere Facebook-Seite und unser Instagram-Profil betreiben zu können.</p>
<p>Weitere Informationen zu "Seiten-Insights" finden Sie unter <a href="https://www.facebook.com/legal/terms/information_about_page_insights_data">https://www.facebook.com/legal/terms/information_about_page_insights_data</a>. Wir haben in Bezug auf die "Seiten-Insights" keine über die oben angegebenen Informationen hinausgehende Kenntnis davon, in welchem Umfang, zu welchen Zwecken, für welche Dauer und an welchem Ort Daten von Facebook gespeichert werden, ob und wie Facebook seine Pflicht zur Löschung von Daten erfüllt, an wen Daten weitergegeben werden und wie Daten von Facebook mit anderen Daten und Informationen zusammengeführt, analysiert und vermarktet werden und ob und in welchem Maß von Facebook Profiling durchgeführt wird.</p>
<p>&nbsp;</p>
<p><strong><a id="DS640" name="DS640"></a>4. Ihre Rechte als betroffene Person (§ 17 Abs. 2 Nr. 2 und Nr. 3 DSG-EKD)</strong></p>
<p>Das Datenschutzgesetz der Evangelischen Kirche in Deutschland gibt dem einzelnen Bürger verschiedene Möglichkeiten, den Umgang mit seinen personenbezogenen Daten selbst zu überprüfen und zu beeinflussen. Sie haben als von der Verarbeitung personenbezogener Daten betroffene Person konkret folgende Rechte:</p>
<ol style={{ "list-style-type": "lower-alpha;" }}>
<li>
<p><strong>Recht auf Auskunft gem. § 19 DSG-EKD</strong></p>
</li>
<li>
<p><strong>Recht auf Berichtigung gem. § 20 DSG-EKD</strong></p>
</li>
<li>
<p><strong>Recht auf Löschung gem. § 21 DSG-EKD</strong></p>
</li>
<li>
<p><strong>Recht auf Einschränkung der Verarbeitung gem. § 22 DSG-EKD </strong></p>
</li>
<li>
<p><strong>Recht auf Datenübertragbarkeit gem. § 24 DSG-EKD</strong></p>
</li>
<li>
<p><strong>Recht auf Widerruf erteilter Einwilligungen (mit Wirkung für die Zukunft) gem. § 11 Abs. 3 DSG-EKD</strong></p>
</li>
</ol>
<p><u>Bitte beachten Sie den folgenden Hinweis:</u></p>
<p>Wenn Ihre gerade aufgezählten Rechte die Verarbeitung von Daten betreffen, für die wir allein Verantwortliche im Sinne des Datenschutzes sind, können Sie diese uns gegenüber mit Hilfe der unter Punkt 1 dieser Erklärung angegebenen Kontaktdaten geltend machen. Wenn Ihre oben aufgezählten Rechte jedoch die Verarbeitung von Daten betreffen, für die Facebook Ireland allein oder gemeinsam mit uns verantwortlich im Sinne des Datenschutzes ist, möchten wir Sie bitten, sich direkt an Facebook Ireland zu wenden. Dies gilt insbesondere für eine Geltendmachung Ihrer Rechte in Bezug auf eine Datenverarbeitung zur Erstellung von "Seiten-Insights". Eine Möglichkeit, den Datenschutzbeauftragten von Facebook Ireland zu kontaktieren, finden Sie ebenfalls oben unter Punkt 1 dieser Erklärung.</p>
<p>&nbsp;</p>
<p><strong><a id="DS650" name="DS650"></a>5. Recht auf Widerspruch gegen die Verarbeitung gem. § 25 DSG-EKD</strong></p>
<p><a name="Bookmark22"></a>Wenn wir zur Wahrung unserer im Rahmen einer Interessenabwägung überwiegenden berechtigten Interessen Ihre personenbezogenen Daten verarbeiten, haben Sie das Recht, aus Gründen, die sich aus Ihrer besonderen Situation ergeben, jederzeit gegen die Verarbeitung Widerspruch einzulegen.</p>
<p>Wir verarbeiten Ihre personenbezogenen Daten dann nicht mehr, es sei denn, an der Verarbeitung besteht ein zwingendes kirchliches Interesse, das Interesse einer dritten Person überwiegt oder eine Rechtsvorschrift verpflichtet uns zur Verarbeitung.</p>
<p><u>Bitte beachten Sie den folgenden Hinweis:</u></p>
<p>Wenn Ihr Widerspruchsrecht die Verarbeitung von Daten betrifft, für die wir allein Verantwortliche im Sinne des Datenschutzes sind, können Sie dieses uns gegenüber mit Hilfe der unter Punkt 1 dieser Erklärung angegebenen Kontaktdaten geltend machen. Wenn Ihr Widerspruchsrecht jedoch die Verarbeitung von Daten betrifft, für die Facebook Ireland allein oder gemeinsam mit uns verantwortlich im Sinne des Datenschutzes ist, möchten wir Sie bitten, sich direkt an Facebook Ireland zu wenden. Dies gilt insbesondere für eine Geltendmachung Ihres Widerspruchsrechts in Bezug auf eine Datenverarbeitung zur Erstellung von "Seiten-Insights". Eine Möglichkeit, den Datenschutzbeauftragten von Facebook Ireland zu kontaktieren, finden Sie ebenfalls oben unter Punkt 1 dieser Erklärung.</p>
<p>Sie können auch der Verarbeitung Ihrer Daten zu Zwecken von personalisierten Werbeanzeigen durch Facebook jederzeit widersprechen, indem Sie die Opt-Out-Möglichkeit in Ihrem Facebook- / Instagram-Nutzerkonto nutzen oder Facebook/Instagram kontaktieren. Mehr Informationen und Wahlmöglichkeiten zu personalisierter Werbung durch Facebook erhalten Sie hier: <a href="https://www.facebook.com/about/ads">https://www.facebook.com/about/ads</a>. Um mehr Informationen über Wahlmöglichkeiten zu erhalten, die Sie im Allgemeinen bezüglich der Verarbeitung von Informationen und der Verfolgung Ihrer Online-Aktivitäten durch Werbetreibende und andere Online-Dienste zu Zwecken der personalisierten Werbung haben, können Sie folgende Webseiten besuchen:</p>
<p>Network Advertising Initiative unter <a href="http://www.networkadvertising.org/managing/opt_out.asp">http://www.networkadvertising.org/managing/opt_out.asp</a></p>
<p>Digital Advertising Alliance unter <a href="http://www.aboutads.info/">http://www.aboutads.info/</a></p>
<p>European Digital Advertising Alliance unter <a href="http://youronlinechoices.eu/">http://youronlinechoices.eu/</a>.</p>
<p>&nbsp;</p>
<p><strong><a id="DS660" name="DS660"></a>6. Recht auf Beschwerde bei der zuständigen Aufsichtsbehörde gem. § 46 DSG-EKD</strong></p>
<p>Neben den oben aufgezählten Rechten haben Sie unbeschadet eines anderweitigen Rechtsbehelfs das Recht auf Beschwerde bei einer örtlichen Aufsichtsbehörde für den Datenschutz. Eine Beschwerde, die die Verarbeitung von Daten betrifft, für die wir allein oder gemeinsam mit Instagram/Facebook Ireland Verantwortliche im Sinne des Datenschutzes sind, können Sie an folgende Stelle richten:</p>
<p><strong>Der Beauftragte für den Datenschutz der Evangelischen Kirche in Deutschland</strong><br />Außenstelle Dortmund</p>
<p>Friedhof 4</p>
<p>44135 Dortmund</p>
<p>Telefon: +49 (0)231 533827-0</p>
<p>Fax: +49 (0)231 533827-20</p>
<p>E-Mail: mitte-west@datenschutz.ekd.de</p>
<p>Internet: https://datenschutz.ekd.de/</p>
<p>Mit einer Beschwerde, die die Verarbeitung von Daten betrifft, für die Instagram/Facebook Ireland allein oder gemeinsam mit verantwortlich im Sinne des Datenschutzes ist, können Sie sich auch an die federführende Aufsichtsbehörde für den Datenschutz von Facebook Ireland wenden. Die zuständige Stelle ist:</p>
<p><strong>Data Protection Commission</strong></p>
<p>21 Fitzwilliam Square South<br />Dublin 2<br />D02 RD28<br />Ireland</p>
<p>Telefon: +353 87 103 0813, +353 87 361 7984</p>
<p>Online-Kontaktformular: <a href="https://www.dataprotection.ie/en/contact/how-contact-us">https://www.dataprotection.ie/en/contact/how-contact-us</a></p>
<p>Internet: <a href="http://www.dataprotection.ie">www.dataprotection.ie</a></p>
<p>&nbsp;</p>
<p><strong><a id="DS670" name="DS670"></a>II. YouTube</strong></p>
<p>&nbsp;</p>
<p><strong><a id="DS680" name="DS680"></a>1. Verantwortliche Stelle (§ 17 Abs. 1 Nr. 1 DSG-EKD)</strong></p>
<p>Soweit wir die von Ihnen über unseren YouTube-Kanal übermittelten Daten ausschließlich selbst verarbeiten und allein über die Zwecke und Mittel der Verarbeitung entscheiden, ist verantwortliche Stelle für die Datenverarbeitung im Sinne des DSG-EKD</p>
</div>
</div></div><div class="html_box">
                            <div style={{ "margin": "1em 0;"  }}>
							<p>Ev. Kirchenkreis Siegen-Wittgenstein</p>
<p>Jugendbüro Solidarraum 7</p>
<p>Manuela Halberstadt</p>
<p>Ulrike Ermisch</p>
<p>Hermann-Manskopf-Weg 5</p>
<p>57223 Kreuztal</p>
<p>evjugend7[at]kirchenkreis-siwi.de</p>
						</div>
						<div style={{ "margin": "1em 0;"  }}>
							<p>Der Evangelische Kirchenkreis Siegen-Wittgenstein ist eine Körperschaft des öffentlichen Rechts. Er wird vertreten durch die Superintendentin, Kerstin Grünert.</p>
						</div>
					</div><div class="wysiwyg_1   "><div id="N2504567_editor" class="wysiwyg_1 datenschutz">
<div id="sdfootnote3">
<p><strong>Anbieter von YouTube in Deutschland ist die Google Ireland Limited</strong>. Soweit die von Ihnen über unseren YouTube-Kanal übermittelten Daten ausschließlich von YouTube/Google Ireland verarbeitet werden und YouTube/Google Ireland allein über die Zwecke und Mittel der Verarbeitung entscheidet, ist verantwortliche Stelle für die Datenverarbeitung im Sinne des DSG-EKD</p>
<p>Google Ireland Limited</p>
<p>Gordon House</p>
<p>Barrow Street, Dublin 4</p>
<p>Ireland.</p>
<p>Soweit die von Ihnen über unseren YouTube-Kanal übermittelten Daten von uns und YouTube/Google Ireland verarbeitet werden und wir an der Entscheidung über die Zwecke und Mittel der Verarbeitung beteiligt sind, sind wir und YouTube/Google Ireland gemeinsam Verantwortliche für die Datenverarbeitung i.S.d. Art. 26 DSGVO bzw. § 29 DSG-EKD.</p>
<p>Eine solche gemeinsame Verantwortlichkeit besteht nach dem Urteil des Europäischen Gerichtshofs vom 5. Juni 2018 in der Rechtssache C210/16 (<a href="http://curia.europa.eu/juris/document/document.jsf?text=&amp;docid=202543&amp;pageIndex=0&amp;doclang=DE">http://curia.europa.eu/juris/document/document.jsf?text=&amp;docid=202543&amp;pageIndex=0&amp;doclang=DE</a>) für die Datenverarbeitung, die durch den Betrieb einer Facebook-Seite ermöglicht wird. Dies gilt vor allem für die Erstellung von "Seiten-Insights" und Statistiken durch Facebook, die dann dem Betreiber einer Facebook-Seite zur Verfügung gestellt werden.</p>
<p><strong>Auch durch den Betrieb unseres YouTube-Kanals wird eine Datenverarbeitung ermöglicht. Für YouTube-Kanäle werden von Google Daten erfasst und daraus Statistiken mit Hilfe von "YouTube Analytics" erstellt. Diese werden den YouTube-Kanal-Betreibern von Google zur Verfügung gestellt.</strong> <strong>Deshalb gehen wir davon aus, dass auch in diesem Fall eine gemeinsame Verantwortlichkeit von uns und Google besteht.</strong> Weitere Informationen zu Statistiken und "YouTube Analytics" finden Sie unten unter Punkt 3.c. dieser Erklärung.</p>
<p>&nbsp;</p>
<p><strong><a id="DS690" name="DS690"></a>2. Datenschutzbeauftragter (§ 17 Abs. 1 Nr. 2 DSG-EKD)</strong></p>
<p><strong><a id="DS700" name="DS700"></a>a. Örtlicher externer Datenschutzbeauftragter des Ev. Kirchenkreises Siegen-Wittgenstein-<br /></strong></p>
<p>Dirk Fromm</p>
<p>Jurist, zertifizierter Datenschutzbeauftragter und Datenschutzauditor (TüV PersCert)</p>
<p>Information Security Officer - ISO/IEC 27001 (TüV PersCert)</p>
<p>CE21 - Gesellschaft für Kommunikationsberatung mbH</p>
<p>Bergfeldstraße 11, 83607 Holzkirchen</p>
<p>Auskunft über Niederlassung NRW:</p>
<p>Donnerbachweg 1, 53332 Bornheim</p>
<p>Tel.: +49 89 7167211-30</p>
<p>Fax: +49 2227 904541</p>
<p>E-Mail: dirk.fromm@ce21.de</p>
<p>&nbsp;</p>
<p><strong><a id="DS710" name="DS710"></a>b. Datenschutzbeauftragter von Google Ireland</strong></p>
<p>Den Datenschutzbeauftragten von Google Ireland können Sie über ein von Google Ireland bereitgestelltes Formular kontaktieren: <a href="https://support.google.com/policies/contact/general_privacy_form">https://support.google.com/policies/contact/general_privacy_form</a>.</p>
<p>&nbsp;</p>
<p><strong><a id="DS720" name="DS720"></a>3. Umfang, Zweck und Rechtsgrundlage der Datenverarbeitung<br />(§ 17 Abs. 1 Nr. 3 und Nr. 4 DSG-EKD)</strong></p>
<p><strong><a id="DS730" name="DS730"></a>a. Datenverarbeitung durch Google Ireland</strong></p>
<p>Bei jedem Aufruf unseres YouTube-Kanals (über den auf unserer Webseite bereitgestellten Link oder auf andere Weise) auf den YouTube-Webseiten werden durch YouTube/Google personenbezogene Daten verarbeitet. Informationen zur Verarbeitung personenbezogener Daten durch YouTube/Google finden Sie in der Datenrichtlinie von Google unter: <a href="https://policies.google.com/privacy?hl=de&amp;gl=de">https://policies.google.com/privacy?hl=de&amp;gl=de</a>. Wir haben keine über diese Informationen von Google hinausgehende Kenntnis davon, in welchem Umfang, zu welchen Zwecken, für welche Dauer und an welchem Ort Daten von YouTube/Google verarbeitet werden, ob und wie YouTube/Google seine Pflicht zur Löschung von Daten erfüllt, an wen Daten weitergegeben werden, wie Daten von YouTube/Google mit anderen Daten und Informationen zusammengeführt, analysiert und vermarktet werden und ob und in welchem Maß von YouTube/Google Profiling durchgeführt wird.</p>
<p>Zudem werden bei jedem Aufruf unseres YouTube-Kanals (über den auf unserer Webseite bereitgestellten Link oder auf andere Weise) auf den YouTube-Webseiten durch YouTube/Google Cookies gesetzt. Unternehmen und Institutionen können Google-Technologien und -Produkte in ihre Webseiten und Apps einbinden (z.B. Social Plugins, Google Analytics, Google Maps). Wenn Sie Webseiten besuchen oder Apps nutzen, die von Unternehmen und Institutionen bereitgestellt werden, die solche Google-Technologien/-Produkte verwenden, werden auch dabei durch Google Cookies eingesetzt. Dadurch ist Google in der Lage, Ihr Nutzerverhalten weit über die YouTube und Google-Webseiten hinaus nachzuvollziehen und zu analysieren. Weitere Informationen zum Einsatz von Cookies durch YouTube/Google finden Sie in der Cookie-Richtlinie von Google unter: <a href="https://policies.google.com/technologies/cookies?hl=de&amp;gl=de">https://policies.google.com/technologies/cookies?hl=de&amp;gl=de</a>. Sie können in Ihren Browser-Einstellungen individuell festlegen, ob und welche Cookies gespeichert werden dürfen und wann diese gelöscht werden. An dieser Stelle möchten wir darauf hinweisen, dass der Besuch unseres YouTube-Kanals auch möglich ist, wenn Ihr Browser Cookies blockiert.</p>
<p>Die Verarbeitung personenbezogener Daten und das Setzen von Cookies durch Google geschieht unabhängig davon, ob Sie in Ihr YouTube- oder Google-Nutzerkonto eingeloggt sind oder überhaupt über eines verfügen. Falls Sie in Ihrem YouTube- oder Google-Nutzerkonto eingeloggt sind, ermöglichen Sie Google, Ihr Nutzerverhalten geräteübergreifend direkt Ihrem persönlichen Profil zuzuordnen. Das können Sie nach Aussage des Unternehmens verhindern, indem Sie sich aus Ihrem YouTube-/Google-Nutzerkonto ausloggen.</p>
<p><a name="Bookmark23"></a> Der Anbieter von YouTube in Deutschland ist die Google Ireland Limited, Gordon House, Barrow Street, Dublin 4, Irland. Der Mutterkonzern von YouTube ist die Google LLC, 1600 Amphitheatre Parkway, Mountain View, California 94043. Personenbezogene Daten und sonstige Informationen werden von Google in Länder der EU und auch in die USA und andere Drittländer übermittelt - in denen ein niedrigeres Datenschutzniveau als in der EU herrschen kann - und dort von Google und seinen Partnern verarbeitet. Der Mutterkonzern von YouTube und Google Ireland Limited, die Google LLC in den USA, hat sich im Rahmen des EU-US Privacy Shields zertifiziert (<a href="https://www.privacyshield.gov/participant?id=a2zt000000001L5AAI">https://www.privacyshield.gov/participant?id=a2zt000000001L5AAI</a>), das ein angemessenes Datenschutzniveau für Datenübermittlungen in die USA sicherstellen soll.</p>
<p>Zusätzlich zur oben aufgeführten Daten- und Cookie-Richtlinie von YouTube/Google gelten für Ihre und unsere Nutzung von YouTube die Nutzungsbedingungen (<a href="https://www.youtube.com/static?template=terms">https://www.youtube.com/static?template=terms</a>), die Community-Richtlinien (<a href="#community-guidelines">https://www.youtube.com/intl/de/about/policies/#community-guidelines</a>) sowie die sonstigen Richtlinien und Hinweise zu Sicherheit und Urheberrecht (<a href="https://support.google.com/youtube/topic/9223153">https://support.google.com/youtube/topic/9223153</a>).</p>
<p>Wir haben keinen Einfluss auf eine Verarbeitung Ihrer Daten durch YouTube/Google und darauf, dass Google die geltenden Datenschutzbestimmungen einhält.</p>
<p>&nbsp;</p>
<p><strong><a id="DS740" name="DS740"></a>b. Datenverarbeitung durch den Ev. Kirchenkreis Siegen-Wittgenstein<br /></strong></p>
<p>Bitte prüfen Sie sorgfältig, welche personenbezogenen Daten Sie uns über YouTube übermitteln. Wenn Sie vermeiden möchten, dass YouTube/Google von Ihnen übermittelte Daten verarbeitet, nehmen Sie bitte auf anderem Weg Kontakt zu uns auf. Unsere Kontaktdaten finden Sie oben unter Punkt 1 dieser Erklärung oder im Impressum.</p>
<p>Wir verarbeiten Ihre Daten im Zusammenhang mit unserem YouTube-Kanal zu Zwecken der Kommunikation und gegebenenfalls zur Durchführung vorvertraglicher oder vertraglicher Maßnahmen.</p>
<p>Wir verarbeiten personenbezogene Daten, wenn Sie über unseren YouTube-Kanal Kontakt zu uns aufnehmen, zum Beispiel durch das Kommentieren eines Beitrags. Nehmen Sie mit uns über unseren YouTube-Kanal Kontakt auf, werden der Inhalt Ihrer Nachricht sowie die sonstigen dabei übermittelten personenbezogenen Daten von uns verarbeitet. Bitte beachten Sie, dass uns zusätzlich zu den von Ihnen aktiv übermittelten Daten und Inhalten auch weitere Informationen zu Ihrem Nutzer-Profil, Ihren Beiträgen und beispielsweise "Gefällt-mir"-Angaben zugänglich sein können. Der Zugang zu diesen Informationen ist abhängig von den Privatsphäre-Einstellungen, die Sie in Ihrem YouTube-Nutzerkonto vorgenommen haben. Wie Sie Ihre Privatsphäre- und Datenschutz-Einstellungen prüfen und ändern können, erläutert YouTube/Google hier: <a href="https://support.google.com/youtube/answer/9315727?hl=de&amp;ref_topic=9386940">https://support.google.com/youtube/answer/9315727?hl=de&amp;ref_topic=9386940</a>, <a href="https://support.google.com/policies/answer/9581826?p=privpol_privts&amp;hl=de&amp;visit_id=637217551183067910-377434558&amp;rd=1">https://support.google.com/policies/answer/9581826?p=privpol_privts&amp;hl=de&amp;visit_id=637217551183067910-377434558&amp;rd=1</a>.</p>
<p>Die Daten werden von uns streng zweckgebunden ausschließlich zur Kommunikation mit Ihnen bzw. zur Bearbeitung Ihres Anliegens benutzt. Rechtsgrundlage für diese Datenverarbeitung ist § 6 Nr. 4 i.V.m. Nr. 8 DSG-EKD. Unser im Rahmen einer Interessenabwägung überwiegendes berechtigtes / kirchliches Interesse liegt hier darin, mit Ihnen zu kommunizieren und auf Ihre Anfragen und sonstigen Anliegen zu reagieren. Soweit wir dazu in der Lage sind und sofern wir die Daten auch außerhalb von YouTube verarbeitet haben (z.B. indem wir Ihnen eine E-Mail gesendet haben), werden die von Ihnen aktiv mitgeteilten Daten von uns gelöscht, wenn der Zweck für die Verarbeitung entfällt, d. h. konkret, nachdem der Kontakt mit Ihnen endgültig beendet ist. Dies gilt nicht für Daten, die systemseitig von YouTube/Google im Rahmen unserer Kommunikation gespeichert werden; auf die Löschung dieser Daten haben wir keinen Einfluss. Zwingende gesetzliche Aufbewahrungsfristen bleiben davon unberührt.</p>
<p>&nbsp;</p>
<p><strong><a id="DS750" name="DS750"></a>c. Datenverarbeitung durch den Ev. Kirchenkreis Siegen-Wittgenstein und Google Ireland - YouTube Analytics &amp; Statistiken</strong></p>
<p>Wie oben bereits erwähnt, gehen wir davon aus, dass wir und YouTube gemeinsam Verantwortliche für die Datenverarbeitung i.S.d. Art. 26 DSGVO bzw. § 29 DSG-EKD im Rahmen der Erstellung und Nutzung von Statistiken bzw. "YouTube Analytics" sind.</p>
<p>"YouTube Analytics" sind von YouTube/Google für die Betreiber von YouTube-Kanälen bereitgestellte Analysen in statistischer Form, die Auswertungen darüber enthalten, welche Personen(gruppen) auf welche Weise mit dem jeweiligen YouTube-Kanal und den darin enthaltenen Inhalten interagieren. "YouTube Analytics" zeigen uns beispielsweise die Reichweite unseres YouTube-Kanals, die Interaktion der Nutzer mit unseren Beiträgen (ansehen, kommentieren, abonnieren) und demografische Daten (z.B. Alter, Geschlecht, Standort) der Besucher sowie die Anzahl der Aufrufe unserer Videos. YouTube/Google benutzt zur Erstellung der "YouTube Analytics"-Statistiken bestimmte Ereignisse - z.B. das Ansehen oder Kommentieren eines unserer Videos oder das Abonnieren unseres Kanals - und die bei der Interaktion mit unserem YouTube-Kanal erfassten personenbezogenen Daten, die von Google-Servern protokolliert werden.</p>
<p>Unsere gemeinsame Verantwortlichkeit mit YouTube/Google umfasst die Erfassung und Zusammenführung von Daten für "YouTube Analytics"-Statistiken für unseren YouTube-Kanal, die uns von YouTube/Google zur Verfügung gestellt werden. Rechtsgrundlage für diese Datenverarbeitung ist auf unserer Seite § 6 Nr. 4 i.V.m. Nr. 8 DSG-EKD. Die Verarbeitung der Daten dient der Wahrung unserer im Rahmen einer Interessenabwägung überwiegenden berechtigten kirchlichen Interessen an einer Optimierung unserer Außendarstellung und Kommunikation sowie unseres Marketings über unseren YouTube-Kanal, die uns durch "YouTube Analytics" ermöglicht wird.</p>
<p>YouTube bzw. Google stellt derzeit keine Vereinbarung über eine gemeinsame Verantwortlichkeit i.S.d. Art. 26 Abs. 1 S. 2 DSGVO bzw. § 29 Abs. 1 S. 2 DSG-EKD zur Verfügung, die festlegt, welcher Verantwortliche welche datenschutzrechtlichen Pflichten nach der DSGVO bzw. dem DSG-EKD erfüllt.</p>
<p>Weitere Informationen zu "YouTube Analytics" finden Sie unter <a href="https://support.google.com/youtube/topic/9257532?hl=de&amp;ref_topic=9257610">https://support.google.com/youtube/topic/9257532?hl=de&amp;ref_topic=9257610</a>. Wir haben in Bezug auf Statistiken und "YouTube Analytics" keine über die oben angegebenen Informationen hinausgehende Kenntnis davon, in welchem Umfang, zu welchen Zwecken, für welche Dauer und an welchem Ort Daten von YouTube/Google gespeichert werden, ob und wie YouTube/Google seine Pflicht zur Löschung von Daten erfüllt, an wen Daten weitergegeben werden und wie Daten von YouTube/Google mit anderen Daten und Informationen zusammengeführt, analysiert und vermarktet werden und ob und in welchem Maß von YouTube/Google Profiling durchgeführt wird.</p>
<p>&nbsp;</p>
<p><strong><a id="DS760" name="DS760"></a>4. Ihre Rechte als betroffene Person (§ 17 Abs. 2 Nr. 2 und Nr. 3 DSG-EKD)</strong></p>
<p>Das Datenschutzgesetz der Evangelischen Kirche in Deutschland gibt dem einzelnen Bürger verschiedene Möglichkeiten, den Umgang mit seinen personenbezogenen Daten selbst zu überprüfen und zu beeinflussen. Sie haben als von der Verarbeitung personenbezogener Daten betroffene Person konkret folgende Rechte:</p>
<ol style={{ "list-style-type": "lower-alpha;" }}>
<li>
<p><strong>Recht auf Auskunft gem. § 19 DSG-EKD</strong></p>
</li>
<li>
<p><strong>Recht auf Berichtigung gem. § 20 DSG-EKD</strong></p>
</li>
<li>
<p><strong>Recht auf Löschung gem. § 21 DSG-EKD</strong></p>
</li>
<li>
<p><strong>Recht auf Einschränkung der Verarbeitung gem. § 22 DSG-EKD </strong></p>
</li>
<li>
<p><strong>Recht auf Datenübertragbarkeit gem. § 24 DSG-EKD</strong></p>
</li>
<li>
<p><strong>Recht auf Widerruf erteilter Einwilligungen (mit Wirkung für die Zukunft) gem. § 11 Abs. 3 DSG-EKD</strong></p>
</li>
</ol>
<p><a name="Bookmark24"></a></p>
<p><u>Bitte beachten Sie den folgenden Hinweis:</u></p>
<p>Wenn Ihre gerade aufgezählten Rechte die Verarbeitung von Daten betreffen, für die wir allein Verantwortliche im Sinne des Datenschutzes sind, können Sie diese uns gegenüber mit Hilfe der unter Punkt 1 dieser Erklärung angegebenen Kontaktdaten geltend machen. Wenn Ihre oben aufgezählten Rechte jedoch die Verarbeitung von Daten betreffen, für die Google Ireland allein oder gemeinsam mit uns verantwortlich im Sinne des Datenschutzes ist, möchten wir Sie bitten, sich direkt an Google Ireland zu wenden. Eine Möglichkeit, den Datenschutzbeauftragten von Google Ireland zu kontaktieren, finden Sie ebenfalls oben unter Punkt 1 dieser Erklärung.</p>
<p>&nbsp;</p>
<p><strong><a id="DS770" name="DS770"></a>5. Recht auf Widerspruch gegen die Verarbeitung gem. § 25 DSG-EKD</strong></p>
<p>Wenn wir zur Wahrung unserer im Rahmen einer Interessenabwägung überwiegenden berechtigten Interessen Ihre personenbezogenen Daten verarbeiten, haben Sie das Recht, aus Gründen, die sich aus Ihrer besonderen Situation ergeben, jederzeit gegen die Verarbeitung Widerspruch einzulegen.</p>
<p>Wir verarbeiten Ihre personenbezogenen Daten dann nicht mehr, es sei denn, an der Verarbeitung besteht ein zwingendes kirchliches Interesse, das Interesse einer dritten Person überwiegt oder eine Rechtsvorschrift verpflichtet uns zur Verarbeitung.</p>
<p><u>Bitte beachten Sie den folgenden Hinweis:</u></p>
<p>Wenn Ihr Widerspruchsrecht die Verarbeitung von Daten betrifft, für die wir allein Verantwortliche im Sinne des Datenschutzes sind, können Sie dieses uns gegenüber mit Hilfe der unter Punkt 1 dieser Erklärung angegebenen Kontaktdaten geltend machen. Wenn Ihr Widerspruchsrecht jedoch die Verarbeitung von Daten betrifft, für die Google Ireland allein oder gemeinsam mit uns verantwortlich im Sinne des Datenschutzes ist, möchten wir Sie bitten, sich direkt an Google Ireland zu wenden. Eine Möglichkeit, den Datenschutzbeauftragten von Google Ireland zu kontaktieren, finden Sie ebenfalls oben unter Punkt 1 dieser Erklärung.</p>
<p>Mehr Informationen und Wahlmöglichkeiten zu personalisierter Werbung durch YouTube/Google erhalten Sie hier: <a href="https://safety.google/intl/de/privacy/ads-and-data/">https://safety.google/intl/de/privacy/ads-and-data/</a>. Eine Opt-Out-Möglichkeit für personalisierte Werbung, die durch Google erfolgt, finden Sie hier: <a href="https://adssettings.google.com/anonymous?sig=ACi0TCgxe64iCWXTsstZ9BTR0UGoyceuQlk6z2ys49Z2dHLVbUuG5_NfhugV5EjWl2bn27jn8Peeo-js8I2OFDNZYcYTNE34-hcCtgK4C1ACSpFNbDjeLNA&amp;hl=de">https://adssettings.google.com/anonymous?sig=ACi0TCgxe64iCWXTsstZ9BTR0UGoyceuQl<br />k6z2ys49Z2dHLVbUuG5_NfhugV5EjWl2bn27jn8Peeo-js8I2OFDNZYcYTNE34-hcCtgK4C1ACSpFNbDjeLNA&amp;hl=de</a>. Um mehr Informationen über Wahlmöglichkeiten zu erhalten, die Sie im Allgemeinen bezüglich der Verarbeitung von Informationen und der Verfolgung Ihrer Online-Aktivitäten durch Werbetreibende und Online-Dienste zu Zwecken der personalisierten Werbung haben, können Sie folgende Webseiten besuchen:</p>
<p>Network Advertising Initiative unter <a href="http://www.networkadvertising.org/managing/opt_out.asp">http://www.networkadvertising.org/managing/opt_out.asp</a></p>
<p>Digital Advertising Alliance unter <a href="http://www.aboutads.info/">http://www.aboutads.info/</a></p>
<p>European Digital Advertising Alliance unter <a href="http://youronlinechoices.eu/">http://youronlinechoices.eu/</a>.</p>
<p>&nbsp;</p>
<p><strong><a id="DS780" name="DS780"></a>6. Recht auf Beschwerde bei der zuständigen Aufsichtsbehörde gem. § 46 DSG-EKD</strong></p>
<p>Neben den oben aufgezählten Rechten haben Sie unbeschadet eines anderweitigen Rechtsbehelfs das Recht auf Beschwerde bei einer örtlichen Aufsichtsbehörde für den Datenschutz. Eine Beschwerde, die die Verarbeitung von Daten betrifft, für die wir allein oder gemeinsam mit YouTube/Google Ireland Verantwortliche im Sinne des Datenschutzes sind, können Sie an folgende Stelle richten:</p>
<p><strong>Der Beauftragte für den Datenschutz der Evangelischen Kirche in Deutschland</strong><br />Außenstelle Dortmund</p>
<p>Friedhof 4</p>
<p>44135 Dortmund</p>
<p>Telefon: +49 (0)231 533827-0</p>
<p>Fax: +49 (0)231 533827-20</p>
<p>E-Mail: mitte-west@datenschutz.ekd.de</p>
<p>Internet: <a href="https://datenschutz.ekd.de/">https://datenschutz.ekd.de/</a></p>
<p>Mit einer Beschwerde, die die Verarbeitung von Daten betrifft, für die YouTube/Google Ireland allein oder gemeinsam mit verantwortlich im Sinne des Datenschutzes ist, können Sie sich auch an die federführende Aufsichtsbehörde für den Datenschutz von Google Ireland wenden. Die zuständige Stelle ist:</p>
<p><strong>Data Protection Commission</strong></p>
<p>21 Fitzwilliam Square South<br />Dublin 2<br />D02 RD28<br />Ireland</p>
<p>Telefon: +353 87 103 0813, +353 87 361 7984</p>
<p>Online-Kontaktformular: <a href="https://www.dataprotection.ie/en/contact/how-contact-us">https://www.dataprotection.ie/en/contact/how-contact-us</a></p>
<p>Internet: <a href="http://www.dataprotection.ie">www.dataprotection.ie</a></p>
</div>
</div></div></div>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
        {/* Weitere Abschnitte */}
      </div>
    </div>
  );
};

export default DataPrivacy;
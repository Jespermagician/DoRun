import "./kmRecord.css";
import { useEffect, useState } from "react";
import { IoHomeOutline } from "react-icons/io5";
import { useNavigate } from "react-router-dom";
import PageHeader from "../Components/PageHeader";
import { getCsrfToken } from "../utils/csrf";
import ListItemUserSelect from "../Components/ListItemUserSelect";
import PerfectScrollbar from "react-perfect-scrollbar";
import { getBackEndDomain } from "../utils/backend-domain";

const KmRecord = () => {
    const navigate = useNavigate();

    // Suchfelder
    const [srch_fname, setSrchFname] = useState("");
    const [srch_lname, setSrchLname] = useState("");
    const [srch_email, setSrchEmail] = useState("");

    const [users, setUsers] = useState([]);
    const [usersList, setUsersList] = useState([]);
    const [sel_user, setSel_user] = useState({});
    const [set_km, setSet_km] = useState(0);

    // Nutzerliste laden beim ersten Render
    useEffect(() => {
        getUsers();
    }, []);

    // Filterfunktion als eigene Funktion
    const filterUsers = () => {
        const filtered = users.filter((user) =>
            (srch_fname === "" || user.firstname.toLowerCase().includes(srch_fname.toLowerCase())) &&
            (srch_lname === "" || user.lastname.toLowerCase().includes(srch_lname.toLowerCase())) &&
            (srch_email === "" || user.email.toLowerCase().includes(srch_email.toLowerCase()))
        );
        setUsersList(filtered);
        // Nutzer automatisch auswählen, wenn nur einer übrig bleibt
        setSel_user(filtered.length === 1 ? filtered[0] : {});
    };

    // Filter bei jeder Änderung der Suchfelder oder Userdaten anwenden
    useEffect(() => {
        filterUsers();
    }, [srch_fname, srch_lname, srch_email, users]);

    // User-Daten vom Backend laden
    const getUsers = async () => {
        try {
            const csrfToken = await getCsrfToken();
            const backEndDomain = await getBackEndDomain();
            const response = await fetch(backEndDomain + "/api/get-users", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json",
                    "X-CSRFToken": csrfToken,
                },
                credentials: "include",
            });

            if (!response.ok) {
                throw new Error("Fehler beim Erhalten der User-Daten!");
            }

            const data = await response.json();
            setUsers(data.users);
        } catch (error) {
            console.error("Fehler beim Abrufen der Nutzer:", error);
        }
    };

    // Eingabefelder-Handler
    const handleChange = (event) => {
        const { name, value } = event.target;

        if (name === "srch_fname") setSrchFname(value);
        if (name === "srch_lname") setSrchLname(value);
        if (name === "srch_email") setSrchEmail(value);
    };

    // Eingabefelder zurücksetzen
    const clearInput = () => {
        setSrchFname("");
        setSrchLname("");
        setSrchEmail("");
        setSel_user({});
    };

    // Kilometer absenden
    const submitKilometer = async (e) => {
        e.preventDefault();

        if (!sel_user.iduser) {
            console.log("Kein Nutzer ausgewählt.");
            return;
        }

        try {
            const csrfToken = await getCsrfToken();
            const backEndDomain = await getBackEndDomain();
            const response = await fetch(backEndDomain + "/api/UpdateUsers", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json",
                    "X-CSRFToken": csrfToken,
                },
                credentials: "include",
                body: JSON.stringify([{
                    Userid: sel_user.iduser,
                    Kilometer: set_km,
                }]),
            });

            if (!response.ok) {
                throw new Error("Fehler beim Senden der Kilometerdaten!");
            }

            const data = await response.json();
            console.log("Kilometer erfolgreich aktualisiert:", data);

            setSet_km(0);
            clearInput();
            getUsers(); // Aktualisiert Liste nach Eintrag
        } catch (error) {
            console.error("Fehler beim Aktualisieren der Kilometer:", error);
        }
    };

    return (
        <>
            <div>
                <button className="home-btn" onClick={() => navigate("/admin")}>
                    <IoHomeOutline /> Home
                </button>
            </div>

            <div className="km-rec-dashboard-container">
                <PageHeader title={"Kilometer Einträge"} />

                <div className="record-content">
                    <div className="section-half left">
                        <h3><span>Nutzer Auswählen</span></h3>

                        <div className="button-row">
                            <button className="clear-btn" onClick={clearInput}>
                                Clear
                            </button>
                            <button className="clear-btn" onClick={getUsers}>
                                Refresh
                            </button>
                        </div>

                        <div className="input-group">
                            <input
                                type="text"
                                name="srch_fname"
                                placeholder="Vorname"
                                className="search-input"
                                value={srch_fname}
                                onChange={handleChange}
                            />
                            <input
                                type="text"
                                name="srch_lname"
                                placeholder="Nachname"
                                className="search-input"
                                value={srch_lname}
                                onChange={handleChange}
                            />
                            <input
                                type="text"
                                name="srch_email"
                                placeholder="E-Mail"
                                className="search-input"
                                value={srch_email}
                                onChange={handleChange}
                            />
                        </div>


                        

                        <div>
                            <h3><span>Nutzer Info</span></h3>
                            <p><strong>Vorname:</strong> {sel_user.firstname}</p>
                            <p><strong>Nachname:</strong> {sel_user.lastname}</p>
                            <p><strong>E-Mail:</strong> {sel_user.email}</p>
                            <p><strong>Kilometer:</strong> {sel_user.kilometers}</p>
                        </div>

                        <form onSubmit={submitKilometer}>
                        <div className="km-input-row">
                            <input
                            type="number"
                            name="set_km"
                            min="0"
                            className="search-input"
                            value={set_km}
                            onChange={(e) => setSet_km(e.target.value)}
                            disabled={Object.keys(sel_user).length === 0}
                            />
                            <button
                            type="submit"
                            className="clear-btn"
                            disabled={Object.keys(sel_user).length === 0}
                            >
                            Submit
                            </button>
                        </div>
                        </form>

                    </div>

                    <div className="section-half right">
                        <div className="user-list-scroll">
                            <PerfectScrollbar>
                            {usersList && usersList.map((user) => (
                                <ListItemUserSelect key={user.iduser} user={user} />
                            ))}
                            </PerfectScrollbar>
                        </div>
                    </div>

                </div>
            </div>
        </>
    );
};

export default KmRecord;
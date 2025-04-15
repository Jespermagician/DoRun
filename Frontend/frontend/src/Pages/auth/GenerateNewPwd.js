import { useEffect, useState } from "react";
import { useParams, useNavigate } from "react-router-dom";
import { getCsrfToken } from "../../utils/csrf";

const GenerateNewPwd = () => {
  // Extract parameters from the URL
  const { UserID, token, TimeStamp } = useParams();
  const navigate = useNavigate();
  const [message_pwd, setMessage_pwd] = useState("");
  const [message2, setMessage2] = useState("");
  const [error, setError] = useState("");
  const [loading, setLoading] = useState(true);
  let isFetched = false; 

  useEffect(() => {


    // Check if all necessary parameters are provided
    if (!UserID || !token || !TimeStamp) {
      setError("Fehlende Parameter");
      setLoading(false);
      return;
    }
    
    const fetchData = async () => {
      try {
        const csrfToken = await getCsrfToken();
        const response = await fetch("http://127.0.0.1:8000/api/generate-pwd", {
            method: "POST",
            headers: {
              "Content-Type": "application/json",
              "X-CSRFToken": csrfToken,
            },
            credentials: "include",
            body: JSON.stringify({
              iduser: UserID,
              token: token,
              timestamp: TimeStamp,
            }),
          }
        );
        if(response.status === 401) {
          setError("Der Link ist ungültig oder wurde bereits aufgerufen!")
          return;
        }
        if(!response.ok) {
          throw new Error("Error fetching data from server.");
        }
        const result = await response.json();
        

        // Parse the response JSON and extract the message
        setMessage_pwd(result.new);
        setMessage2("Bitte melden Sie sich an und ändern es in Ihren Einstellungen. Sie können es hier nur ein einziges mal aufrufen!");
      } catch (err) {
        // Handle errors
        setError(err.message);
      } finally {
        setLoading(false);
      }
    };

    if (!isFetched) {
      isFetched = true;
      fetchData();
    }
  }, [UserID, token, TimeStamp]);

 

  return (
    <div className="flex justify-center items-center h-screen">
      <div className="p-6 w-96 text-center border rounded-lg shadow-md bg-white">
        <h2 className="text-xl font-bold mb-4">Passwort ändern</h2>
        {message_pwd && <p>Ihr neues Passwort: <i>{message_pwd}</i></p>} 
        {message2 && <p>{message2}</p>} 
        {error && <p className="text-red-500">{error}</p>}
        <button onClick={() => navigate("/")} className="mt-4 bg-green-500 text-white py-2 px-4 rounded">Anmelden</button>
      </div>
    </div>
  );
};

export default GenerateNewPwd;

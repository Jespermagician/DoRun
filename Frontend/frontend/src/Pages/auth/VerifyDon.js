import { useEffect, useState } from "react";
import { useParams, useNavigate } from "react-router-dom";
import { getCsrfToken } from "../../utils/csrf";
import { getBackEndDomain } from "../../utils/backend-domain";

const VerifyDon = () => {
  // Extract parameters from the URL
  const { UserID, DonRecID, token } = useParams();
  const navigate = useNavigate();
  const [message, setMessage] = useState(null);
  const [error, setError] = useState(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    // Check if all necessary parameters are provided
    if (!UserID || !token || !DonRecID) {
      setError("Fehlende Parameter");
      setLoading(false);
      return;
    }

    const fetchData = async () => {
      try {
        // Retrieve CSRF token for secure request
        const csrfToken = await getCsrfToken();
        if (!csrfToken) {
          throw new Error("CSRF Token konnte nicht abgerufen werden.");
        }
        const backEndDomain = await getBackEndDomain();

        // Make a GET request to verify user
        const response = await fetch(
          `${backEndDomain}/mail/auth/don/${UserID}/${DonRecID}/${token}/`,
          {
            method: "GET",
            credentials: "include",
            headers: {
              "Content-Type": "application/json",
              "X-CSRFToken": csrfToken,
            },
          }
        );

        // Parse the response JSON and extract the message
        const result = await response.json();
        setMessage(result.message);
      } catch (err) {
        // Handle errors
        setError(err.message);
      } finally {
        setLoading(false);
      }
    };

    fetchData();
  }, [UserID, token]);

  // Function to render content based on the verification message
  const renderContent = () => {
    switch (message) {
      case "EXPIRED":
        return (
          <>
            <p>Der Verifizierungs Link ist abgelaufen.</p>
            {/* <button onClick={() => navigate("/")} className="mt-4 bg-gray-500 text-white py-2 px-4 rounded">Home</button> */}
            {/* <button onClick={() => navigate("/")} className="mt-4 bg-blue-500 text-white py-2 px-4 rounded">Link neu senden</button> */}
          </>
        );
      case "INVALID":
        return (
          <>
            <p>Link ist ungültig.</p>
            {/* <button onClick={() => navigate("/")} className="mt-4 bg-gray-500 text-white py-2 px-4 rounded">Home</button> */}
          </>
        );
      case "VERIFIED":
        return (
          <>
            <p>Vielen Dank. Sie haben sich als Sponsor verifiziert!</p>
            {/* <button onClick={() => navigate("/")} className="mt-4 bg-green-500 text-white py-2 px-4 rounded">Anmelden</button> */}
          </>
        );
      case "ALREADY":
        return (
          <>
            <p>Sponsor wurde bereits verifiziert!</p>
            {/* <button onClick={() => navigate("/")} className="mt-4 bg-green-500 text-white py-2 px-4 rounded">Anmelden</button> */}
          </>
        );
      default:
        return null;
    }
  };

  return (
    <div className="flex justify-center items-center h-screen">
      <div className="p-6 w-96 text-center border rounded-lg shadow-md bg-white">
        <h2 className="text-xl font-bold mb-4">User Auth Verification</h2>
        {loading && <p>Lädt...</p>}
        {error && <p className="text-red-500">{error}</p>}
        {!loading && !error && renderContent()}
      </div>
    </div>
  );
};

export default VerifyDon;

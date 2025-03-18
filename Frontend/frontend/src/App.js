import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import './App.css';
import './Pages/Login.css';
import './Pages/Dashboard.css'
import Login from './Pages/Login';
import Dashboard from './Pages/Dashboard';
import Register from './Pages/Register';
import Admin from './Pages/Admin';
import ProtectedRoute from "./ProtectedRoute";

import VerifyUser from "./Pages/auth/VerifyUser";

function App() {
  return (
      <Router>
        <Routes>
          <Route path="/" element={<Login />}/>
          <Route path="/register" element={<Register />}/>
          <Route path="/homeTest" element={<Dashboard />}/>
          <Route path="/adminTest" element={<Admin />}/>
          <Route 
            path="/home"
            element={
              <ProtectedRoute>
                <Dashboard />
              </ProtectedRoute>
            }
            />
          <Route path="/auth/user/:UserID/:token/:TimeStamp" element={<VerifyUser />} />
          <Route path="/auth/don/:UserID/:token/:TimeStamp" element={<VerifyUser />} />
          <Route path="*" element={<NotFound />}/>
        </Routes>
      </Router>
  );
}

function NotFound() {
  return <h1>404 - Seite nicht gefunden</h1>;
}

export default App;

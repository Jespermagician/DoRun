import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import './App.css';
import './Pages/Login.css';
import './Pages/Dashboard.css'
import Login from './Pages/Login';
import Dashboard from './Pages/Dashboard';
import Register from './Pages/Register';
import Admin from './Pages/Admin';
import ProtectedRoute from "./ProtectedRoute";

function App() {
  return (
      <Router>
        <Routes>
          <Route path="/" element={<Login />}/>
          <Route path="/register" element={<Register />}/>
          <Route path="/home" element={<Dashboard />}/>
          <Route path="/admin" element={<Admin />}/>
          <Route 
            path="/home2"
            element={
              <ProtectedRoute>
                <Dashboard />
              </ProtectedRoute>
            }
            />
        </Routes>
      </Router>
  );
}

export default App;

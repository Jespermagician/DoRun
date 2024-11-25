import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import './App.css';
import './Pages/Login.css';
import './Pages/Dashboard.css'
import Login from './Pages/Login';
import Dashboard from './Pages/Dashboard';

function App() {
  return (
      <Router>
        <Routes>
          <Route path="/" element={<Login />}/>
          <Route path="/home" element={<Dashboard />}/>
        </Routes>
      </Router>
  );
}

export default App;

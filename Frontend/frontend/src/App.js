import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import './App.css';
import './Login.css';
import Login from './Login';

function App() {
  return (
    <div className='App'>
      <h1>DoRun Spendenlaufverwaltung</h1>
      <Router>
        <Routes>
          <Route path="/" element={<Login />}/>
        </Routes>
      </Router>
    </div>
  );
}

export default App;

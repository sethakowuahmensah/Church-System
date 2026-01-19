import { BrowserRouter as Router, Routes, Route, Link } from 'react-router-dom';
import './App.css';
import Home from './pages/Home';
import Login from './pages/Login';
import Signup from './pages/Signup';
import Activities from './pages/Activities';
import Expenses from './pages/Expenses';
import TitheReturns from './pages/TitheReturns';
import Members from './pages/Members';
import Secretary from './pages/Secretary';
import Pastor from './pages/Pastor';

function App() {
  return (
    <Router>
      <div className="App">
        <nav className="main-nav">
          <div className="nav-brand">Church System</div>
          <ul className="nav-links">
            <li><Link to="/">Home</Link></li>
            <li><Link to="/activities">Activities</Link></li>
            <li><Link to="/expenses">Expenses</Link></li>
            <li><Link to="/tithe-returns">Tithe Returns</Link></li>
            <li><Link to="/members">Members</Link></li>
            <li><Link to="/secretary">Secretary</Link></li>
            <li><Link to="/pastor">Pastor</Link></li>
            <li><Link to="/login">Login</Link></li>
            <li><Link to="/signup">Sign Up</Link></li>
          </ul>
        </nav>
        <Routes>
          <Route path="/" element={<Home />} />
          <Route path="/login" element={<Login />} />
          <Route path="/signup" element={<Signup />} />
          <Route path="/activities" element={<Activities />} />
          <Route path="/expenses" element={<Expenses />} />
          <Route path="/tithe-returns" element={<TitheReturns />} />
          <Route path="/members" element={<Members />} />
          <Route path="/secretary" element={<Secretary />} />
          <Route path="/pastor" element={<Pastor />} />
        </Routes>
      </div>
    </Router>
  );
}

export default App;

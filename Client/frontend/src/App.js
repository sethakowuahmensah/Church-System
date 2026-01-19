import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
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
          <img
            src={`${process.env.PUBLIC_URL}/churchpic.jpeg`}
            alt="Church logo"
            className="nav-logo"
          />
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

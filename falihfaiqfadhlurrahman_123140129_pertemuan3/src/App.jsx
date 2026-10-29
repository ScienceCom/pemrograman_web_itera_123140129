import { BrowserRouter as Router, Routes, Route, Link } from 'react-router-dom';
import { BookProvider } from './context/BookContext';
import Home from './pages/Home';
import Stats from './pages/Stats';

export default function App() {
  return (
    <BookProvider>
      <Router>
        <div>
          <nav style={{ padding: '15px', background: '#f0f0f0', marginBottom: '20px' }}>
            <Link to="/" style={{ marginRight: '15px' }}>Beranda</Link>
            <Link to="/stats">Statistik</Link>
          </nav>
          <Routes>
            <Route path="/" element={<Home />} />
            <Route path="/stats" element={<Stats />} />
          </Routes>
        </div>
      </Router>
    </BookProvider>
  );
}
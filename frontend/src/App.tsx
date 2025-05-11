import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import Dashboard from './pages/Dashboard';

function App() {
  return (
    <Router>
      <div className="App bg-hevy-light min-h-screen">
        <header className="bg-hevy-blue text-white p-4">
          <h1 className="text-2xl font-bold">HevyAI</h1>
          <p className="text-sm">Integração com a API do Hevy</p>
        </header>
        <main className="container mx-auto p-4">
          <Routes>
            <Route path="/" element={<Dashboard />} />
          </Routes>
        </main>
      </div>
    </Router>
  );
}

export default App;
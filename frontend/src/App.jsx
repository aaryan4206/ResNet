// frontend/src/App.jsx
import { useState, useEffect } from 'react';

function App() {
  const [message, setMessage] = useState('Loading...');

  useEffect(() => {
    // Vite's proxy forwards '/api/data' directly to 'http://127.0.0'
    fetch('/')
      .then((res) => res.json())
      .then((data) => setMessage(data.message))
      .catch((err) => {
        console.error("Error fetching data:", err);
        setMessage("Failed to connect to backend.");
      });
  }, []);

  return (
    <div style={{ textAlign: 'center', marginTop: '50px' }}>
      <h1>React + Flask Integration</h1>
      <p>Backend Status: <strong>{message}</strong></p>
    </div>
  );
}

export default App;

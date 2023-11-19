import './App.css';
import React from 'react';
import NavBar from './components/NavBar';
import {Outlet} from 'react-router-dom';

function App() {
  return (
    <div className="App">
        <NavBar />
        <div className="app-content">
            <Outlet />
        </div>
    </div>
  );
}

export default App;

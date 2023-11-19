import React from 'react';
import './NavBar.css';
import { Link } from 'react-router-dom';

const NavBar = () => {
  return (
    <header>
      <nav id="navbar">
        <h1 id="navbar-name">Name</h1>
        <ul className="link-list">
            <li><Link className="navbar-link" to="/">Home</Link></li>
            <li><Link className="navbar-link" to="/service">Service</Link></li>
            <li><Link className="navbar-link" to="/about">About</Link></li>
            <li><Link className="navbar-link" to="/contact">Contact</Link></li>
        </ul>
      </nav>
    </header>
  );
};

export default NavBar;

import React from 'react';
import './Homepage.css';
import { Link } from 'react-router-dom';

function Homepage() {
    return (
        <section className="homepage">
            <h2>Revive Guide</h2>
            <div>
                <p>Making teaching CPR easier than ever!</p>
                <p>Try us now, and discover how efficient your training can be!</p>
            </div>
            <div className="buttons">
                <Link to="service/"><button className="service-button">Try It Now!</button></Link>
                <Link to="about/"><button className="about-button">Learn More</button></Link>
            </div>
        </section>
    )
}

export default Homepage;
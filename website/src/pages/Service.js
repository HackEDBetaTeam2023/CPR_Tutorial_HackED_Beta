import React from 'react';
import childrenImage from '../assets/children.png';
import adultImage from '../assets/couple.png';
import VideoGuide from './VideoGuide.js';
import { Link, useMatch, Outlet } from 'react-router-dom';

const Service = () => {
    return (
        <section className="homepage">
            <div className="content-box">
                <h2>Who needs CPR in your situation?</h2>
                <div className="options">
                    <div className="option">
                        <Link to="child-guide/"><img src={childrenImage} alt="Children" /></Link>
                        <Link to="adult-guide/"><img src={adultImage} alt="Adult" /></Link>
                    </div>
                    {/* Add more options as needed */}
                </div>
            </div>
        </section>
    );
};

export default Service;
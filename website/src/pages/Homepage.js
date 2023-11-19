import React from 'react';
import childrenImage from '../assets/children.png';
import adultImage from '../assets/couple.png';

function Homepage() {
    return (
        <section className="homepage">
            <div className="content-box">
                <h2>Who needs CPR in your situation?</h2>
                <div className="options">
                    <div className="option">
                        <img src={childrenImage} alt="Children" />
                        <img src={adultImage} alt="Adult" />
                    </div>
                    {/* Add more options as needed */}
                </div>
            </div>
        </section>
    )
}

export default Homepage;

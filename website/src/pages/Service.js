import React from 'react';
//import NavBar from './NavBar';
import childrenImage from '../assets/children.png'; // Adjust the path based on your project structure

const Service = () => {
    return (
        <>
            <main>
                <div className="content-box">
                    <h2>Who needs CPR in your situation?</h2>
                    <div className="options">
                        <div className="option">
                            <img src={childrenImage} alt="Children" />
                            <span>Children</span>
                        </div>
                        {/* Add more options as needed */}
                    </div>
                </div>
            </main>

            <h1>OpenCV Project</h1>
            <img src="http://127.0.0.1:5000/video_feed" style={{ width: '50%' }} alt="Video Feed" />

        </>
    );
};

export default Service;

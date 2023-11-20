import React from 'react';

const VideoGuide = () => {
    const onClick = () => {
        fetch("http://localhost:5000/poll_key");
    }
    return (
        <div className="video_guide">
            <h2>Adult cardiopulmonary resuscitation (CPR)</h2>
            <p>
                1. Check the person's condition (breathing, pulse, consciousness, etc.).<br/>
                2. Enable the emergency response system.(Reporting to Emergency Medical Institutions, etc.)<br/>
                3. If an automatic defibrillator (AED) is nearby, use it immediately, and if it is not nearby, turn the subject's head back to secure the airway and start chest compression.<br/>
                4. Continue chest compression until the defibrillator is brought in.After using a defibrillator, re-compress the chest immediately. <br/>
                5. The defibrillator is operated repeatedly periodically every two minutes. In the absence of a defibrillator, chest compression is maintained.<br/>
                6. Repeat 5 times until paramedics or medical personnel arrive.
            </p>
            <h1>OpenCV Project</h1>
            <img src="http://127.0.0.1:5000/video_feed" style={{ width: '50%' }} alt="Video Feed" />
            <button type="submit" onClick={onClick}>Start!</button>
        </div>
    )
}

export default VideoGuide;

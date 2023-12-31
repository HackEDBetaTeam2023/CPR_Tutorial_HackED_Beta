import React from 'react';
import ReactDOM from 'react-dom/client';
import './index.css';
import App from './App';
import reportWebVitals from './reportWebVitals';
import {
    BrowserRouter,
    Routes,
    Route
} from "react-router-dom";
import Service from './pages/Service';
import Homepage from './pages/Homepage.js';
import About from './pages/About.js';
import Contact from './pages/Contact.js';
import VideoGuide from './pages/VideoGuide.js';
import PageNotFinished from './pages/PageNotFinished.js';

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
    <React.StrictMode>
        <BrowserRouter>
            <Routes>
                <Route element={<App />}>
                    <Route path="/" element={<Homepage />}/>
                    <Route path="service/" element={<Service />} />
                    <Route path="about/" element={<About />}/>
                    <Route path="contact/" element={<Contact />}/>
                    <Route path="service/child-guide/" element={<PageNotFinished />}/>
                    <Route path="service/adult-guide/" element={<VideoGuide />}/>
                </Route>
            </Routes>
        </BrowserRouter>
    </React.StrictMode>
);

// If you want to start measuring performance in your app, pass a function
// to log results (for example: reportWebVitals(console.log))
// or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals
reportWebVitals();

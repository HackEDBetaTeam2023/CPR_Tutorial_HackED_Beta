import React from 'react';
import '../App.css';
import cprDemo from '../assets/cpr-demo.jpeg';
import cprgraph from '../assets/Survival_graph.png';
import meter1 from "../assets/meter1.svg";
import meter2 from "../assets/meter2.svg";
import meter3 from "../assets/meter3.svg";
import overview from "../assets/project_overview.png";
import detection from "../assets/pose_detection.png";
import Carousel from 'react-multi-carousel';
import 'react-multi-carousel/lib/styles.css';


export const About = () => {
    const responsive = {
        superLargeDesktop: {
          breakpoint: { max: 4000, min: 3000 },
          items: 5
        },
        desktop: {
          breakpoint: { max: 3000, min: 1024 },
          items: 3
        },
        tablet: {
          breakpoint: { max: 1024, min: 464 },
          items: 2
        },
        mobile: {
          breakpoint: { max: 464, min: 0 },
          items: 1
        }
      };

    return (
        <div className="container">
            <header className="about-header">
                <h1>CPR: Life Saving Techniques</h1>
            </header>

            <section className="about-section">
                <h2>What is CPR?</h2>
                <img src={cprDemo} alt="CPR Demonstration" />
                    <p>CPR stands for Cardiopulmonary Resuscitation. It is a lifesaving technique used in emergencies...</p>
            </section>

            <h2>Understanding the importance of CPR</h2>
            <p>Immediate Response</p>
            <p>Critical in Emergency Situations</p>
            <p>Buying Time</p>
            <p>Brain Protection</p>
            <p>Empowering Bystanders</p>

            <div className='about-bx wow zoomIn'>
                <h2>Did you know? </h2>
                <p>About 60% people can survive with CPR, especially if performed immediately, can significantly improve survival chances.</p>
                <img src={cprgraph} alt="CPR Graph" />
            </div>
            
            <h2>Project objective</h2>
            <p>01.Educational Resources</p>
            <p>02.Interactive Learning with tracking over our CPR with detecting program</p>
            <p>03.Immediate Feedback and Improvement</p>
            <p>04.Emergency Assistance</p>

            <h2>Target audience</h2>
            <p>Everyone</p>
            <p>All Health Instructors</p>
            <p>All the people who work in sports fields</p>
            <p>All practitioners in rehabilitation and fitness</p>
            
            <h2>Program Overview</h2>
            <img src={overview} alt="project overview"/>

            <div className='about-bx wow zoomIn'>
                <h2>Movement Detecting Program </h2>
                <p>This program can detect our hands, face, and upper part of body</p>
                <p>Camera can be used through the laptop</p>
                <img src={detection} alt="Pose Detection" />
            </div>

            <h2>Which factor is the program considering?</h2>
            <p>Based on Body Detecting Program it considers:</p>
            <p>Accurate Speed of CPR</p>
            <p>Proper Location of Heart</p>
            <p>Number of times to do CPR</p>
            <p>Total CPR time</p>
        
            <div className="about-bx2 wow zoomIn">
                <h2>Skills we used..</h2>
                <Carousel responsive={responsive} infinite={true} className="owl-carousel owl-theme skill-slider">
                    <div className="item">
                        <img src={meter3} alt="Image" />
                        <h5>Python</h5>
                    </div>
                    <div className="item">
                        <img src={meter1} alt="Image" />
                        <h5>JavaScirpt</h5>
                    </div>
                    <div className="item">
                        <img src={meter3} alt="Image" />
                        <h5>HTML</h5>
                    </div>
                    <div className="item">
                        <img src={meter2} alt="Image" />
                        <h5>CSS</h5>
                    </div>
                    <div className="item">
                        <img src={meter1} alt="Image" />
                        <h5>GitHub</h5>
                    </div>
                    <div className="item">
                        <img src={meter1} alt="Image" />
                        <h5>OpenCV</h5>
                    </div>
                    <div className="item">
                        <img src={meter1} alt="Image" />
                        <h5>React</h5>
                    </div>
                </Carousel>
            </div>

            <h2>Thank you!</h2>
            <p1>Daniel</p1>
            <h2>Ben</h2>
            <h2>Crystal Cho</h2>
            <h2>Rorgon</h2>
            <h2>Aspyn</h2>

            <footer className="about-footer">
                <h2>Thank you for visiting our site and learning about CPR.</h2>
            </footer>

        </div>
    );
};

export default About;
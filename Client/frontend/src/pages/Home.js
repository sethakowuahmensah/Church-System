import React from 'react';
import { Link } from 'react-router-dom';

function Home() {
  const backgroundStyle = {
    backgroundImage: `url(${process.env.PUBLIC_URL}/homepic.jpeg)`,
  };

  return (
    <div className="home-page" style={backgroundStyle}>
      <div className="home-overlay">
        <div className="home-hero">
          <div className="home-hero-text">
            <h1>ROYAL GOSPEL CHURCH INTERNATIONAL</h1>
            <p>
              A central system to manage services, members, tithe returns, activities,
              and finances across your church branches.
            </p>
            <div className="home-hero-actions">
              <Link to="/login" className="btn btn-primary">Get started</Link>
              <Link to="/signup" className="btn btn-secondary">Create account</Link>
              <Link to="/activities" className="btn btn-accent">Activities</Link>
              <Link to="/login" className="btn btn-outline">Admin login</Link>
            </div>
            <p className="home-hero-note">
              Secure access for pastors, secretaries, and members.
            </p>
          </div>
        </div>
      </div>
    </div>
  );
}

export default Home;

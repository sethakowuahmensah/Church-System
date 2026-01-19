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
            <h1>Church administration, simplified.</h1>
            <p>
              A central system to manage services, members, tithe returns, activities,
              and finances across your church branches.
            </p>
            <div className="home-hero-actions">
              <Link to="/login" className="btn btn-primary">Get started</Link>
              <Link to="/signup" className="btn btn-secondary">Create account</Link>
            </div>
            <p className="home-hero-note">
              Secure access for pastors, secretaries, and members.
            </p>
          </div>

          <div className="home-features-grid">
            <div className="feature-card">
              <h3>Activities</h3>
              <p>Plan and track church programs, meetings, and special events.</p>
              <Link to="/activities">View activities &rarr;</Link>
            </div>

            <div className="feature-card">
              <h3>Expenses</h3>
              <p>Record and monitor church expenses with clear reporting.</p>
              <Link to="/expenses">Manage expenses &rarr;</Link>
            </div>

            <div className="feature-card">
              <h3>Tithe returns</h3>
              <p>Submit and review tithe returns for branches and members.</p>
              <Link to="/tithe-returns">Tithe returns &rarr;</Link>
            </div>

            <div className="feature-card">
              <h3>Members</h3>
              <p>Keep an up-to-date directory of members and their details.</p>
              <Link to="/members">Member directory &rarr;</Link>
            </div>

            <div className="feature-card">
              <h3>Secretary</h3>
              <p>Tools focused on the branch secretary&apos;s daily tasks.</p>
              <Link to="/secretary">Secretary tools &rarr;</Link>
            </div>

            <div className="feature-card">
              <h3>Pastor</h3>
              <p>High-level view of activities, giving, and member engagement.</p>
              <Link to="/pastor">Pastor dashboard &rarr;</Link>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}

export default Home;

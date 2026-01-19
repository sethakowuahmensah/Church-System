import React from 'react';

function Home() {
  const backgroundStyle = {
    backgroundImage: `url(${process.env.PUBLIC_URL}/homepic.jpeg)`,
  };

  return (
    <div className="home-page" style={backgroundStyle}>
      <div className="home-overlay">
        <h1>Welcome to the Church System</h1>
        <p>Manage activities, expenses, tithe returns, and members in one place.</p>
      </div>
    </div>
  );
}

export default Home;

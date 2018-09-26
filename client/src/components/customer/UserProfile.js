import React from 'react';
import { Link } from 'react-router-dom';

function UserProfile(props) {
  return (
    <main>
      <h3>Leo DaVinci</h3>
      <p>512-555-5555</p>
      <Link to='/user/event'>
        <button className="button-primary">
          Order Food
        </button>
      </Link>
    </main>
  )
}

export default UserProfile;
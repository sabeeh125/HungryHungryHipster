import React from 'react';
import { Link } from 'react-router-dom';

function VendorProfile(props) {
  return (
    <main>
      <Link to='/vendor/orders'>
        <button className="button-primary">
          Orders
        </button>
      </Link>
      <Link to='/vendor/stats'>
        <button className="button-primary">
          Stats
        </button>
      </Link>
    </main>
  )
}

export default VendorProfile;
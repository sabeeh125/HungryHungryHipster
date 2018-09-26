import React from 'react';
import { Link } from 'react-router-dom';

function Home(props) {
  return (
    <main>
      <Link to='/vendor'>
        <button className="button-primary">Vendor</button>
      </Link>
      <Link to ='/user'>
        <button className="button-primary">Customer</button>
      </Link>
    </main>
  )
}

export default Home;
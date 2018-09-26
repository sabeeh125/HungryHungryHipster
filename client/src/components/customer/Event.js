import React from 'react';
import { Link } from 'react-router-dom';

function Event(props) {
  return (
    <main>
      <Link to ='/user/vendor'>
        <button className="button-primary">
          Slab BBQ
        </button>
      </Link>      
      <button className="button-primary">
        East Side King
      </button>
      <button className="button-primary">
        Burro Cheese Kitchen
      </button>
    </main>
  )
}

export default Event;
import React, { Component } from 'react';
import { Link } from 'react-router-dom';
import fetcher from '../../helpers/fetcher.js';

class Cart extends Component {
  constructor(props) {
    super(props);
    this.state = {
      vendor: this.props.vendor,
      user: this.props.user,
      quantities: this.props.quantities,
      order: {
        vendor_id: this.props.vendor.id,
        user_id: this.props.user.id,
        items: Object.keys(this.props.quantities).map(item_id => {
          return {
            item_id,
            item_quantity: this.props.quantities[item_id].quantity,
          }
        })

      }
    }
    this.doOrderPost = this.doOrderPost.bind(this);
  };

  doOrderPost() {
    const {vendor_id, user_id, items} = this.state.order;
    return fetcher(
      'POST',
      '/atxtab/api/v1.0/orders',
      {
        vendor_id,
        user_id,
        items
      }
    )
      .then(res => this.props.onComplete(res.orders.order_id))
  }

  render() {
    
    return (
      <main>
        <h3>Order Summary from {this.props.vendor.vendor_name}</h3>
        {Object.keys(this.props.quantities)
          //filter out any zero quantity items
          .filter(key => !!Number(this.props.quantities[key].quantity))
          .map((itemId) => (
            <div key={itemId}>
              <h5>Item / Quantity:</h5>
              <p>{this.props.quantities[itemId].name} / {this.props.quantities[itemId].quantity}</p>
            </div>
          ))}
        <div className="menu-item">
          <h3>Payment Info</h3>
          <h5>Card on File:</h5>
          <p>**** **** **** 8725</p>
          <h5>Expiration Date:</h5>
          <p>08/19</p>
        </div>
        <Link to='/user/order'>
          <button type="button" className="button-primary" 
          onClick={this.doOrderPost}>
            Submit Order
          </button>
        </Link>
      </main>
    )
  }
}

export default Cart;
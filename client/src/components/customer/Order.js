import React, { Component } from 'react';
import fetcher from '../../helpers/fetcher';

class Order extends Component {
  constructor(props) {
    super(props);
    this.state ={
      order_id: this.props.order_id,   
      quantities: this.props.quantities,
      order: {}
    }
  }

  getOrder() {
    fetcher('GET', `/atxtab/api/v1.0/orders/${this.props.order_id}/stats`)
    .then(res => console.log(res) || res)
      .then(order => {
        this.setState( { order }, () => console.log(this.state) )  
      })
      .catch(err => console.log(err));
  }

  componentDidUpdate(prevProps) {
    if(this.props.order_id && this.props.order_id !== prevProps.order_id) {
      this.getOrder(); 
    }
  }

  render() {
    console.log(this.state.quantities)
    return (
      <main>
        <h4>Order Number:</h4>
        <h2 className="large-font">{this.props.order_id}</h2>
        <h4>Estimated Wait Time: {this.state.order.wait_time_total} minutes</h4>
        <h4>Total Price: ${this.state.order.price_total}</h4>
      </main>
    )
  }
}

export default Order;
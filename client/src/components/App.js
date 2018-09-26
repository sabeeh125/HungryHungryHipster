import React, { Component } from 'react';
//import logo from './logo.svg';
import '../App.css';
import {BrowserRouter as Router, Route} from 'react-router-dom';
import fetcher from '../helpers/fetcher';

import Home from './Home';
import UserProfile from './customer/UserProfile';
import Event from './customer/Event';
import Vendor from './customer/Vendor';
import Order from './customer/Order';
import Complete from './customer/Complete';
import Cart from './customer/Cart';
import VendorProfile from './vendor/VendorProfile';
import VendorOrders from './vendor/VendorOrders';
import VendorStats from './vendor/VendorStats';


class App extends Component {
  constructor(props) {
    super(props);
    this.state = {
      vendor: {},
      quantities: {
        //{1: {name: '', quantity: #}}
      },
      user: {
        id: 1,
        address_1: '555 Austin Blvd',
        address_2: '',
        city: 'Austin',
        state: 'TX',
        zip: 78751,
        phone: '740-641-5582',
        first_name: 'Hungry',
        last_name: 'Hipster',
      },
      order_id: null,
    }
    this.onChange = this.onChange.bind(this);
  }

  componentDidMount() {
    fetcher('GET', '/atxtab/api/v1.0/vendors/1')
    .then(res => console.log(res) || res)
      .then(vendor => {
        this.setState( vendor )
        });
  }

  onChange(e) {
    const quantities = this.state.quantities;
    quantities[e.target.dataset.id] = {
      name: e.target.dataset.name,
      quantity: e.target.value
    };

    this.setState({
      quantities,
    });
  }

  onComplete = (order_id) => {
    this.setState({
      order_id,
    })
  } 
  
  render() {
    const items = this.state.vendor.items;
    const vendor = this.state.vendor.vendor_name;

    if(!items || !vendor) {
      return (
        <div>loading</div>
      )
    }

    return (
      <Router>
        <div className="App">
          <div className="App-header">  
            <h1 className="title">HUNGRY HUNGRY</h1>
            <h1 className="title">HIPSTER</h1>
          </div>
          <Route exact path="/" component={Home} />
          <Route exact path="/user" component={UserProfile} />
          <Route exact path="/user/event" component={Event} />
          <Route exact path="/user/vendor" render={props => (
            <Vendor {...props}
              vendor={this.state.vendor}
              quantities={this.state.quantities}
              onChange={this.onChange}
              />)} />
          <Route exact path="/user/order" render= {props => (
            <Order {...props}
              order_id={this.state.order_id}
              quantities={this.state.quantities}
            />
          )} />
          <Route exact path="/user/complete" component={Complete} />
          <Route exact path="/user/cart" render={props => (
            <Cart {...props}
              vendor={this.state.vendor}
              quantities={this.state.quantities}
              user={this.state.user}
              onComplete={this.onComplete}
              />)} />
          <Route exact path="/vendor" component={VendorProfile} />
          <Route exact path="/vendor/stats" component={VendorStats} />
          <Route exact path="/vendor/orders" component={VendorOrders} />
          <img className="logo" src="/truck2.png" alt="food truck"/>
        </div>
      </Router>
    );
  }
}

export default App;

//<img src={logo} className="App-logo" alt="logo" />

import React from 'react';
import Button from './button';

//stephen grider is a good udemy professor for react

const App = () => {
	return (
		<div>
			<h1 class="title">Current Order</h1>
			<Button className="button-primary:hover" text="Update Order" margin="10px"  clickFnc={orderCollect}/>
			<Button className="button-primary:hover" text="Order is ready" color="green" clickFnc={orderReady} />
			 <br /> 
			<p className="vendor-name">Food Items In Order for Erin:</p>
			<p className="menu-item" id="food">Brussel Sprout Salad</p>
			<p className="menu-item" id="food">Tori Meshi</p>
			
		</div>
	)
}

function orderCollect(e){
	fetcher('GET', '/atxtab/api/v1.0/orders/1') 
	.then(function(response) {
		//alert(response);
		// var vendor = response.vendor
		console.log(response.order.items[1]);
	alert("New Order: "+ response.order.items[0].item_id);
	//VendorOrders();


function VendorOrders() {
	return <div dangerouslySetInnerHTML={{
    __html: '<em>response.order.items[-1].item_name</em>'
}} />
}

//export default VendorOrders;

	});


function fetcher(method, path, body) {
  return fetch(`http://54.226.185.103:5000${path}`, {
    method,
    headers: {
      Accept: 'application/json',
      'Content-Type': 'application/json',
      'Access-Control-Allow-Origin': '*',
      'Access-Control-Allow-Methods': 'GET',
    },
    body: JSON.stringify(body),
  })
    .then((res) => {
      if (!res.ok) {
        throw Error(res.statusText);
      }
      return res;
    })
    .then(res => res.json());
}


};
function orderReady(e){

var hipster = "Erin"; 

//sender("POST",'/atxtab/api/v1.0/sms',{"body":"Order for "+hipster+" is ready for pickup!!"});



sender("POST","/orders/<int:order_id>/status",{"body":"Complete"});
 


};

function sender(method, path, body) {
  return fetch(`http://54.226.185.103:5000${path}`, {
    method,
    headers: {
      Accept: 'application/json',
      'Content-Type': 'application/json',
      'Access-Control-Allow-Origin': '*',
      'Access-Control-Allow-Methods': 'POST',
    },
    body: JSON.stringify(body),
  })
    .then((res) => {
      if (!res.ok) {
        throw Error(res.statusText);
      }
      return res;
    })
    .then(res => res.json());
}

function backupload(){
	

};

export default App
#!flask/bin/python

from flask import abort, request, Flask, jsonify, make_response
from flask_cors import CORS, cross_origin
from twilio import twiml
from twilio.rest import Client

# Pull in configuration from system environment variables
account_sid = "AC50d5f032a3a46203dcc426c2c4f8fed5"
auth_token = "995372d2ba23503ec919411cf8f0ed38"
client = Client(account_sid, auth_token)

# create an authenticated client that can make requests to Twilio for your
# account.
#client = TwilioRestClient(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

app = Flask(__name__)
CORS(app)

orders = [
   {
        'order_id': 1,
        'vendor_id': u'1',
        'user_id': u'1',
        'order_status': u'order_complete',
        'items': [
             {
                'item_id': u'1',
                'item_quantity': u'4',
             },
             {
                'item_id': u'2',
                'item_quantity': u'2',
             }
        ]
   }
]

users = [
   {
        'id': 1,
        'first_name': u'Hungry',
        'last_name': u'Hipster',
        'address_1': u'701 Brazos',
        'address_2': u'',
        'city': u'Austin',
        'state': u'Texas',
        'zip': u'78706',
        'status': u'active',
        'phone': u'512-123-2345',
        'credit_cards': [ 
            {
                 'saved_cc_name': u'primary card',
                 'cc_number': u'12345678899',
                 'expiration_date': u'01/18',
                 'num_back': u'412',
                 'active': u'true'
            },
            {
                 'saved_cc_name': u'backup card',
                 'cc_number': u'12345678899',
                 'expiration_date': u'01/18',
                 'num_back': u'412',
                 'active': u'false'
            }
        ]
    },
   {
        'id': 2,
        'first_name': u'Harrison',
        'last_name': u'Ford',
        'address_1': u'703 Brazos',
        'address_2': u'',
        'city': u'Austin',
        'state': u'Texas',
        'zip': u'78706',
        'status': u'active',
        'phone': u'512-233-2345',
        'credit_cards': [
            {
                 'saved_cc_name': u'primary card',
                 'cc_number': u'1324235678899',
                 'expiration_date': u'02/18',
                 'num_back': u'413',
                 'active': u'true'
            },
            {
                 'saved_cc_name': u'backup card',
                 'cc_number': u'12234678899',
                 'expiration_date': u'06/18',
                 'num_back': u'432',
                 'active': u'false'
            }
        ]
    }
]



vendors = [
   {
        'id': 1,
        'vendor_name': u'Slab BBQ',
        'vendor_logo': u'http://realdopebbq.com/wp-content/themes/realdopebbq/images/logo.png',
        'vendor_description': u'Completely delicious BBQ',
        'items': [
            {
                 'item_id': u'1',
                 'item_name': u'Notorious P.I.G.',
                 'item_description': u'Slabs original BBQ classic. Pulled pork topped with mustard cole slaw and backyard red',
                 'item_price': u'7.50',
                 'item_wait_time': u'5',
                 'item_url': u'https://farm5.staticflickr.com/4428/35966397574_378af3f24e.jpg',
                 'active': u'true'
            },
            {
                 'item_id': u'2',
                 'item_name': u'Texas O.G.',
                 'item_description': u'Texas classic BBQ sandwitch. Prime Angus brisket topped with pickes, onions, and backyard red.',
                 'item_price': u'9.00',
                 'item_wait_time': u'7',
                 'item_url': u'https://farm9.staticflickr.com/8186/8351713851_e638159d8b.jpg',
                 'active': u'true'
            }
         ]
    },
    {
        'id': 2,
        'vendor_name': u'East Side King',
        'vendor_logo': u'https://37b7056d31190ef2fa7a-433f921b39a1bc4f0ccf711eb1902eb5.ssl.cf2.rackcdn.com/de14f8a3fb0e4bd69acc523e54839de5.png',
        'vendor_description': u'Completely delicious Thai',
        'items': [
            {
                 'item_id': u'1',
                 'item_name': u'Thai Chicken Kara-Age',
                 'item_description': u'Deep-fried chicken thigh sweet & spicy sauce basil cilantro mint onion jalapeno',
                 'item_price': u'8.50',
                 'item_wait_time': u'6',
                 'item_url': u'https://farm3.staticflickr.com/2067/2937919437_156fd31b61.jpg',
                 'active': u'true'
            },
            {
                 'item_id': u'2',
                 'item_name': u'Beet Home Fries',
                 'item_description': u'Deep-fried roasted beets, Kewpie mayo, shichimi togarashi, green onion',
                 'item_price': u'7.50',
                 'item_wait_time': u'5',
                 'item_url': u'https://farm8.staticflickr.com/7280/8151301434_66aa0d6d5a.jpg',
                 'active': u'true'
            }
         ]
    },
    {
        'id': 3,
        'vendor_name': u'Burro Cheese Kitchen',
        'vendor_logo': u'http://www.burrocheesekitchen.com/wp-content/uploads/2013/02/Burro_shield.png',
        'vendor_description': u'Completely delicious Cheese',
    }
]


#########################
# Users - GET REQUESTS
#########################
@app.route('/atxtab/api/v1.0/users', methods=['GET'])
def get_users():
    return jsonify({'users': users})

@app.route('/atxtab/api/v1.0/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = [user for user in users if user['id'] == user_id]
    if len(user) == 0:
        abort(404)
    return jsonify({'user': user[0]})

#########################
# Vendors - GET REQUESTS
#########################
@app.route('/atxtab/api/v1.0/vendors', methods=['GET'])
def get_vendors():
    return jsonify({'vendors': vendors})

@app.route('/atxtab/api/v1.0/vendors/<int:vendor_id>', methods=['GET'])
def get_vendor(vendor_id):
    vendor = [vendor for vendor in vendors if vendor['id'] == vendor_id]
    if len(vendor) == 0:
        abort(404)
    return jsonify({'vendor': vendor[0]})

#@app.route('/atxtab/api/v1.0/vendors/<int:vendor_id>/items/<int:item_num>', methods=['GET'])
#def get_vendor(vendor_id):
#    vendor = [vendor for vendor in vendors if vendor['id'] == vendor_id]
#    if len(vendor) == 0:
#        abort(404)
#    results = str("[")
#    for item in vendor[0]['items']:
#       item_id = item['item_id'][0]
#       item_price = item['item_price'][0]
#       item_wait_time = item['item_wait_time'][0]
#
#       if(results == str("[")):
#         results = results + "{'item_id': " + item_id + ", 'item_price': " + item_price + ", 'item_wait_time': " + item_wait_time + "}"
#       else:
#         results = results + "{'item_id': " + item_id + ", 'item_price': " + item_price + ", 'item_wait_time': " + item_wait_time + "}"
#    results = results + "]"
#    return jsonify(results)

#########################
# Vendors - POST REQUESTS
#########################
@app.route('/atxtab/api/v1.0/vendors', methods=['POST'])
def create_vendors():
    if not request.json or not 'vendor_name' in request.json:
        abort(400)
    vendor = {
        'id': vendors[-1]['id'] + 1,
        'vendor_name': request.json['vendor_name'],
        'vendor_description': request.json.get('vendor_description', ""),
        'vendor_logo': request.json.get('vendor_logo', ""),
    }
    vendors.append(vendor)
    return jsonify({'vendor': vendor}), 201


#########################
# Orders - GET REQUESTS
#########################
@app.route('/atxtab/api/v1.0/orders', methods=['GET'])
def get_orders():
    return jsonify({'orders': orders})

@app.route('/atxtab/api/v1.0/orders/<int:order_id>', methods=['GET'])
def get_order(order_id):
    order = [order for order in orders if order['order_id'] == order_id]
    if len(order) == 0:
        abort(404)
    return jsonify({'order': order[0]})

@app.route('/atxtab/api/v1.0/orders/<int:order_id>/stats', methods=['GET'])
def get_order_stats(order_id):
    
    results = str("[")
    order = [order for order in orders if order['order_id'] == order_id]
    if len(order) == 0:
        abort(404)
    #results = results + str({'order': order[0]})
    vendor = [vendor for vendor in vendors if order[0]['vendor_id']]
    
    price_total = float(0)
    wait_time_total = float(0)
    for item in vendor[0]['items']:
       item_id = item['item_id'][0]
       item_price = item['item_price'][0]
       item_wait_time = item['item_wait_time'][0]
#       price_total = float(item_price)
#       price_total = format(price_total,'.2f')
#       wait_time_total = float(wait_time_total) + float(item_wait_time)
       results = results + "{'item_price': " + str(item_price) + ", 'item_id': " + str(item_id) + ", 'item_wait_time': " + str(item_wait_time) + "}" 
    return jsonify(results)


#########################
# Orders - POST REQUESTS
#########################
@app.route('/atxtab/api/v1.0/orders', methods=['POST'])
def create_orders():
    if not request.json or not 'user_id' in request.json:
        abort(400)
    order = {
        'order_id': orders[-1]['order_id'] + 1,
        'user_id': request.json['user_id'],
        'vendor_id': request.json['vendor_id'],
        'items':  request.json['items'],
        'order_status': 'order_complete'
    }
    orders.append(order)
    return jsonify({'orders': order}), 201


@app.route('/atxapi/api/v1.0/orders/<int:order_id>/status', methods=['POST'])
def update_status(order_id):
    order = [order for order in orders if order['order_id'] == order_id]
    if len(order) == 0:
        abort(404)
    order[0]['order_status'] = request.json.get('order_status', order[0]['order_status'])
    return jsonify({'order': order[0]})

#########################
# Orders - POST REQUESTS
#########################
@app.route('/atxtab/api/v1.0/sms', methods=['POST'])
def message():
#user_id': request.json['user_id']    +17406415582
    # Send a text message to the number provided
    message = client.api.account.messages.create(to="+17406415582",
                                         from_="+12164506685",
                                         body=request.json['body'])

    # Return a message indicating the text message is enroute
    return 'Message on the way!'

#########################
# Error Handling
#########################

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)


if __name__ == '__main__':
    app.run(host= '0.0.0.0', port=5000, debug=True)
#    app.run(debug=True)

from flask import Flask,jsonify,request,Response
import json

app = Flask(__name__)

orders = [
	{
		'food':'salad',
		'price':100,
		'id':1
	},

	{
		'food':'pizza',
		'price':700,
		'id':2
	}
]

#GET/orders
@app.route('/orders')
def get_orders():
	return jsonify({'orders':orders})

def validOrderObject(OrderObject):
	if ("food" in OrderObject
			and "price" in OrderObject
				and "id" in OrderObject):
		return True
	else:
		return False

#new order
@app.route('/orders', methods=['POST'])
def add_order():
	request_data = request.get_json()
	response = Response("", 201, mimetype="application/json")
	response.headers['Location'] = "/orders/" 
	return response
	
#GET/specific/order
@app.route('/orders/<int:id>')
def get_order_by_id(id):
 	return_value = {}
 	for order in orders:
 		if order ["id"] == id:
 			return_value = {
 				'food':order["food"],
 				'price':order['price']
 			}
 	return jsonify(return_value)

#change status of the order
@app.route('/orders/<int:id>',methods=['PUT'])
def change_status(id):
	request_data = request.get_json(force=True)
	new_order = {
		"food": request_data['food'],
		"price": request_data['price'],
		"id": id
		}
	i = 0;
	for order in orders:
		if  order['id'] == new_order:
			orders[i] = new_order
		i += 1
	response = Response("", status=204)
	return response

@app.route('/orders/<int:id>',methods=['DELETE'])
def delete_order(id):
	i = 0;
	for order in orders:
		if order["id"] == id:
			orders.pop(i)
			response = Response("", status=204)
			return response
		i += 1
	invalidOrderObjectErrorMsg = {
			"error":"Order with id  number was not found",
			
		}
	response = Response(json.dumps(invalidOrderObjectErrorMsg), status=404, mimetype="application/json")
	return response
		

app.run(port=5000,debug=True)
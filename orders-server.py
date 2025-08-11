import uuid
from flask import Flask, request

app = Flask("orderapp")

all_orders = {
}

@app.route("/")
def main_error():
    result = {'msg':"root endpoint not supported. Please try only /orders."}
    return result

@app.route('/orders', methods=['GET'])
def get_all_orders():
    return all_orders

@app.route('/orders', methods=['POST'])
def add_new_order():     #  Details: "prod", "quantity", but no id
    order_details = request.get_json()
    new_id = str(uuid.uuid4())
    order_details['id'] = new_id
    all_orders[new_id] = order_details
    return {'id': new_id}

@app.route('/orders/<id>', methods=['DELETE'])
def delete_order(id):
    if id in all_orders:
       del all_orders[id]
       return {'msg': 'deleted'}
    else:
        return {'msg': "can't delete, order id is invalid"}



@app.route('/orders/<id>', methods=['GET'])
def get_specific_order(id):
    return all_orders[id]


@app.route('/health', methods=['GET'])
def get_health():
    return "good health"


app.run('0.0.0.0', 8080)



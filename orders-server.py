from flask import Flask

app = Flask("orderapp")

all_orders = {
    55:{'id':55, 'prod': 'milk', 'quantity':4}, 
    56:{'id':56, 'prod': 'eggs', 'quantity':2}, 
    57:{'id':57, 'prod': 'coffee', 'quantity':8} 
}

@app.route("/")
def main_error():
    result = {'msg':"root endpoint not supported"}
    return result

@app.route('/orders', methods=['GET'])
def get_all_orders():
    return all_orders
    

app.run('0.0.0.0', 8080)



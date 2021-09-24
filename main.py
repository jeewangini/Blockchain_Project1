from flask import Flask, render_template
from flask import request
import datetime as date
import time
from block import genesis_block
from mine import mine
from sync import sync
from node import blockchain
import json

app = Flask(__name__)

customer =''
amount =''

@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == "POST":
        customer = request.form.get('customer')
        amount = request.form.get('amount')
                    
   
    return render_template('index.html')

@app.route('/mine')
def add():
    data = {
            'customer' : customer,
            'amount' : amount,
            'timestamp' : date.datetime.now()
        }
    node_blocks = sync()
    if node_blocks == []:
        genesis = genesis_block()
        new_block = mine(genesis, data)
    else:
        prev_block = node_blocks[-1]
        new_block = mine(prev_block, data)
    new_block.self_save()
    return "block added"


@app.route('/view')
def view():
    python_blocks = blockchain()
    json_blocks = json.dumps(python_blocks)
    return json_blocks
    

if __name__ == '__main__':
    app.run(debug = True) 


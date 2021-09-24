from block import Block, genesis_block
from flask import Flask, render_template, request
import sync
import os
import json
from mine import mine
import datetime as date
import time

node = Flask(__name__)
print("here2")
node_blocks = sync.sync()

def dict(block): 
    info = {}
    info['index'] = str(block['index'])
    info['previous_hash'] = str(block['previous_hash'])
    info['timestamp'] = str(block['timestamp'])
    info['hash'] = str(block['hash'])
    info['data'] = str(block['data'])
    return info



def blockchain():
    print("here")
    python_blocks = []
    for block in node_blocks:
        print(block)
        node_index = str(block.index)
        block_timestamp = str(block.timestamp)
        block_data = str(block.data)
        block = {
            'index': block.index,
            'timestamp': block.timestamp,
            'data': block.data,
            'hash': block.hash,
            'previous_hash': block.previous_hash
        }
        python_blocks.append(dict(block))
    return python_blocks


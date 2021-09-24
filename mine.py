from block import Block, genesis_block
import datetime as date
import time
import sync
import json
import hashlib

NUM_ZEROES = 5

def generate_header(index, previous_hash, data, timestamp, nonce):
    return str(index) + previous_hash + str(data) + str(timestamp) + str(nonce)

def calculate_hash(index, previous_hash, data, timestamp, nonce):
    header_string  = generate_header(index, previous_hash, data, timestamp, nonce)
    sha = hashlib.sha256()
    sha.update(header_string.encode())
    return sha.hexdigest()

def mine(last_block, data):
    index = int(last_block.index) + 1
    timestamp = date.datetime.now()
    data = data
    prev_hash = last_block.hash
    nonce = 0

    block_hash = calculate_hash(index, prev_hash, data, timestamp, nonce)
    while str(block_hash[0:NUM_ZEROES]) != '0' * NUM_ZEROES:
        nonce += 1
        block_hash = calculate_hash(index, prev_hash, data, timestamp, nonce)

    block_data = {}
    block_data['index'] = index
    block_data['previous_hash'] = prev_hash
    block_data['timestamp'] = timestamp
    block_data['data'] = data 
    block_data['hash'] = block_hash
    block_data['nonce'] = nonce
    return Block(block_data)


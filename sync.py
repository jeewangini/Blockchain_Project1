from block import Block
import os 
import json
def sync():
    print("here3")
    node_blocks = []
    chaindata_dir = 'chaindata'
    print(chaindata_dir)
    if os.path.exists(chaindata_dir):
        print('here4')
        for filename in os.listdir(chaindata_dir):
            print(filename)
            if filename.endswith('.json'):
                filepath = '%s/%s' % (chaindata_dir, filename)
                print(filepath)
                with open(filepath, 'r') as block_file:
                    block_info = json.load(block_file)
                    block_object =Block(block_info)
                    node_blocks.append(block_object)
    return node_blocks
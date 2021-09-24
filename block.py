import json
import os
import datetime
import hashlib


class Block():
    def __init__(self, dictionary):
        for k, v, in dictionary.items():
            setattr(self, k, v)
            if not hasattr(self, 'nonce'):
                self.nonce = None
            if not hasattr(self, 'hash'):
                self.hash = self.create_self_hash()



    def header_string(self):
        return str(self.index) + str(self.nonce) 

    def create_self_hash(self):
        sha = hashlib.sha256()
        sha.update(self.header_string().encode())
        return sha.hexdigest()

    def self_save(self):
        chaindata_dir = 'chaindata'
        index_string = str(self.index).zfill(6)
        print(index_string)
        filename = 'chaindata/%s%s.json' %(chaindata_dir, index_string)
        print('filename')
        print(filename)
        with open(filename, 'w') as block_file:
            json.dump(self.__dict__(), block_file)

    def __dict__(self):
        info = {}
        info['index'] = str(self.index)
        info['previous_hash'] = str(self.previous_hash)
        info['timestamp'] = str(self.timestamp)
        info['hash'] = str(self.hash)
        info['data'] = str(self.data)
        return info

    def __str__(self):
        return "Block<previous_hash: %s, hash: %s>" %(self.previous_hash, self.hash)


def genesis_block():
    block_data = {}
    block_data['index'] = 0
    block_data['timestamp'] = datetime.datetime.now()
    block_data['previous_hash'] = "00"
    block_data['data'] ="f"
    block = Block(block_data)
    return block

if __name__ == '__main__':
    chaindata_dir = 'chaindata/'
    if not os.path.exists(chaindata_dir):
        os.mkdir(chaindata_dir)
    if os.listdir(chaindata_dir) == []:
        genesis = genesis_block()
        genesis.self_save()

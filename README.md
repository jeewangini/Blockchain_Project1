# Blockchain_Project1
Dexter owns the most well-known coffee shop in town, and he has a large number of friends that frequent his establishment. He keeps track of his transactions in logbooks. Because his shop is so well-known, he frequently runs out of logbooks. Dexter's buddies have access to his shop, and they would frequently remove or change their transactions from the logbook, causing him to lose money. Dexter has learned about blockchain technology and is considering applying it to his firm to increase productivity.
 
To run the application, navigate to  A1_16_1. From here, run the Python script main.py to start the application. The output window will show:

The features of the blockchain can be viewed by visiting Dexter's Cafe once the main.py script has been run.
 
The application is divided into various scripts, with each containing various methods relevant to the application and its usage:
Node.py
This script implements the “block” of the blockchain. The current implementation of the block holds information of the index, data (transaction amount), hash and time of the creation of the block. 
Index:  Every transaction has a unique ID or index.
Timestamp: It stands for the time of transaction. Every transaction ID is unique. Therefore every transaction is thus identified by the Timestamp and the index.
Data: The actual transaction amount is denoted by data. 
Hash: A hash is a function that satisfies the encrypted demands required for a blockchain computation to be solved. The hashed value will always be the same for the same data. The blockchain network's backbone is a hash.
 
 
 
 
Block.py
The class implements the basic features and functionalities of a block in a blockchain. The various functions and their uses are:
header_string() - the functions creates the header string which is of the format “indexnonce”
create_self_hash() - the function uses the hashlib library to create the hash for any particular block following the sha256 algorithm. The input to the hash function is the header string.
self_save() - the function appends the block to the preexisting blockchain. A new file is created and the data corresponding to that particular block is added to the file and names chaindata00000index and added to the list of blocks at the end.
__dict__() - the function creates a map data structure consisting of all the data of the block
genesis_block() - If the blockchain does not have any block this function creates the forest default block ie the genesis block so the further blocks can be added.


Sync.py
The sync file is used to sync the interface with all the blocks currently present in the blockchain. All the blocks are appended to node_blocks and returned when displaying all the blocks present in the blockchain.
Main.py - this file is used to host the blockchain using flask. Flask is a lightweight WSGI web application framework. It is designed to make getting started quick and easy, with the ability to scale up to complex applications. It began as a simple wrapper around Werkzeug and Jinja and has become one of the most popular Python web application frameworks.
	The different routes are used for different applications of the blockchain
@app.route('/', methods=['POST', 'GET'])
The homepage from where the user is redirected to the different applications. The page has a form that takes as input the name of the customer and the amount of money spent. Also, the page consists of two buttons - add transaction and view transaction
	Add Transaction button initiates the creation of a new block corresponding to the details entered in the form by the user. It also does the verification part using the proof of work. If the transaction is added successfully to a block and the block is added to the chain, the user is redirected to the page where the confirmation that the block has been added is shown.
	View Transaction button redirects the user to the page where all the transactions in the blockchain can be viewed.
 
@app.route('/mine')
This comes into action when the Add transaction button is clicked and the mine() function is called to perform the following actions.
 
@app.route('/view')
This is the page where the transactions are displayed. This page appears when the View transaction button is clicked.


Mine.py
               Mine.py mines the block using proof of work consensus algorithm.
               The various functionalities used are -
generate_header - Concatenates all the strings of data that contain index, previous_hash, data, timestamp, nonce 

calculate_hash - Calculates the hash of a block. The popular cryptographic hash algorithm SHA256 (Secure Hash Algorithm) is being used. SHA256 algorithm generates an almost unique, fixed-size 256-bit (32-byte) hash. Hash is so-called a one-way function. Getting data if provided with a hash and hash algorithm isn’t possible. 
encode(): Converts the string into bytes to be acceptable by the hash function.
hexdigest() :Returns the encoded data in hexadecimal format.

mine - Is used for mining the newly created block. This function uses preset values- previous hash and nonce. The idea of this method is to generate proof of work. The method takes as its parameters the set of miners available for mining. Miners try to create the difficulty hash by changing the nonce value. Here the difficulty hash is set as 5 zeroes followed by other numbers. The work done is indicated by the nonce count of every miner, and the current hash of the block is updated after every iteration according to the nonce count before finally adding the block onto the chain. This makes it more secure since the nonce count cannot be pre-determined.












             

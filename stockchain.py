"""Its Katie"""
"""Dan is in the house"""
"""Malik is aqui"""
import hashlib
import json
from time import time

class Blockchain(object):
    """An immutable, sequential chain of Blocks (records)"""
    
    def __init__(self,genesis_block = None):
        self.chain = []
        self.current_transactions = []
        
        self.add_block(proof = 100,previous_hash = 1)
        #self.genesis_block = genesis_block
        
    def __str__(self):
        """Print content of the Blockchain"""
        
        ret_str = "Inside our chain: \n"
        for blk in self.chain:
            ret_str += blk.__str__() + ", "
        
        ret_str += 50 * "*"
        ret_str += "\nCurrent transaction: \n"
        for trn in self.current_transactions:
            ret_str += trn.__str__() + ","
        return ret_str
            

    def add_block(self,proof = 0, previous_hash = None):
        #self.chain.append(blk)
        
        #Change later to keep a counter instead of checking length each time.
        blk = Block(len(self.chain)+1,time(), self.current_transactions,proof,
                    previous_hash or self.hash(self.chain[-1]))

        self.chain.append(blk)        
        
        self.current_transactions = [] #Reet current list of transactions?
        
        return blk
 
    def add_trans(self,sen,rec,amt):
        trn = Transaction(sen,rec,amt)
        self.current_transactions.append(trn)
        
        return self.last_block.idx + 1
        
#    def add_trans(self,trn):
#        self.current_transactions.append(trn)
#        
#        return self.last_block.idx + 1
        
#    def new_block(self):
#        # creates a new Block and adds it to the chain
#        pass

#    def new_transaction(self):
#        """Adds a new transaction to the list of transactions
#        
#        Input: sender (str): address of the sender
#               recipient (str): address of the recipient
#               amount (int): amount of money being sent
#               
#        Output: (int): index of the Block that will hold this transaction"""
#        
#        # adds a new transaction to the list of transactions
    
        
        pass
    
    @staticmethod
    def hash(block):
        """Masks information in 256 bits so that it is not easily readible
            Does not decrypt, only encrypts"""
        
        # Hashes a Block
        block_string = json.dumps(block.info, sort_keys = True).encode()
        return hashlib.sha256(block_string).hexdigest()
        #Hash of 256 bits
        pass

    @property
    def last_block(self):
        # Returns the last Block in the chian
        return self.chain[-1]
        
    def proof_of_work(self,last_proof):
        
        proof = 0
        while self.valid_proof(las_proof,proof) is False:
            proof += 1
            
        return proof
        
    @staticmethod
    def valid_proof(last_proof,proof):
        pass

 
class Block(object):
    """Record of information, holds the hash of the previous Block, this gives chains immutability
            If a hacker corrupts a hash, they have to change ALL subsequent blocks or else the 
            difference will be noted by holders of the blocks in the decentralized network"""
            
    def __init__(self,idx = 0,ts = 0.0,tran = None,pr = 0,ph = ""):
        
        self.idx = idx
        self.ts = ts
        self.tran = [tran]
        self.pr = pr
        self.ph = ph
                     
        self.info = {'index':idx,
                     'timestamp':ts,
                     'transactions':tran,
                     'proof':pr,
                     'previous_hash':ph}
        
        #self.trans = []
        
    def __str__(self):
        
        #ret_str = ""
        return "index:{},timestamp:{}".format(self.info['index'],self.info['timestamp'])

class Transaction(object):

    def __init__(self, sender = "Me", recipient = "You", amount = 0):

        self.sen = sender
        self.rec = recipient
        self.amt = amount
        
    def __str__(self):
        
        return "sender:{}\nrecipient:{}\namount:{}".format(self.sen,self.rec,self.amt)
        
        
def main():
    
    #trans = Transaction("8527147fe1f5426f9dd545de4b27ee00",
    #                    "a77f5cdfa2934df3954a5c7c7da5df1f", 5)

    #block = Block(1,1506057125.900785, trans, 324984774000, 
    #         "2cf24dba5fb0a30e26e83b2ac5b9e29e1b161e5c1fa7425e73043362938b9824")
             
    chain = Blockchain()
#    block = Block(1,1506057125.900785,
#            [{'sender': "8527147fe1f5426f9dd545de4b27ee00",
#             'recipient': "a77f5cdfa2934df3954a5c7c7da5df1f",
#             'amount': 5}], 324984774000, 
#             "2cf24dba5fb0a30e26e83b2ac5b9e29e1b161e5c1fa7425e73043362938b9824")
             

    chain.add_block(1,10)
    chain.add_trans("Me","You",5)
    print(chain)
    
#    block = {
#        'index': 1,
#        'timestamp': 1506057125.900785,
#        'transactions': [
#            {
#                'sender': "8527147fe1f5426f9dd545de4b27ee00",
#                'recipient': "a77f5cdfa2934df3954a5c7c7da5df1f",
#                'amount': 5,
#            }
#        ],
#        'proof': 324984774000,
#        'previous_hash': "2cf24dba5fb0a30e26e83b2ac5b9e29e1b161e5c1fa7425e73043362938b9824"
#            }
    
main()

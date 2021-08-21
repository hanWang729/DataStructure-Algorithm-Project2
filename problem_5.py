import hashlib
import datetime



class Block:

    def __init__(self, data):
        if data is None:
            data = ""
        self.timestamp = datetime.datetime.utcnow()
        self.data = data
        self.previous_hash = None
        self.hash = self.calc_hash()
        self.index = 0

    def calc_hash(self):
        sha = hashlib.sha256()
        hash_str = self.data.encode('utf-8')
        sha.update(hash_str)
        return sha.hexdigest()

    def print(self):
        print("Block: {}".format(self.index))
        print("Timestamp: {}".format(self.timestamp))
        print("Data: {}".format(self.data))
        print("Hash: {}".format(self.hash))
        print("Previous hash: {}".format(self.previous_hash))

class BlockChain:
    def __init__(self):
        self.block_chain = list()
        self.last_hash = None
        self.block_num = 0

    def append(self, block):
        block.previous_hash = self.last_hash
        block.index = self.block_num
        self.block_num += 1
        self.block_chain.append(block)
        self.last_hash = block.hash

    def print(self):
        print("*******************************************")
        print("Block Chain Size: {}".format(self.block_num))
        for b in self.block_chain:
            print("[{}, {}]".format(b.timestamp, b.data))

        for i in range(len(self.block_chain)-1, -1, -1):
            print("\n")
            b = self.block_chain[i]
            b.print()


# Test 1
block_chain = BlockChain()
block1 = Block("Test Block1")
block_chain.append(block1)
block_chain.print()
# Test 2
block2 = Block("")
block_chain.append(block2)
block_chain.print()
# Test 3
block3 = Block(None)
block_chain.append(block3)
block_chain.print()

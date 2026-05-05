import hashlib
import json
from time import time

class Blockchain:

    def __init__(self):
        self.chain = []
        self.create_block("0")

    def create_block(self, previous_hash, merkle_root=None):
        block = {
            "index": len(self.chain) + 1,
            "timestamp": time(),
            "merkle_root": merkle_root,
            "previous_hash": previous_hash
        }
        self.chain.append(block)
        return block

    def get_last_block(self):
        return self.chain[-1]

    def hash(self, block):
        return hashlib.sha256(json.dumps(block, sort_keys=True).encode()).hexdigest()

    def add_block(self, merkle_root):
        prev_block = self.get_last_block()
        prev_hash = self.hash(prev_block)
        return self.create_block(prev_hash, merkle_root)
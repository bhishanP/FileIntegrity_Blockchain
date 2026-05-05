import os
from hash_utils import calculate_file_hash
from merkle_tree import build_merkle_root

def get_hashes(folder):
    hashes = []
    for file in os.listdir(folder):
        path = os.path.join(folder, file)
        if os.path.isfile(path):
            hashes.append(calculate_file_hash(path))
    return hashes

def compute_merkle(folder):
    hashes = get_hashes(folder)
    return build_merkle_root(hashes)
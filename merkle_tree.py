import hashlib

def hash_pair(a, b):
    return hashlib.sha256((a + b).encode()).hexdigest()

def build_merkle_root(file_hashes):
    if not file_hashes:
        return None

    level = file_hashes

    while len(level) > 1:
        next_level = []

        for i in range(0, len(level), 2):
            left = level[i]
            right = level[i+1] if i+1 < len(level) else left
            next_level.append(hash_pair(left, right))

        level = next_level

    return level[0]
import os
from hash_utils import calculate_file_hash

def get_file_hash_map(folder):
    file_hash_map = {}

    for file in os.listdir(folder):
        path = os.path.join(folder, file)
        if os.path.isfile(path):
            file_hash_map[file] = calculate_file_hash(path)

    return file_hash_map


def detect_changes(folder, old_map):
    new_map = get_file_hash_map(folder)

    for file, new_hash in new_map.items():
        if file not in old_map:
            return True, f"New file added: {file}"

        if old_map[file] != new_hash:
            return True, f"Modified file: {file}"

    for file in old_map:
        if file not in new_map:
            return True, f"Deleted file: {file}"

    return False, None
from flask import Flask, render_template, redirect
from blockchain import Blockchain
from monitor import get_file_hash_map, detect_changes
from merkle_tree import build_merkle_root

app = Flask(__name__)

FOLDER = "test"

blockchain = Blockchain()

file_hash_map = get_file_hash_map(FOLDER)
current_root = build_merkle_root(list(file_hash_map.values()))
blockchain.add_block(current_root)

status = "SAFE"
changed_file = None


@app.route("/")
def index():
    global status, current_root, file_hash_map, changed_file

    changed, message = detect_changes(FOLDER, file_hash_map)

    if changed:
        status = "TAMPERED"
        changed_file = message
        file_hash_map = get_file_hash_map(FOLDER)
        current_root = build_merkle_root(list(file_hash_map.values()))
    else:
        status = "SAFE"
        changed_file = None

    return render_template(
        "index.html",
        status=status,
        root=current_root,
        chain=blockchain.get_chain(),
        changed_file=changed_file,
        is_valid=blockchain.is_chain_valid()
    )


@app.route("/add_block", methods=["POST"])
def add_block():
    global current_root
    blockchain.add_block(current_root)
    return redirect("/")


@app.route("/reset", methods=["POST"])
def reset():
    global blockchain, file_hash_map, current_root, status, changed_file

    blockchain.reset_chain()

    file_hash_map = get_file_hash_map(FOLDER)
    current_root = build_merkle_root(list(file_hash_map.values()))

    status = "SAFE"
    changed_file = None

    return redirect("/")


@app.route("/refresh")
def refresh():
    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)
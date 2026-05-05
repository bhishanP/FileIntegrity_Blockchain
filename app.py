from flask import Flask, render_template, request, redirect
from blockchain import Blockchain
from monitor import compute_merkle

app = Flask(__name__)

blockchain = Blockchain()
FOLDER = "test"

# store initial root
current_root = compute_merkle(FOLDER)
blockchain.add_block(current_root)

status = "SAFE"

@app.route("/")
def index():
    global status, current_root

    new_root = compute_merkle(FOLDER)

    if new_root != current_root:
        status = "TAMPERED"
    else:
        status = "SAFE"

    return render_template(
        "index.html",
        status=status,
        root=new_root,
        chain=blockchain.chain
    )

@app.route("/refresh")
def refresh():
    return redirect("/")

@app.route("/add_block", methods=["POST"])
def add_block():
    global current_root
    current_root = compute_merkle(FOLDER)
    blockchain.add_block(current_root)
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)
# 🔐 Blockchain-Based File Integrity Monitoring System

A Python-based mini project that uses **Blockchain + Merkle Trees** to detect file tampering and ensure data integrity, with an interactive **Flask UI** and **vis.js graph visualization**.

---

## 🚀 Features

* 🔗 **Blockchain Implementation**

  * Blocks linked using cryptographic hashes
  * Genesis block initialization
  * Chain validation support

* 🌳 **Merkle Tree Integration**

  * Efficient hashing of multiple files
  * Single root hash stored in blockchain

* 📁 **File Integrity Monitoring**

  * Detects:

    * Modified files
    * New files
    * Deleted files
  * Displays exact file affected

* 🗄️ **SQLite Persistence**

  * Blockchain stored in database (`blockchain.db`)
  * Data persists across server restarts

* 🌐 **Flask Web UI**

  * Real-time monitoring dashboard
  * Status indicators (SAFE / TAMPERED)
  * Blockchain integrity status (VALID / CORRUPTED)

* 📊 **Interactive Graph (vis.js)**

  * Visual representation of blockchain
  * Clickable nodes → view block details

* 🧹 **Reset Feature**

  * Clear blockchain and reinitialize genesis block

---

## 🧠 Concepts Covered

* Blockchain Architecture
* Cryptographic Hash Functions (SHA-256)
* Merkle Trees
* Data Integrity & Tamper Detection
* Decentralization Concepts (simulation)

---

## 🏗️ Project Structure

```
FileIntegrity_Blockchain/
│
├── app.py                 # Flask app
├── blockchain.py          # Blockchain logic (SQLite)
├── db.py                  # Database setup
├── hash_utils.py          # SHA256 hashing
├── merkle_tree.py         # Merkle tree implementation
├── monitor.py             # File change detection
├── requirements.txt
│
├── templates/
│   └── index.html         # Frontend UI
│
├── static/
│   ├── style.css          # Styling
│   └── graph.js           # vis.js graph logic
│
└── test_files/            # Files to monitor
```

---

## ⚙️ Installation & Setup

### 1️⃣ Clone Repository

```
git clone https://github.com/bhishanP/FileIntegrity_Blockchain.git
cd FileIntegrity_Blockchain
```

### 2️⃣ Install Dependencies

```
pip install -r requirements.txt
```

### 3️⃣ Run Application

```
python app.py
```

### 4️⃣ Open Browser

```
http://127.0.0.1:5000
```

---

## 🧪 How It Works

1. Files in `test_files/` are hashed using SHA256
2. Hashes are combined using a **Merkle Tree**
3. Merkle root is stored in a blockchain block
4. On each refresh:

   * File hashes are recomputed
   * Changes are detected
   * Blockchain integrity is validated

---

## 🎯 Demo Steps

1. Run the application
2. Observe **SAFE** status
3. Modify any file in `test_files/`
4. Refresh page
5. System shows:

   * 🔴 **TAMPERED**
   * ⚠️ Modified file name

---

## 🧠 Blockchain Validation

The system verifies:

```
current_block.previous_hash == hash(previous_block)
```

If mismatch occurs → **CORRUPTED**

---

## 📊 Graph Visualization

* Each block = node
* Links = hash connections
* Click node → view details

---

## 🧹 Reset Blockchain

Use the **Reset Chain** button to:

* Clear database
* Recreate Genesis block

---

## 📌 Future Improvements

* Real-time monitoring (auto-refresh)
* Multi-user system
* Deployment (cloud hosting)
* Smart contract integration

---

## 🎓 Academic Relevance

This project aligns with:

* Blockchain Essentials
* Cryptographic Constructs
* Merkle Trees
* Transactions & Immutability

---

## 👨‍💻 Author

**Bhishan Pangeni**

---

## 📜 License

This project is for educational purposes.

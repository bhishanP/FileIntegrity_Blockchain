import hashlib
import json
from time import time
from db import get_connection, init_db


class Blockchain:

    def __init__(self):
        init_db()
        self.ensure_genesis()

    def hash(self, block):
        return hashlib.sha256(
            json.dumps(block, sort_keys=True).encode()
        ).hexdigest()

    def ensure_genesis(self):
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("SELECT COUNT(*) FROM blocks")
        count = cursor.fetchone()[0]

        if count == 0:
            self.create_block("0", "GENESIS")

        conn.close()

    def create_block(self, previous_hash, merkle_root):
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("SELECT COUNT(*) FROM blocks")
        index = cursor.fetchone()[0] + 1

        timestamp = time()

        cursor.execute("""
            INSERT INTO blocks (idx, timestamp, merkle_root, previous_hash)
            VALUES (?, ?, ?, ?)
        """, (index, timestamp, merkle_root, previous_hash))

        conn.commit()
        conn.close()

    def get_last_block(self):
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("""
            SELECT idx, timestamp, merkle_root, previous_hash
            FROM blocks ORDER BY idx DESC LIMIT 1
        """)

        row = cursor.fetchone()
        conn.close()

        return {
            "index": row[0],
            "timestamp": row[1],
            "merkle_root": row[2],
            "previous_hash": row[3]
        }

    def add_block(self, merkle_root):
        last_block = self.get_last_block()
        prev_hash = self.hash(last_block)
        self.create_block(prev_hash, merkle_root)

    def get_chain(self):
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("""
            SELECT idx, timestamp, merkle_root, previous_hash
            FROM blocks ORDER BY idx
        """)

        rows = cursor.fetchall()
        conn.close()

        return [
            {
                "index": row[0],
                "timestamp": row[1],
                "merkle_root": row[2],
                "previous_hash": row[3]
            }
            for row in rows
        ]

    def reset_chain(self):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM blocks")
        conn.commit()
        conn.close()
        self.ensure_genesis()

    def is_chain_valid(self):
        chain = self.get_chain()

        for i in range(1, len(chain)):
            prev = chain[i - 1]
            curr = chain[i]

            if curr["previous_hash"] != self.hash(prev):
                return False

        return True
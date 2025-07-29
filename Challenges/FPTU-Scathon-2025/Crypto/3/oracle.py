from flask import Flask, request, jsonify
from Crypto.Cipher import AES
import os, base64

app = Flask(__name__)
KEY = bytes.fromhex("1db5418423aba385ceabca806aded47d")
NONCE = bytes.fromhex("85dc878d16717b74")  # same nonce reused!

def aes_ctr_encrypt(data: bytes) -> bytes:
    cipher = AES.new(KEY, AES.MODE_CTR, nonce=NONCE)
    return cipher.encrypt(data)

@app.route('/encrypt', methods=['POST'])
def encrypt():
    data = request.json.get('data', '').encode()
    ct = aes_ctr_encrypt(data)
    return jsonify(ciphertext=ct.hex())

if __name__ == '__main__':
    app.run(port=5000)
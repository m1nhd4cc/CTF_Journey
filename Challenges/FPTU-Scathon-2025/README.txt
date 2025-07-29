CTR Reuse Oracle – Medium Crypto Challenge
=========================================

Goal
----
Recover the flag from `ciphertext.bin`.

Scenario
--------
A developer mistakenly **reuses the same nonce** for AES‑CTR encryption.
You have two powers:
1. A ciphertext (`ciphertext.bin`) that contains a secret message with the flag.
2. An **encryption oracle** (`oracle.py`) that will encrypt *any plaintext you supply* using **the same key and the SAME nonce**.

Because AES‑CTR is a stream cipher (keystream XOR), reusing the nonce leaks the keystream.
By querying the oracle with chosen plaintexts, you can reconstruct the keystream and decrypt `ciphertext.bin`.

Flag format: FUSec2025{...} (already inside the message).

Files
-----
* `ciphertext.bin` – secret ciphertext
* `oracle.py`      – Flask server providing `/encrypt` endpoint
* `README.txt`     – this guide

Quick Start
-----------
```bash
pip install flask pycryptodome requests

# Terminal 1 – start oracle
python oracle.py

# Terminal 2 – example usage
python - <<'PY'
import requests, sys, os
ct = bytes.fromhex(open("ciphertext.bin","rb").read().hex())
# Step 1: ask oracle to encrypt zeros of same length → gives keystream
zeros = b'\x00'*len(ct)
ks_hex = requests.post("http://127.0.0.1:5000/encrypt", json={"data": zeros.decode('latin1')}).json()['ciphertext']
keystream = bytes.fromhex(ks_hex)
pt = bytes(a ^ b for a,b in zip(ct, keystream))
print("Decrypted:", pt.decode())
PY
```

That script prints the original message along with the flag.

Good luck!
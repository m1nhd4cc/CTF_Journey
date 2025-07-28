# get_flag.py
import math

# 1) paste your hex‐modulus here (no “0x”, no spaces)
hexN = "28f8f1d3384879ece1a0e4fa990fdee59f83bccf5fc41d2783a657e3cad4f181f0a1c2b7f61e0f391b7b11afc502b070e555a39c14d9b3eae6c89e330e0f68fb77892438e93e6c1cc94869ce80525b59d097c0c783161a148d5370fd4ade1e65f49060a78bd722e0fa4ed624f3747a4d6190122fd1b778ca5bbbd85ca04cae13e197be5275d4c5811a2a2df186e374ad5f8b11f6f501c32cdaa6ac11707796395c2a957b5c7398401c9b9be06c18ddb97981c5ebf1ece7564f42b844370506a0bc9dfc2ae54649ab05ef483981e7d7ecd6d6dbbaacdc4e809cc54afac4ce308943c7c5e1"

# 2) build N as an integer
N = int(hexN, 16)

# 3) compute s = floor(sqrt(N))
s = math.isqrt(N)

# 4) turn s into bytes; pad hex to even length
h = hex(s)[2:]
if len(h) % 2:
    h = "0" + h
data = bytes.fromhex(h)

# 5) print the flag
print(data.decode('ascii'))
from cryptography.hazmat.primitives import serialization

with open("ssh_host_rsa_key.pub", "rb") as f:
    key_data = f.read()

public_key = serialization.load_pem_public_key(key_data)
public_numbers = public_key.public_numbers()

e = public_numbers.e
n = public_numbers.n

print(f"e = {e}")
print(f"n = {n}")

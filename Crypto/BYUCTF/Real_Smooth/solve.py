from pwn import *
from binascii import unhexlify

# Known plaintexts
pt1 = b"Slide to the left"
pt2 = b"Slide to the right"
target = b"Criss cross, criss cross"

# Connect to remote server
p = remote("smooth.chal.cyberjousting.com", 1350)

# Receive two ciphertext lines
ct1 = p.recvline().strip().decode()
ct2 = p.recvline().strip().decode()

# Convert from hex
ct1_bytes = bytes.fromhex(ct1)
ct2_bytes = bytes.fromhex(ct2)

# Recover keystreams
keystream1 = bytes([c ^ p for c, p in zip(ct1_bytes, pt1)])
keystream2 = bytes([c ^ p for c, p in zip(ct2_bytes, pt2)])

# Combine
full_keystream = keystream1 + keystream2

# Encrypt target
cipher = bytes([p ^ k for p, k in zip(target, full_keystream)])

# Send encrypted response
p.sendline(cipher.hex())

# Get result
p.interactive()

#byuctf{ch4ch4_sl1d3?...n0,ch4ch4_b1tfl1p}
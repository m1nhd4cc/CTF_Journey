import pwn
from binascii import unhexlify, hexlify

# Connect to the remote server
host = "90ec0cbf20818aa01edb732a-1024-intro-crypto-1.challenge.cscg.live"
port = 1337

# Setup pwntools context
pwn.context.log_level = 'error'  # or 'debug' for full logs

r = pwn.remote(host, port, ssl=True)

# Step 1: Receive the initial prompt
r.recvuntil(b"Enter some plaintext (hex): ")

# Step 2: Send 32 bytes of known plaintext (all zeroes)
plaintext = b'\x00' * 128
r.sendline(plaintext.hex().encode())

# Step 3: Collect 255 ciphertexts and extract keystreams
keystreams = {}
for i in range(255):
    line = r.recvline()
    index = int(line[11:14])  # parse the counter index
    ct_hex = line.strip().split(b': ')[1]
    ct_bytes = unhexlify(ct_hex)
    keystreams[index] = ct_bytes  # Since plaintext is all 0s: ct = keystream

# Step 4: Get final flag ciphertext
line = r.recvline()
assert line.startswith(b"Flag: ")
flag_ct = unhexlify(line.strip().split(b": ")[1])

# Step 5: Try all keystreams
print("\n[+] Trying all keystreams to recover the flag...\n")
for i in range(255):
    ks = keystreams[i]
    guess = bytes([a ^ b for a, b in zip(flag_ct, ks)])
    if guess.startswith(b"CSC{") or guess.startswith(b"CSCG{"):
        print(f"[!] Found possible flag (counter {i}): {guess.decode()}")
        break
else:
    print("[-] Flag not found. Maybe increase plaintext size?")


#CSCG{turns_out_that_once_in_nonce_is_actually_important_who'd've_thought?}

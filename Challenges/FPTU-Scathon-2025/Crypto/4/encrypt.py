import random

def secret_shuffle_seed():
    return [(i * 73 + 41) % 256 for i in range(256)]

def mix_state(secret_key):
    box = secret_shuffle_seed()
    x = 0
    for y in range(256):
        x = (x + box[y] + ord(secret_key[y % len(secret_key)])) % 256
        box[y], box[x] = box[x], box[y]
    return box

def drip_bytes(box, data_len):
    a = b = 0
    flow = []
    for _ in range(data_len):
        a = (a + 1) % 256
        b = (b + box[a]) % 256
        box[a], box[b] = box[b], box[a]
        flow.append(box[(box[a] + box[b]) % 256])
    return flow

def obfuscate(message, secret_key):
    box = mix_state(secret_key)
    flow = drip_bytes(box, len(message))
    return bytes([ord(c) ^ s for c, s in zip(message, flow)])

if __name__ == "__main__":
    hidden_message = "FUSec2025{jU5t_4_L1ttl3_Shuffl3}"
    key = "twister"
    output = obfuscate(hidden_message, key)
    with open("ciphertext.txt", "wb") as f:
        f.write(b"###" + output + b"$$$")  # Added noise padding
    print("Encryption complete. Ciphertext saved to ciphertext.txt")

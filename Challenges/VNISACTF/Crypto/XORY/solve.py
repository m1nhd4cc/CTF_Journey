import itertools as it

def xor(a, b):
    assert len(a) > len(b)
    return bytes([i^j for i, j in zip(a, it.cycle(b))])

# known plaintext attack on XOR
enc = bytes.fromhex('784af066014241837d0d082cec58610d72ec1e346660835a0d527783580d6f52e65258')
known = b'ASCIS{'
key = xor(enc, known)[:len(known)-1]
flag = xor(enc, key)
print(flag)
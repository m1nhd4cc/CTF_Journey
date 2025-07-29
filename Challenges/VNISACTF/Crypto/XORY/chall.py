import random, os

def xory(msg, key):
    ct = []
    for i in range(len(msg)):
        ct.append(msg[i] ^ key[i%len(key)])
    return bytes(ct)

#KEY = random.randbytes(5)
KEY = os.urandom(5)
FLAG = open('../flag.txt', 'rb').read()

cipher = xory(FLAG, KEY)
print(cipher.hex())
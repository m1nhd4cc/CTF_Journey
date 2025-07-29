import random, os

def xory(msg, key):
    ct = []
    for i in range(len(msg)):
        ct.append(msg[i] ^ key[i%len(key)])
    return bytes(ct)

#KEY = random.randbytes(5)
KEY = os.urandom(5)
FLAG = open('../flag.txt', 'rb').read()
cipher= ba35f89312c933e1d97fa6168ddc21a650d8b733c914e18324c916e1af0eac1c
cipher = xory(FLAG, KEY)
print(cipher.hex())

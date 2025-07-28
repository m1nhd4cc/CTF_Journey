import gostcrypto
from secret import key
from Crypto.Util.Padding import pad

with open("flag.txt", "rb") as f:
    flag = bytearray(f.read())

try:
    plaintext = bytearray.fromhex(input("Plaintext (hex): "))
    plaintext = pad(plaintext + flag, 16)

    cipher = gostcrypto.gostcipher.new('kuznechik', key, gostcrypto.gostcipher.MODE_ECB)
    ciphertext = cipher.encrypt(plaintext)
    print(ciphertext.hex())
except:
    print("Eh!")
    exit(0)
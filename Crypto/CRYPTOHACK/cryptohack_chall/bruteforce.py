from Crypto.Cipher import AES
import hashlib

ct = bytes.fromhex('c92b7734070205bdf6c0087a751466ec13ae15e6f1bcdd3f3a535ec0f4bbae66')
with open("words.txt") as f:
    words = [w.strip() for w in f.readlines()]

for keyword in words:
    KEY = hashlib.md5(keyword.encode()).digest()
    cipher = AES.new(KEY, AES.MODE_ECB)
    pt = cipher.decrypt(ct)
    if pt[:6] == b'crypto':
        print("keyword:",keyword)
        print("hash:",KEY.hex())
        print(pt)
        break

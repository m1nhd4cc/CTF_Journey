#!/usr/bin/env python3
from Crypto.Util.number  import long_to_bytes
from Crypto.Cipher       import AES
from Crypto.Util.Padding import unpad

# public parameters
g = 3
p = 121407847840823587654648673057258513248513248172487324370407391241175652533523276605532412599555241774504967764519702094283197762278545483713873101436663001473945726106157159264352878998534133035299601861808839807763182625559052896295039354029361792893109774218584502647139466059910154701304129191164513825925289381

# 48‐byte ciphertext from the challenge
ct = b'S\x00\xe7%\xcd\xec\xad\x9a\xe1lO\x80\xd6\r\xa5\x00\x19Y\x18\x7f\xa1\x9cx\x98\xb08n~-\rj2\xd4d\xd2\xda\xa6\xd0\r#7\xee-\\\xb4\x10\x98\x8f'

def try_decrypt_with_a(a):
    raw = long_to_bytes(a)
    if len(raw) < 16:
        return None
    key = raw[:16]
    cipher = AES.new(key, AES.MODE_ECB)
    pt = cipher.decrypt(ct)
    try:
        return unpad(pt, AES.block_size)
    except ValueError:
        return None

print("[*] Brute-forcing k*(p-1) …")
for k in range(1, 5001):
    a = k * (p - 1)
    pt = try_decrypt_with_a(a)
    if pt is not None:
        print(f"[+] Success with k = {k}")
        print(f"[+] a = {a}")
        print(f"[+] AES key (hex): {long_to_bytes(a)[:16].hex()}")
        print(f"[+] Plaintext: {pt!r}")
        break
else:
    print("[-] Didn't find a valid k up to 5000. Increase the bound if needed.")



# #python3 exploit.py
# [*] Brute-forcing k*(p-1) …
# [+] Success with k = 7
# [+] a = 849854934885765113582540711400809592739592737207411270592851738688229567734662936238726888196886692421534774351637914659982384335949818385997111710056641010317620082743100114850470152989738931247097213032661878654342278378913370274065275478205532550251768419530091518529976262419371082909128904338151596781477025660
# [+] AES key (hex): 4822b2ff72b6a95311583c3827d1bd5e
# [+] Plaintext: b'\xe2T\xcb\xb5\xe1\x0cu\xb4x[\xd6zY\x8f\xa1]\x8e\x8egr\x80\xb8&\n\xac\xe1_\x94\x0e\x8e6\xc2"n3\xbb&\x89\x18U\x1d;:EmT\xd4'


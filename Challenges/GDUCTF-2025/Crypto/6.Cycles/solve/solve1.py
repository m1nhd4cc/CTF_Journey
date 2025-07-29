#!/usr/bin/env python3
from Crypto.Util.number import long_to_bytes
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad

# Public parameters from challenge
g = 3
p = 121407847840823587654648673057258513248172487324370407391241175652533523276605532412599555241774504967764519702094283197762278545483713873101436663001473945726106157159264352878998534133035299601861808839807763182625559052896295039354029361792893109774218584502647139466059910154701304129191164513825925289381

ciphertext = b'\xd1R\xb2\xb1\x1f\x9d\xbe\xfd\xe94\x84\x8c;\xcc\xc2\x95\xe3:\xf8 \x9d\xbfT\xba\xf8H<n\xdb\x86l\x10\xfdD\xb8\x1f\x12E1\xd4\xda\xe4\xa0\xd7\xda\t\x90f'

def try_decrypt_with_a(a):
    raw = long_to_bytes(a)
    if len(raw) < 16:
        return None
    key = raw[:16]
    cipher = AES.new(key, AES.MODE_ECB)
    pt = cipher.decrypt(ciphertext)
    try:
        return unpad(pt, AES.block_size)
    except ValueError:
        return None

print("[*] Brute-forcing a = k*(p-1) …")
for k in range(1, 10000):
    a = k * (p - 1)
    pt = try_decrypt_with_a(a)
    if pt is not None:
        print(f"[+] Success with k = {k}")
        print(f"[+] a = {a}")
        print(f"[+] AES key (hex): {long_to_bytes(a)[:16].hex()}")
        print(f"[+] Plaintext (raw): {pt!r}")
        try:
            print(f"[+] Flag (utf-8): {pt.decode()}")
        except UnicodeDecodeError:
            print("[!] Could not decode as UTF-8. Try manual inspection.")
        break
else:
    print("[-] Didn't find a valid k up to 10000. Increase bound if needed.")

# [*] Brute-forcing a = k*(p-1) …
# [+] Success with k = 1
# [+] a = 121407847840823587654648673057258513248172487324370407391241175652533523276605532412599555241774504967764519702094283197762278545483713873101436663001473945726106157159264352878998534133035299601861808839807763182625559052896295039354029361792893109774218584502647139466059910154701304129191164513825925289380
# [+] AES key (hex): ace3f8bd3322cf46e6c72218b82c2588
# [+] Plaintext (raw): b'CTF{1t_4lw4ys_c0m3s_b4ck_t0_1_21bcd6}'
# [+] Flag (utf-8): CTF{1t_4lw4ys_c0m3s_b4ck_t0_1_21bcd6}
   
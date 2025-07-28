#!/usr/bin/env python3
from Crypto.Util.number import long_to_bytes
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad

# Public parameters from challenge
g = 3
p = 121407847840823587654648673057258513248172487324370407391241175652533523276605532412599555241774504967764519702094283197762278545483713873101436663001473945726106157159264352878998534133035299601861808839807763182625559052896295039354029361792893109774218584502647139466059910154701304129191164513825925289381

ciphertext = b'S\x00\xe7%\xcd\xec\xad\x9a\xe1lO\x80\xd6\r\xa5\x00\x19Y\x18\x7f\xa1\x9cx\x98\xb08n~-\rj2\xd4d\xd2\xda\xa6\xd0\r#7\xee-\\\xb4\x10\x98\x8f'

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
# [+] Success with k = 29
# [+] a = 3520827587383884041984811518660496884197002132406741814345994093923472175021560439965387102011460644065171071360734212735106077819027702319941663227042744426057078557618666233490957489858023688453992456354425132296141212533992556141266851491993900183452338950576767044515737394486337819746543770900951833392020
# [+] AES key (hex): 1395d32d6ecaf17b08248edcccdd0040
# [+] Plaintext (raw): b'byuctf{1t_4lw4ys_c0m3s_b4ck_t0_1_21bcd6}'
# [+] Flag (utf-8): byuctf{1t_4lw4ys_c0m3s_b4ck_t0_1_21bcd6}

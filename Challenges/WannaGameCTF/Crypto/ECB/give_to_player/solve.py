from pwn import *
import string

char_set = set(string.ascii_letters + string.digits + "{}_@")

len_flag = 31
flag = b''
for i in range(len_flag):
    conn = remote("chall.w1playground.com", 24777)
    conn.recvuntil(": ")

    test = "0" * (len_flag - len(flag))
    test_encoded = test.encode()
    conn.sendline(test_encoded.hex())

    cur = conn.recvline()
    cur = bytes.fromhex(cur.decode())

    conn.close()

    for ch in char_set:
        conn = remote("chall.w1playground.com", 24777)
        conn.recvuntil(": ")

        newpat = test.encode() + flag + ch.encode()
        conn.sendline(newpat.hex())

        res = conn.recvline().decode()
        res = bytes.fromhex(res)

        conn.close()

        if cur[:len(newpat)] == res[:len(newpat)]:
            flag += ch.encode()
            break

    if flag[-1] == b"}":
        break

print()
print(f"Flag: {flag}")
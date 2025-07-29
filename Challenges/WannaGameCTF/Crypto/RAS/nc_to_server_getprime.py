from pwn import *
from tqdm import tqdm 
from ast import literal_eval
from math import gcd
from Crypto.Util.number import getPrime, inverse

def chinese_remainder_theorem(remainders, moduli):
    total = 0
    product = 1
    
    for modulus in moduli:
        product *= modulus
    
    for remainder, modulus in zip(remainders, moduli):
        p = product // modulus
        total += remainder * p * pow(p, -1, modulus)
    
    return total % product

io = remote("154.26.136.227", 41214)
ps = []
ess = []
css = []

for _ in tqdm(range(100)):
    p = getPrime(256)
    q = getPrime(256)
    io.sendline(b"1")
    io.sendline((str(p) + "," + str(q)).encode())

    io.sendline(b"2")
    es = []
    cs = []
    check = True
    io.recvuntil(b'separated by comma: > ')
    for _ in range(3):
        datas = literal_eval(io.recvline()[:-1].decode())
        e, c = datas
        es.append(e)
        cs.append(c)
        if gcd(e, (p-1)) != 1:
            check = False
            break
        
    if check:
        ps.append(p)
        ess.append(es)
        css.append(cs)

plaintext_1 = []
plaintext_2 = []
plaintext_3 = []

for i in range(len(ps)):
    p = ps[i]
    es = ess[i]
    cs = css[i]
    e0, e1, e2 = es[0], es[1], es[2]
    c0, c1, c2 = cs[0], cs[1], cs[2]
    d0, d1, d2 = inverse(e0,p-1), inverse(e1,p-1), inverse(e2,p-1)
    p0, p1, p2 = pow(c0,d0,p), pow(c1,d1,p), pow(c2,d2,p)
    
    plaintext_1.append(p0)
    plaintext_2.append(p1)
    plaintext_3.append(p2)

# Sử dụng CRT tự implement thay vì sage
m1 = chinese_remainder_theorem(plaintext_1, ps)
m2 = chinese_remainder_theorem(plaintext_2, ps)
m3 = chinese_remainder_theorem(plaintext_3, ps)

print(m1, m2, m3)

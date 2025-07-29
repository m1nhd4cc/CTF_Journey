from Crypto.Util.number import long_to_bytes, inverse
from sympy import factorint
n = #<số rất dài trong output.txt>
e = 65537
c = #<flag (số rất dài) trong output.txt>
# 1. Phân tích n
factors = factorint(n)  # {p1: e1, p2: e2, ...}
# 2. Tính phi(n)
phi = 1
for p, exp in factors.items():
    phi *= (p**exp - p**(exp-1))
# 3. Tính private key d
d = inverse(e, phi)
# 4. Giải mã
m = pow(c, d, n)
print(long_to_bytes(m))

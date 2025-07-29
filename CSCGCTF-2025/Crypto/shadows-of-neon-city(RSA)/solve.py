# n = 221541797339534473245329129302928044909
# e = 65537
# cipher (base64) = hHiH/n4zALwKrj57hzUoZg==


from sympy import factorint, mod_inverse
import base64

# Given values
n = 221541797339534473245329129302928044909
e = 65537
cipher_b64 = "hHiH/n4zALwKrj57hzUoZg=="

# Step 1: Decode base64 cipher
c = int.from_bytes(base64.b64decode(cipher_b64), "big")

# Step 2: Factor n
factors = factorint(n)
p, q = list(factors.keys())

# Step 3: Compute φ(n)
phi = (p - 1) * (q - 1)

# Step 4: Compute private exponent d
d = mod_inverse(e, phi)

# Step 5: Decrypt ciphertext
m = pow(c, d, n)

# Step 6: Convert to plaintext
plaintext_bytes = m.to_bytes((m.bit_length() + 7) // 8, 'big')
print("Decrypted password:", plaintext_bytes.decode())



#Decrypted password: 3f96f9659bf7
# Enter password:
# 3f96f9659bf7
# V, inject this code into the mainframe backdoor: dach2025{curs3d_RSA_1s_curs3d_2124214}
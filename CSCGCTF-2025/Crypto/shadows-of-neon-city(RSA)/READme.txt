Description
I cracked the shard's stego layers and extracted the relevant data. Thought it'd be a piece of cake, but it's a bit more involved. We don't have a direct private key, just a public key and the encrypted payload. The suits at AstraCorp might have gotten lazy—they used a small RSA modulus

----------- SECRET MESSAGE FROM NEON CITY MAYOR -----------
n = 221541797339534473245329129302928044909
e = 65537
cipher = hHiH/n4zALwKrj57hzUoZg==

Given:

n = p * q         # both p, q are 64-bit primes
e = 65537         # standard public exponent
c = ciphertext    # encrypted password as integer

We’ll:
Decode the base64 cipher to an integer c.
Factor n to get p and q.
Compute φ(n) = (p-1)(q-1)
Compute d = e⁻¹ mod φ(n)
Decrypt: m = cᵈ mod n
Convert m to bytes → secret message



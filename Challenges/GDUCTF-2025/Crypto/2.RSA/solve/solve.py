# Complete script to solve the "subprime" challenge

from sympy import factorint, mod_inverse

def rsa_decrypt(e, n, ciphertext):
    # Step 1: Factor n
    factors = factorint(n)
    p, q = list(factors.keys())

    # Step 2: Compute phi(n)
    phi_n = (p - 1) * (q - 1)

    # Step 3: Compute private exponent d
    d = mod_inverse(e, phi_n)

    # Step 4: Decrypt each ciphertext element
    plaintext_numbers = [pow(c, d, n) for c in ciphertext]

    # Step 5: Convert decrypted numbers to characters
    plaintext = ''.join(chr(num) for num in plaintext_numbers)
    
    return plaintext

if __name__ == "__main__":
    # Given values
    e = 1009
    n = 98563159
    ciphertext = [
        23637004, 83925846, 2209113, 27583995, 30323096, 31771886, 30323096,
        75901128, 31771886, 53482472, 97809030, 69683388, 68450410, 39905961,
        75846723, 75901128, 53482472, 56293282, 69683388, 68450410, 63432789,
        9450820, 81966837
    ]

    # Decrypt
    flag = rsa_decrypt(e, n, ciphertext)
    print(flag)

#CTF{n0n_0pt!m@l_pR!m3$}
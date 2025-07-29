from pwn import *
from math import gcd
import re

def main():
    residues = [4, 9, 16, 25, 36, 49, 64, 81, 100]
    conn = remote('smiley.cat', 34987)
    multiples = []
    
    # Skip initial prompt
    conn.recvuntil(b">>> ")
    
    # Step 1: Recover modulus n
    for x in residues:
        roots = set()
        for _ in range(5):
            conn.sendline(str(x))
            root_line = conn.recvline().decode().strip()
            # Skip next prompt
            conn.recvuntil(b">>> ")
            roots.add(int(root_line))
        
        # Compute multiples of n from root differences
        roots_list = list(roots)
        for r in roots_list:
            d1 = r * r - x
            if d1 != 0:
                multiples.append(abs(d1))
        for i in range(len(roots_list)):
            for j in range(i + 1, len(roots_list)):
                d2 = abs(roots_list[i] ** 2 - roots_list[j] ** 2)
                multiples.append(d2)
    
    # Compute GCD of all multiples to get n
    candidate_n = 0
    for d_val in multiples:
        candidate_n = gcd(candidate_n, d_val)
    
    # Step 2: Factor n using root differences
    p = None
    for residue in residues:
        roots = set()
        for _ in range(5):
            conn.sendline(str(residue))
            root_line = conn.recvline().decode().strip()
            conn.recvuntil(b">>> ")
            roots.add(int(root_line))
        
        roots_list = list(roots)
        for i in range(len(roots_list)):
            for j in range(i + 1, len(roots_list)):
                g_val = gcd(roots_list[i] - roots_list[j], candidate_n)
                if 1 < g_val < candidate_n:
                    p = g_val
                    break
            if p:
                break
        if p:
            break
    
    if not p:
        print("Failed to factor modulus")
        conn.close()
        return
    
    # Compute RSA parameters
    q = candidate_n // p
    e_val = 65537
    phi = (p - 1) * (q - 1)
    d = pow(e_val, -1, phi)
    
    # Break out of oracle loop
    conn.sendline("done")
    conn.recvuntil(b"m = ")
    m = int(conn.recvline().decode().strip())
    
    # Skip signature prompt
    conn.recvuntil(b">>> ")
    
    # Compute and send signature
    s = pow(m, d, candidate_n)
    conn.sendline(str(s))
    
    # Get flag
    print(conn.recvline().decode().strip())
    conn.close()

if __name__ == "__main__":
    main()
    

# .;,;.{squares_as_a_service_est_like_the_dawn_of_time}

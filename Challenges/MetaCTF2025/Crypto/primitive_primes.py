def egcd(a, b):
    x,y, u,v = 0,1, 1,0
    while a != 0:
        q, r = b//a, b%a
        m, n = x-u*q, y-v*q
        b,a, x,y, u,v = a,r, u,v, m,n
        gcd = b
    return gcd, x, y

def main():

#################################################
    # CTF TASK 1 - Find p and q
#################################################

    # p * q = n
    n = 305127521
    # What is p and q?
    p = 0 #Change this value from 0 to a factor of n
    q = 0 #Change this value from 0 to a factor of n

    # Checkpoint 1
    if ((p * q) == n):
        print("Excellent, you found p and q!")
    else:
        print("Hmm, " + str(p) + " * " + str(q) + " doesn't seem to equal " + str(n))
        print("Exiting...")
        exit()

    # Now that we have p and q, we can calculate phi!
    phi = (p-1) * (q-1)
    e = 43 #From our public key

    # We will now use the Extended Euclidean algorithm to find d
    gcd, a, b = egcd(e, phi)
    d = a
    print("\nBased on p and q, you also have this value for d:\n" + str(d));

#################################################
    # CTF TASK 2 - Decrypt the ciphertext
#################################################

    # Ciphertext
    ct = [59742575,131625273,120376065,264043389,264043389,297186533,204523531,114463201,115812863,183156843,155097359,264043389,131625273,204523531,120376065,59742575,115812863,276605528,73775441,183156843,131625273,276605528,115812863,139940843]

    # You will need to write some simple math code
    # to get the plaintext from the ciphertext
    # Hint 1: You will need d
    # Hint 2: Use the Python function pow() for fast exponentiation



if __name__ == "__main__":
    main()

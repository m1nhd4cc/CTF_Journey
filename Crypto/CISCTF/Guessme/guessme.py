from secp256k1 import *
import secrets
from hashlib import sha256
from flag import FLAG
import json


def gen_publickey(a, gen_proof=False):  # generate public key with a Schnorr proof
    A = multiply(G, a)
    if gen_proof:
        k = secrets.randbelow(N)
        R = multiply(G, k)
        e = int(sha256((str(P) + str(Gx) + str(Gy) +
                str(A[0]) + str(A[1]) + str(R[0]) + str(R[1])).encode()).hexdigest(), 16)
        z = (e*a + k) % N
        assert multiply(G, z) == add(multiply(A, e), R)
        return A, (R, z)
    return A


def verify_publickey(A, proof):
    R, z = proof
    e = int(sha256((str(P) + str(Gx) + str(Gy) +
            str(A[0]) + str(A[1]) + str(R[0]) + str(R[1])).encode()).hexdigest(), 16)
    return multiply(G, z) == add(multiply(A, e), R)


def round(b):
    print("Give me your public key and its Schnorr proof.")
    user_input = input()
    user_input = json.loads(user_input)
    A = user_input["publickey"]
    proof = user_input["proof"]
    assert verify_publickey(A, proof)
    bit = secrets.randbits(1)
    if bit:
        B = add(multiply(G, b), A)
    else:
        B = multiply(G, b)
    print(f"B = {B}")
    print("Guess my bit.")
    user_input = input()
    user_input = json.loads(user_input)
    guess = user_input["bit"]
    if guess == bit:
        return True
    else:
        return False


if __name__ == "__main__":
    for i in range(1, 129):
        try:
            print(f"Round [{i}/128]")
            res = round(secrets.randbelow(N))
            if not res:
                break
        except:
            break
    if i == 128:
        print(FLAG)

from Crypto.PublicKey import RSA

# Import the RSA key from a file
with open('2048b-rsa-example-cert_3220bd92e30015fe4fbeb84a755e7ca5.der', 'rb') as f:
    public_key_der = f.read()

public_key = RSA.import_key(public_key_der)
print(public_key.n)

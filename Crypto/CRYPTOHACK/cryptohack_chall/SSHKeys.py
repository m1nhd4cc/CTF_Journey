from Crypto.PublicKey import RSA
with open('bruce_rsa_6e7ecd53b443a97013397b1a1ea30e14.pub',"rb") as f:
    public_key =f.read()
public_data = RSA.importKey(public_key)
print(public_data.n)

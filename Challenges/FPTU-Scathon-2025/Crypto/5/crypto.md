from Crypto.Cipher import AES, PKCS1_OAEP
from Crypto.PublicKey import RSA
from Crypto.Util.Padding import pad, unpad
import base64
import json
import os

def generate_rsa_keypair():
    key_size = 2048
    key = RSA.generate(key_size)
    private_key = key
    public_key = key.publickey()
    return private_key, public_key

def aes_encrypt(plaintext, key, iv):
    cipher = AES.new(key, AES.MODE_CBC, iv)
    ciphertext = cipher.encrypt(pad(plaintext, AES.block_size))
    return ciphertext

def rsa_encrypt(data, public_key):
    cipher_rsa = PKCS1_OAEP.new(public_key)
    encrypted_data = cipher_rsa.encrypt(data)
    return encrypted_data

def hybrid_encrypt(flag, public_key):
    plaintext = flag.encode()
    aes_key = os.urandom(32)
    iv = os.urandom(16)
    ciphertext_aes = aes_encrypt(plaintext, aes_key, iv)
    encrypted_aes_key = rsa_encrypt(aes_key, public_key)
    return ciphertext_aes, encrypted_aes_key, iv

if __name__ == "__main__":
    flag = "FUSec2025{Hay_thu_phan_tich_doan_chuong_trinh_nay_xem}"

    private_key, public_key = generate_rsa_keypair()

    with open("private_key.pem", "wb") as f:
        f.write(private_key.export_key())
    with open("public_key.pem", "wb") as f:
        f.write(public_key.export_key())

    ciphertext_aes, encrypted_aes_key, iv = hybrid_encrypt(flag, public_key)

    data = {
        "ciphertext_aes": base64.b64encode(ciphertext_aes).decode(),
        "encrypted_aes_key": base64.b64encode(encrypted_aes_key).decode(),
        "iv": base64.b64encode(iv).decode()
    }

    with open("encrypted_data.json", "w") as f:
        json.dump(data, f, indent=4)

    print("Encryption completed. Data saved to encrypted_data.json")
    print("Private and public keys saved to private_key.pem and public_key.pem")
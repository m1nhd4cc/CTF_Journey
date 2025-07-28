from Crypto.PublicKey import RSA

from Crypto.PublicKey import RSA

# Import the RSA key from a file
with open('privacy_enhanced_mail_1f696c053d76a78c2c531bb013a92d4a.pem', 'r') as f:
    private_key_data = f.read()

private_key = RSA.importKey(private_key_data)
print(private_key.d)

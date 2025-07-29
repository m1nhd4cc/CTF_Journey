def encode_pwd(password):
    key = 0x24
    encoded_chars = [chr(ord(c) ^ key) for c in password]
    return ''.join(encoded_chars)

def decode_pwd(encoded_password):
    key = 0x24
    decoded_chars = [chr(ord(c) ^ key) for c in encoded_password]
    return ''.join(decoded_chars)

# Ví dụ: giả sử bạn có chuỗi mã hóa
encoded_password = "I]{I\024V\027{WAGQV\027{TS@"
decoded_password = decode_pwd(encoded_password)
print(f"Decoded password: {decoded_password}")


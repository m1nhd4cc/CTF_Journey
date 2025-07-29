def vigenere_decrypt(ciphertext, key):
    # Chuyển key về dạng chữ thường
    key = key.lower()
    plaintext = ""
    key_index = 0  # Chỉ số của key

    for char in ciphertext:
        if char.isalpha():  # Chỉ xử lý chữ cái
            # Xác định offset (A=0 hoặc a=0)
            offset = ord('A') if char.isupper() else ord('a')
            # Vị trí của ký tự trong bảng chữ cái
            c = ord(char) - offset
            k = ord(key[key_index % len(key)]) - ord('a')
            # Giải mã ký tự
            p = (c - k + 26) % 26
            # Thêm ký tự đã giải mã vào plaintext
            plaintext += chr(p + offset)
            # Tăng key_index
            key_index += 1
        else:
            # Giữ nguyên ký tự không phải chữ cái
            plaintext += char

    return plaintext

# Ciphertext và key
ciphertext = "W0RY3 D1Q3N3X3 0X3B4T10T"
key = "kagi"

# Giải mã
plaintext = vigenere_decrypt(ciphertext, key)
print("Plaintext:", plaintext)
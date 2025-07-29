def xory(msg, key):
    ct = []
    for i in range(len(msg)):
        ct.append(msg[i] ^ key[i % len(key)])
    return bytes(ct)

# Cipher đã được chuyển từ hex sang bytes
cipher = bytes.fromhex('ba35f89312c933e1d97fa6168ddc21a650d8b733c914e18324c916e1af0eac1c')

# Key mới tìm được
key = b'\xf9\x61\xbe\xe8\x4a'

# Giải mã FLAG
flag = xory(cipher, key)

print("Flag giải mã:", flag)

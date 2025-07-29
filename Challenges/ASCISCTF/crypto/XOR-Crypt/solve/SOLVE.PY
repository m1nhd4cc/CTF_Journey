def xory(msg, key):
    ct = []
    for i in range(len(msg)):
        ct.append(msg[i] ^ key[i % len(key)])
    return bytes(ct)

# Cipher đã được chuyển từ hex sang bytes
cipher = bytes.fromhex('4c61a1087e766ad213723c07bd361e3959bd704b524bd23472665cd236725b79b73c27')

# KEY tìm được
key = b'\x0d\x32\xe2\x41\x2d'

# Giải mã FLAG
flag = xory(cipher, key)
# a= xory(b,c) == b=xory(a,c)

print(flag)

#b'ASCIS{X0R_15_w34k_1f_y0u_kn0w_VKU}\n'

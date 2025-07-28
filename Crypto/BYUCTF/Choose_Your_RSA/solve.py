import pwn
from Crypto.Util.number import long_to_bytes
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad
import gmpy2

# Chọn các số mũ e = [2, 3, 6]
e = [2, 3, 6]

# Kết nối đến server
r = pwn.remote('choose.chal.cyberjousting.com', 1348)

# Đọc dòng chứa thông báo generating values và dòng chứa flag
r.recvuntil(b"[+] Generating values...\n")  # Bỏ qua dòng thông báo
encrypted_flag_hex = r.recvline().decode().strip()  # Đọc dòng chứa flag hex
print(f"Encrypted Flag: {encrypted_flag_hex}")

# Bỏ qua các dòng tiếp theo cho đến prompt nhập e
r.recvuntil(b"Please put your distinct e values in increasing order.\n")

# Gửi các số mũ đã chọn
r.sendline(' '.join(map(str, e)).encode())

# Đọc các giá trị n và c từ server
n = []
c = []
for i in range(3):
    n_line = r.recvline().decode().strip()
    n_i = int(n_line.split('=')[1])
    n.append(n_i)
    c_line = r.recvline().decode().strip()
    c_i = int(c_line.split('=')[1])
    c.append(c_i)

n0, n1, n2 = n
c0, c1, c2 = c

# Tính toán X0 = c0^3 mod n0 (key^6 mod n0)
X0 = pow(c0, 3, n0)

# Tính toán X1 = c1^2 mod n1 (key^6 mod n1)
X1 = pow(c1, 2, n1)

# X2 = c2 (key^6 mod n2)
X2 = c2

# Hàm CRT cho 3 modulus
def crt(moduli, remainders):
    from functools import reduce
    prod = reduce(lambda a, b: a * b, moduli)
    result = 0
    for mod, rem in zip(moduli, remainders):
        p = prod // mod
        result += rem * pow(p, -1, mod) * p
    return result % prod

# Tính X = key^6 sử dụng CRT
X = crt([n0, n1, n2], [X0, X1, X2])

# Khai căn bậc 6 để lấy key
key, is_exact = gmpy2.iroot(X, 6)
if not is_exact:
    print("Không tìm thấy căn chính xác!")
    exit()

key_bytes = long_to_bytes(int(key))
aes_key = key_bytes[:16]  # Lấy 16 byte đầu làm khóa AES

# Giải mã flag
encrypted_flag = bytes.fromhex(encrypted_flag_hex)
cipher = AES.new(aes_key, AES.MODE_ECB)
flag_padded = cipher.decrypt(encrypted_flag)
flag = unpad(flag_padded, AES.block_size)

print("Flag:", flag.decode())



# [+] Opening connection to choose.chal.cyberjousting.com on port 1348: Done
# Encrypted Flag: ed41d664c1a7f726f83da866c26cbb809416225eb02e615aef2c621ca332a704aa63dd7c88f677b3aabc2ff6d5ee69c28f6f74f82c5ad88cbc488fd4dbbff210
# Flag: byuctf{Chin3s3_rema1nd3r_th30r3m_is_Sup3r_H3lpful}
# [*] Closed connection to choose.chal.cyberjousting.com port 1348
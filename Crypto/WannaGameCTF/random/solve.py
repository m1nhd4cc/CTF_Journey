import random

# Kết quả mã hóa từ bài toán
encrypted_hex = "0203e2c0dd20182bea1d00f41b25ad314740c3b239a32755bab1b3ca1a98f0127f1a1aeefa15a418e9b03ad25b3a92a46c0f5a6f41cb580f7d8a3325c76e66b937baea"
encrypted_bytes = bytes.fromhex(encrypted_hex)

# Thử tất cả các seed
for seed in range(10001):
    random.seed(seed)
    decrypted = list(encrypted_bytes)

    # Thực hiện quá trình đảo ngược XOR 1337 lần
    for _ in range(1337):
        random_values = [random.randint(0, 255) for _ in range(len(decrypted))]
        decrypted = [x ^ y for x, y in zip(decrypted, random_values)]

    # Chuyển đổi lại thành chuỗi ký tự
    decrypted_flag = bytes(decrypted)
    
    # Kiểm tra xem flag có hợp lệ không
    # Giả sử flag bắt đầu bằng "W1{"
    if decrypted_flag.startswith(b"W1{"):
        print(f"Found flag with seed {seed}: {decrypted_flag.decode()}")
        break

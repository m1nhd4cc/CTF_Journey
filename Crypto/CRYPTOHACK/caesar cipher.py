import pandas as pd

P = input("Nhập bản rõ: ").upper()  # Chuyển đổi thành chữ hoa để đảm bảo tính đúng đắn
k = int(input("Nhập khóa k: "))

# Loại bỏ khoảng trắng và các ký tự không phải chữ cái, chỉ lưu lại các chữ cái
cleaned_chars = [char for char in P if char.isalpha()]

# Dùng một list để lưu các giá trị x tương ứng với mỗi ký tự
values_x = []

for char in cleaned_chars:
    value_x = ord(char) - ord('A')  # Tính giá trị x: A = 0, B = 1, ..., Z = 25
    values_x.append(value_x)

# Tính giá trị y theo công thức y = (x + k) % 26
values_x2 = [(x + k) % 26 for x in values_x]

# Chuyển đổi giá trị x+k mod 26 thành ciphertext
C = ''.join(chr(x + ord('A')) for x in values_x2)

values_y = values_x2

values_y2= [(y - k) % 26 for y in values_y]

Plaintext = ''.join(chr(y + ord('A')) for y in values_y2)
# Tạo DataFrame từ dữ liệu
df = pd.DataFrame({'Bản rõ': cleaned_chars, 'x': values_x, 'x+k mod 26': values_x2, 'Bản mã': list(C), 'y':values_y, 'y-k mod 26': values_y2, 'Plaintext': list(Plaintext)})

# Hiển thị bảng theo hàng ngang
print(df.T)

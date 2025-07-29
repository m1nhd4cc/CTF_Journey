Sử dụng tools để phân tích mã Morse: https://morsecode.world/international/decoder/audio-decoder-adaptive.html
Bạn sẽ nhận được ciphertext từ file audio là:

W0RY3 D1Q3N3X3 0X3B4T10T

Lưu ý:

Key được cung cấp là "kagi".
Chúng ta sẽ sử dụng Vigenère Cipher để giải mã ciphertext này. Tuy nhiên, Vigenère Cipher thường chỉ áp dụng cho các chữ cái (A-Z hoặc a-z). Vì vậy, chúng ta cần xử lý các ký tự đặc biệt (số và khoảng trắng) một cách phù hợp.

Nguyên tắc giải mã Vigenère Cipher:
Với mỗi ký tự trong ciphertext:
Nếu ,đó là chữ cái áp dụng giải mã bằng cách sử dụng key.
Nếu không phải chữ cái (ví dụ: số hoặc khoảng trắng), giữ nguyên.

Công thức giải mã:
Mỗi ký tự ciphertext C được giải mã thành ký tự plaintext P như sau: 
P=(C−K+26)mod26 

Trong đó:
C là vị trí của ký tự ciphertext trong bảng chữ cái (A=0, B=1, ..., Z=25).
K là vị trí của ký tự key trong bảng chữ cái.
P là vị trí của ký tự plaintext trong bảng chữ cái.
Xử lý key:
Key "kagi" sẽ được lặp lại để khớp với độ dài của ciphertext (bỏ qua các ký tự đặc biệt).

#flag: m0rs3_v1g3n3r3_0p3r4t10n
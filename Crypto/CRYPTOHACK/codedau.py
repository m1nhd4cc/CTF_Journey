from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.backends import default_backend

def diffie_hellman(p, g, a, b):
    # Tính giá trị công khai
    A = pow(g, a, p)  # Giá trị công khai của Alice
    B = pow(g, b, p)  # Giá trị công khai của Bob
    
    print(f"Giá trị công khai của Alice (A): {A}")
    print(f"Giá trị công khai của Bob (B): {B}")
    
    # Trao đổi giá trị công khai và tính khóa chung
    K_A = pow(B, a, p)  # Khóa chung tính bởi Alice
    K_B = pow(A, b, p)  # Khóa chung tính bởi Bob
    
    print(f"Khóa chung tính bởi Alice (K_A): {K_A}")
    print(f"Khóa chung tính bởi Bob (K_B): {K_B}")
    
    # Khóa chung phải giống nhau
    assert K_A == K_B, "Khóa chung không khớp!"
    
    # Sử dụng SHA-256 để băm khóa chung
    digest = hashes.Hash(hashes.SHA256(), backend=default_backend())
    digest.update(K_A.to_bytes((K_A.bit_length() + 7) // 8, byteorder='big'))
    return digest.finalize()  # Trả về giá trị băm 32 byte

def main():
    # Các số nguyên tố lớn p và g
    p = 23
    g = 5

    # Nhập các số bí mật (phải là số nguyên dương nhỏ hơn p)
    a = int(input(f"Nhập số bí mật của Alice : "))
    b = int(input(f"Nhập số bí mật của Bob : "))

    # Thực hiện thỏa thuận khóa
    key = diffie_hellman(p, g, a, b)
    print(f"Khóa chung cuối cùng (dạng byte): {key}")

if __name__ == "__main__":
    main()

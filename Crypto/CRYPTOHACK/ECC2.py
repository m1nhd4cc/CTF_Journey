class Point:
    def __init__(self, x, y, curve):
        self.x = x
        self.y = y
        self.curve = curve
    
    def __add__(self, other):
        if self == other:
            return self.curve.double_point(self)
        return self.curve.add_points(self, other)
    
    def __mul__(self, n):
        return self.curve.multiply_point(self, n)
    
    def __str__(self):
        return f"({self.x}, {self.y})"

class EllipticCurve:
    def __init__(self, a, b, p):
        self.a = a
        self.b = b
        self.p = p
    
    def add_points(self, P, Q):
        if P.x == Q.x and P.y == Q.y:
            return self.double_point(P)
        
        lam = (Q.y - P.y) * pow(Q.x - P.x, -1, self.p) % self.p
        x_r = (lam**2 - P.x - Q.x) % self.p
        y_r = (lam * (P.x - x_r) - P.y) % self.p
        print(f"Phép cộng điểm: λ = ({Q.y} - {P.y}) * ({Q.x} - {P.x})^(-1) mod {self.p} = {lam}")
        print(f"x_r = λ^2 - x_P - x_Q mod {self.p} = {x_r}")
        print(f"y_r = λ * (x_P - x_r) - y_P mod {self.p} = {y_r}")
        return Point(x_r, y_r, self)
    
    def double_point(self, P):
        lam = (3 * P.x**2 + self.a) * pow(2 * P.y, -1, self.p) % self.p
        x_r = (lam**2 - 2 * P.x) % self.p
        y_r = (lam * (P.x - x_r) - P.y) % self.p
        print(f"Phép nhân đôi điểm: λ = (3 * {P.x}^2 + {self.a}) * (2 * {P.y})^(-1) mod {self.p} = {lam}")
        print(f"x_r = λ^2 - 2 * {P.x} mod {self.p} = {x_r}")
        print(f"y_r = λ * ({P.x} - {x_r}) - {P.y} mod {self.p} = {y_r}")
        return Point(x_r, y_r, self)
    
    def multiply_point(self, P, n):
        result = None
        addend = P
        
        print(f"Phép nhân điểm: {n} * {P}")
        while n:
            if n & 1:
                result = addend if result is None else result + addend
                print(f"Kết quả tạm thời: {result}")
            addend += addend
            n >>= 1
        
        return result

def main():
    # Nhập thông tin cho elliptic curve
    a = int(input("Nhập hệ số a: "))
    b = int(input("Nhập hệ số b: "))
    p = int(input("Nhập modulus p: "))
    curve = EllipticCurve(a, b, p)
    
    # Nhập điểm sinh G
    Gx = int(input("Nhập tọa độ x của điểm sinh G: "))
    Gy = int(input("Nhập tọa độ y của điểm sinh G: "))
    G = Point(Gx, Gy, curve)
    
    # Nhập khóa riêng của A và B
    n_B = int(input("Nhập khóa riêng của B: "))
    
    # Tính khóa công khai
    P_B = G * n_B
    print(f"Khóa công khai của B (P_B): {P_B}")
    
    # Nhập bản tin cần gửi
    PMx = int(input("Nhập tọa độ x của bản tin P_M: "))
    PMy = int(input("Nhập tọa độ y của bản tin P_M: "))
    P_M = Point(PMx, PMy, curve)
    
    # Nhập giá trị ngẫu nhiên k
    k = int(input("Nhập giá trị ngẫu nhiên k: "))
    
    # Mã hóa bản tin
    C1 = G * k
    C2 = P_M + (P_B * k)
    print(f"Mã hóa: C1 = {C1}, C2 = {C2}")
    
    # Giải mã bản tin
    decoded_P_M = C2 + Point(C1.x, -C1.y, curve) * n_B
    print(f"Giải mã: P_M = {decoded_P_M}")

if __name__ == "__main__":
    main()

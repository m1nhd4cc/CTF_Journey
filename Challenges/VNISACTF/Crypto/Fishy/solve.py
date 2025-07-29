from sage.all import *
from hashlib import sha256
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad

n = 100
m = 100
q = 7


f = open("output.txt", "r")
for _ in range(7):
    exec(f.readline().strip())
gen_seed = bytes(seed)
FF = GF(q)
F = []

# Regen F
for i in range(m):
    cur = []
    for j in range(n):
        cur.append([])
        for k in range(n):
            cur[-1].append(sha256(gen_seed).digest()[0] % q)
            gen_seed = sha256(gen_seed).digest()
    F.append(matrix(FF, n, n, cur))




# Duyệt qua tất cả các danh sách và tính toán giá trị a. Nếu a = 0, thì chúng ta có bộ ba (com, t, verif).
# Chúng ta có thể khôi phục s từ t bằng cách giải một hệ phương trình tuyến tính trong GF(7).
# Trong trường hợp có nhiều nghiệm, chúng ta liệt kê chúng và cố gắng giải mã cờ với từng nghiệm.


for i in range(len(coms)):
    com, tas, verif = coms[i], tass[i], verifs[i]
    a = sha256(bytes([int(i) for i in com + v + verif])).digest()[0] % q
    if a != 0:
        continue

    t = matrix(FF, tas)
    lhs =  []
    for j in range(n):
        lhs.append((t * (F[j] + F[j].T)).list())
    lhs = matrix(FF, lhs)
    rhs = matrix(FF, verif)

    s = lhs.solve_right(rhs.T).T
    if lhs.right_nullity() == 0:
        print(f'Recovered secret key: {s = }')
        key = sha256(str([int(i) for i in s.list()]).encode()).digest()
        cipher = AES.new(key, AES.MODE_CBC, iv)
        flag = cipher.decrypt(ct)
        flag = unpad(flag, 16).decode()
        print(f'{flag = }')
    else:
        row = lhs.right_kernel_matrix()
        for i in range(q):
            tmp = s + i * row
            key = sha256(str([int(i) for i in tmp.list()]).encode()).digest()
            cipher = AES.new(key, AES.MODE_CBC, iv)
            flag = cipher.decrypt(ct)
            if b'ASCIS' in flag:
                print(f'Recovered secret key: {s = }')
                flag = unpad(flag, 16).decode()
                print(f'{flag = }')
                break
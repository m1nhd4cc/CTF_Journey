real_parts = [...]
i_coeffs = [...]
j_coeffs = [...]
k_coeffs = [...]

F.<i,j,k> = QuaternionAlgebra(-1, -1)
B = [1, i, j, k]
t1, t2, t3, t4, mat = [], [], [], [], []
for i in range (9) :
    b1, b2, b3, b4 = real_parts[i], i_coeffs[i], j_coeffs[i], k_coeffs[i]
    t1.extend([b1, -b2, -b3, -b4])
    t2.extend([b2, b1, b4, -b3])
    t3.extend([b3, -b4, b1, b2])
    t4.extend([b4, b3, -b2, b1])

mat.extend([t1,t2,t3,t4])
A = [-17021892191322790357078, 19986226329660045481112, 15643261273292061217693, 21139791497063095405696]
load('https://raw.githubusercontent.com/TheBlupper/linineq/main/linineq.py')
for i in solve_bounded_gen(Matrix(mat), A, [30]*36, [130]*36) :
    s = ''.join(chr(j) for j in i)  
    if 'irisctf{' in s: 
        print(s)
        break

#irisctf{wow_i_cant_believe_its_lll!}
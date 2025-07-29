from Crypto.Util.number import long_to_bytes

# Các giá trị m1, m2, m3 từ output trước
m1 = 27046270205583738426625185075519510256285586266082049340895748725090922871901733752596624170542655351844326784290936506265553138960321101164405131707635668507337081720614161651196708
m2 = 83716119419780532650621654937209317428545934412326930445313250
m3 = 94935765042063898468589645892042631226395106982780352338713683009814390664706073361352974705452428061610640019886587570757

# Viết code giải hệ phương trình bậc 3
def solve_cubic(m1, m2, m3):
    # Sử dụng SageMath hoặc thư viện sympy để giải
    from sympy import Symbol, solve
    x = Symbol('x')
    y = Symbol('y')
    z = Symbol('z')
    
    eq1 = x*y*z - m1
    eq2 = x + y + z - m2
    eq3 = x*y + y*z + z*x - m3
    
    solution = solve((eq1, eq2, eq3), (x, y, z))
    return solution

# Giải hệ phương trình
solution = solve_cubic(m1, m2, m3)

# Chuyển các giá trị tìm được thành bytes
for sol in solution:
    try:
        flag1 = long_to_bytes(int(sol[0]))
        flag2 = long_to_bytes(int(sol[1]))
        flag3 = long_to_bytes(int(sol[2]))
        print(flag1 + flag2 + flag3)
    except:
        continue
        
#W1{wi3rd_ch41!En9e_n33d_4_WlErD_s0O!luti0n_06dc6c13b6e6208ad688ce003a161cbb}

from sage.all import *
from sage.modules.free_module_integer import IntegerLattice

F = QuaternionAlgebra(-1 , -1 , names=('i', 'j', 'k',))
(i, j, k,) = F._first_ngens(3)
A = []
B = [1, i, j, k]

def to_matrix(q):
    return matrix([[q[0],q[1],q[2],q[3]],[-q[1],q[0],-q[3],q[2]],[-q[2],q[3],q[0],-q[1]],[-q[3],-q[2],q[1],q[0]]])

def from_matrix(m):
    return F(m[0]) 

A = [17182433425281628234 + 14279655808574179137*i + 8531159707880760053*j + 10324521189909330699*k, 10979190813462137563 + 11958433776450130274*i + 10360430094019091456*j + 11669398524919455091*k, 3230073756301653559 + 4778309388978960703*i + 7991444794442975980*j + 11596790291939515343*k, 11946083696500480600 + 18097491527846518653*i + 5640046632870036155*j + 2308502738741771335*k, 12639949829592355838 + 12578487825594881151*i + 5989294895593982847*j + 9055819202108394307*k, 15962426286361116943 + 6558955524158439283*i + 2284893063407554440*j + 14331331998172190719*k, 14588723113888416852 + 432503514368407804*i + 11024468666631962695*j + 10056344423714511721*k, 2058233428417594677 + 7708470259314925062*i + 7418836888786246673*j + 14461629396829662899*k, 4259431518253064343 + 9872607911298470259*i + 16758451559955816076*j + 16552476455431860146*k]
s = F(-17021892191322790357078 + 19986226329660045481112*i + 15643261273292061217693*j + 21139791497063095405696*k)

A = list(map(F, A))
s_sym = matrix(4,4)

assert A[0]*A[1] == from_matrix(to_matrix(A[0])*to_matrix(A[1]))
assert A[0]+A[1] == from_matrix(to_matrix(A[0])+to_matrix(A[1]))

R = PolynomialRing(ZZ, names=",".join([f"m{i}" for i in range(4*len(A))]))
msg_gens = R.gens()

# known part
msg_bin = b"irisctf{"
msg = [F(sum(Integer(msg_bin[idx+bi])*b for bi, b in enumerate(B))) for idx in range(0, len(msg_bin), len(B))]
known = matrix(4,4)

for i, m in enumerate(msg):
    known += to_matrix(m) * to_matrix(A[i])

s = s - from_matrix(known)
A = A[len(msg):]

for i in range(len(A)):
    s_sym += to_matrix(msg_gens[i*4:i*4+4]) * to_matrix(A[i])

M = []

for i, s_target in enumerate(s_sym[0]):
    #print(s_target.coefficients(), "=", s[i])
    M.append([s[i]] + list(map(lambda x: -x, s_target.coefficients()))) # negation

M = matrix(M).transpose().augment(identity_matrix(4*len(A)+1))
W = diagonal_matrix([2**256] * 5 + [1]*(4*len(A)))

lattice = IntegerLattice(M * W).LLL() / W

v = next(v for v in lattice if all(map(lambda x: x == 0, v[:4])) and abs(v[4])==1)
v *= sign(v[4])
v = v[5:]

flag = msg_bin.decode() + "".join(map(chr, v))

print(flag)
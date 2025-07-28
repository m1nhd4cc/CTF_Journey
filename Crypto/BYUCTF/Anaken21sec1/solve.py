import numpy as np

# --- copy in the same five 6×6 permutation arrays A–E from encrypt(1).py ---
A = np.array([[1,  7, 13, 19, 25, 31],
              [2,  8, 14, 20, 26, 32],
              [3,  9, 15, 21, 27, 33],
              [4, 10, 16, 22, 28, 34],
              [5, 11, 17, 23, 29, 35],
              [6, 12, 18, 24, 30, 36]])
B = np.array([[36, 30, 24, 18, 12,  6],
              [35, 29, 23, 17, 11,  5],
              [34, 28, 22, 16, 10,  4],
              [33, 27, 21, 15,  9,  3],
              [32, 26, 20, 14,  8,  2],
              [31, 25, 19, 13,  7,  1]])
C = np.array([[31, 25, 19, 13,  7,  1],
              [32, 26, 20, 14,  8,  2],
              [33, 27, 21, 15,  9,  3],
              [34, 28, 22, 16, 10,  4],
              [35, 29, 23, 17, 11,  5],
              [36, 30, 24, 18, 12,  6]])
D = np.array([[ 7,  1,  9,  3, 11,  5],
              [ 8,  2, 10,  4, 12,  6],
              [19, 13, 21, 15, 23, 17],
              [20, 14, 22, 16, 24, 18],
              [31, 25, 33, 27, 35, 29],
              [32, 26, 34, 28, 36, 30]])
E = np.array([[ 2,  3,  9,  5,  6, 12],
              [ 1, 11, 15,  4, 29, 18],
              [ 7, 13, 14, 10, 16, 17],
              [20, 21, 27, 23, 24, 30],
              [19,  8, 33, 22, 26, 36],
              [25, 31, 32, 28, 34, 35]])
permutes = [A, B, C, D, E]

def inverse_permute(mat, count):
    P = permutes[count]
    inv = np.zeros_like(mat)
    for i in range(6):
        for j in range(6):
            idx = int(P[i,j] - 1)
            r,c = divmod(idx,6)
            inv[r,c] = mat[i,j]
    return inv

def inverse_add(mat, count):
    M = mat.copy()
    if count == 0:
        for i in range(6):
            for j in range(6):
                if (i+j)%2 == 0:
                    M[i,j] = (M[i,j] - 1) % 3

    elif count == 1:
        M[3:,3:] = (M[3:,3:] - M[:3,:3]) % 3

    elif count == 2:
        M[:3,:3] = (M[:3,:3] - M[3:,3:]) % 3

    elif count == 3:
        M[3:,:3] = (M[3:,:3] - M[:3,3:]) % 3

    else:  # count == 4
        M[:3,3:] = (M[:3,3:] - M[3:,:3]) % 3

    return M

def undo_columnar(ctext, key):
    keyNums = [ord(c)-97 for c in key]
    # unique in order
    reduced = []
    for x in keyNums:
        if x not in reduced:
            reduced.append(x)
    n = len(reduced)
    L = len(ctext)
    # compute each column's length
    col_lens = [(L - j + n - 1)//n for j in range(n)]
    # reading order = indices of columns in ascending reduced[]
    order = sorted(range(n), key=lambda i: reduced[i])
    # slice out each box in the order it was emitted
    boxes = [None]*n
    idx = 0
    for col in order:
        ln = col_lens[col]
        boxes[col] = list(ctext[idx:idx+ln])
        idx += ln

    # put them back into the flat result by i % n
    flat = []
    for i in range(L):
        c = i % n
        flat.append( boxes[c].pop(0) )
    return ''.join(flat)

def decrypt(ctext, key):
    flat = undo_columnar(ctext, key)
    # break into 12‐char blocks
    blocks = [flat[12*i:12*(i+1)] for i in range(len(flat)//12)]
    keyNums = [ord(c)-97 for c in key]
    plain = []


    for blk in blocks:
        # rebuild M from the 12 cipher‐letters
        M = np.zeros((6,6), dtype=int)
        # first 6 letters => row i, columns 0–2
        for i,ch in enumerate(blk[:6]):
            v = 0 if ch=='0' else (ord(ch)-96)
            M[i,0] = v//9
            M[i,1] = (v%9)//3
            M[i,2] = v%3
        # next 6 => row i, columns 3–5
        for i,ch in enumerate(blk[6:]):
            v = 0 if ch=='0' else (ord(ch)-96)
            M[i,3] = v//9
            M[i,4] = (v%9)//3
            M[i,5] = v%3

        # undo all (permute→add) in reverse
        for kn in reversed(keyNums):
            a = kn % 5
            p = (kn//5) % 5
            M = inverse_add(M, a)
            M = inverse_permute(M, p)

        # *** HERE IS THE FIX ***
        # original blockM was built with plaintext letters
        # in columns, not rows:
        #   letter 0–5 came from col i of rows 0–2
        #   letter 6–11 came from col i of rows 3–5
        for i in range(6):
            num = 9*M[0,i] + 3*M[1,i] + M[2,i]
            plain.append('?' if num==0 else chr(num+96))
        for i in range(6):
            num = 9*M[3,i] + 3*M[4,i] + M[5,i]
            plain.append('?' if num==0 else chr(num+96))
    return ''.join(plain).rstrip('x')
if __name__ == '__main__':
    key        = 'orygwktcjpb'
    ciphertext = 'cnpiaytjyzggnnnktjzcvuzjexxkvnrlfzectovhfswyphjt'
    pt = decrypt(ciphertext, key)
    print("Decrypted plaintext:", pt)
    print("Flag: byuctf{" + pt + "}")

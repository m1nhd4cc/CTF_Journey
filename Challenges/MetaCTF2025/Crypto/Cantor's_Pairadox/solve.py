from math import isqrt

# === INPUT ===
# Encoded final value from output.txt
final_value = 4036872197130975885183239290191447112180924008343518098638033545535893348884348262766810360707383741794721392226291497314826201270847784737584016

# === REVERSE FUNCTIONS ===

# Invert the triangular number: S such that T = S*(S+1)//2
def invert_triangular(T):
    return (isqrt(8 * T + 1) - 1) // 2

# Reverse the custom Cantor-like pair function
def unpair(z):
    S = invert_triangular(z)
    T = S * (S + 1) // 2
    n2 = z - T
    n1 = S - n2
    return (n1, n2)

# Expand array by reversing pairings
def unpair_array(arr):
    result = []
    for val in arr:
        result.extend(unpair(val))
    return result

# === MAIN DECODING ===

# Start with the final value as a 1-element list
temp = [final_value]

# Reverse 6 rounds of pairing
for _ in range(6):
    temp = unpair_array(temp)

# Convert ASCII codes back to characters (ignore padding zeros)
flag = ''.join(chr(n) for n in temp if n != 0)

print("Recovered flag:", flag)

#Recovered flag: Dawg{1_pr3f3r_4ppl3s_t0_pa1rs_4nyw2y5}

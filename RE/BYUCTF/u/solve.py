# Let's replicate the Python code to get the hidden string (flag)

# hardcoded list ù
u_list = [12838,1089,16029,13761,1276,14790,2091,17199,2223,2925,17901,3159,18135,18837,3135,19071,4095,19773,4797,4085,20007,5733,20709,17005,2601,9620,3192,9724,3127,8125]
# parameters
u = 3
U = 256
# generate 3^i mod 256 for i in 0..255
pow_list = [pow(u, i, U) for i in range(U)]
# set of these values
uniq = set(pow_list)
# list of set
data = list(uniq)
# slice indices
start = u
length = len(u_list)
slice_vals = data[start:start+length]
# now compute characters
chars = []
for a, b in zip(slice_vals, u_list):
    if b % a != 0:
        chars.append('?')
    else:
        val = b // a
        # only if valid ASCII
        if 0 <= val < 256:
            chars.append(chr(val))
        else:
            chars.append('?')
flag = ''.join(chars)
flag

#byuctf{uuuuuuu_uuuu_uuu_34845}
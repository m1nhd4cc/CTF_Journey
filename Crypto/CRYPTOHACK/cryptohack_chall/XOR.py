import binascii
from pwn import*

str="0e0b213f26041e480b26217f27342e175d0e070a3c5b103e2526217f27342e175d0e077e263451150104"
encode = binascii.unhexlify(str)
print(encode)
format_flag ="crypto{"
key = "myXORkey"
print(xor(encode, key))

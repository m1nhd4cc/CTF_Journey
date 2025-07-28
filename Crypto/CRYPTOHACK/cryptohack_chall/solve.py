#!usr/bin/python

from pwn import xor

enc_flag = bytes.fromhex("5541103a246e415e036c4c5f0e3d415a513e4a560050644859536b4f57003d4c")
enc_text = bytes.fromhex("6227295e455c7838375c7866375c7862355c786430635c7838665c7863365c78")
dec_text = b'A'*32

key = xor(enc_text, dec_text)

print(xor(enc_flag, key).decode())


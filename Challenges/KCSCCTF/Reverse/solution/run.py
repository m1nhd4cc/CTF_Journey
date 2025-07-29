#!/usr/bin/python3

from pwn import *
flag = open('flag.enc', 'rb').read()

def phase1():
    global enc
    enc = enc[::-1]

def phase2():
    global enc
    tmp = list(enc)
    for i in range(0, len(tmp), 2):
        a = (tmp[i] & 0xf0) | (tmp[i+1] & 0xf)
        b = (tmp[i+1] & 0xf0) | (tmp[i] & 0xf)
        tmp[i] = a
        tmp[i+1] = b
    enc = b''.join([p8(c) for c in tmp])

def phase3():
    global enc
    tmp = list(enc)
    for i in range(len(enc)-1-2, -1, -1):
        tmp[i+2] = (tmp[i] + tmp[i+2]) & 0xff
        tmp[i] = (tmp[i] + tmp[i+2]) & 0xff
    enc = b''.join([p8(c) for c in tmp])

def phase4(key):
    global enc
    tmp = list(enc)
    for i in range(len(tmp)):
        tmp[i] = tmp[i] ^ key
    enc = b''.join([p8(c) for c in tmp])

if __name__=='__main__':
    for a in range(0x100):
        enc = flag
        phase4(a)
        phase3()
        phase2()
        phase1()
        if b'KCSC' in enc:
            print(enc)





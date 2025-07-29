from Crypto.Cipher import AES
from os import urandom
from base64 import b64encode
import string
import socket
import threading


chars = string.ascii_lowercase + string.ascii_uppercase + '!_{}'
FLAG = b'KCSC{yay}'
assert all(i in chars for i in FLAG.decode())


def pad(msg, block_size):
    if len(msg) % block_size == 0:
        return msg
    return msg + bytes(block_size - len(msg) % block_size)


def chall(usrname):
    key = urandom(16)
    cipher = AES.new(key, AES.MODE_ECB)
    msg = usrname + FLAG
    enc = cipher.encrypt(pad(msg,16))
    return b64encode(enc)

class ThreadedServer(object):
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.sock.bind((self.host, self.port))

    def listen(self):
        self.sock.listen(5)
        while True:
            client, address = self.sock.accept()
            client.settimeout(60)
            threading.Thread(target = self.listenToClient,args = (client,address)).start()

    def listenToClient(self, client, address):
        size = 1024
        while True:
            try:
                usrname = client.recv(size).strip()
                client.send(chall(usrname) + b'\n')
            except:
                client.close()
                return False


if __name__ == "__main__":
    ThreadedServer('',2003).listen()
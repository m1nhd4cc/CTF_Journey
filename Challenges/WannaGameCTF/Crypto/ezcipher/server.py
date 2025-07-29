from secrets import token_bytes
import ctypes

BLOCK_SIZE = 0x08
TOKEN_SIZE = 0x20
FLAG       = open("/flag", "r").read().strip()

class Challenge:
    # Define the structures and function prototypes
    class CipherCtx(ctypes.Structure):
        _fields_ = [("rkeys", ctypes.c_uint16 * 0x10)]

    # Load the shared library
    lib = ctypes.CDLL('./libCrypto.so')

    # Function prototypes
    lib.Cipher_init_ctx.argtypes    = [ctypes.POINTER(CipherCtx), ctypes.POINTER(ctypes.c_uint8)]
    lib.Cipher_init_ctx.restype     = None

    lib.Cipher_ECB_encrypt.argtypes = [ctypes.POINTER(CipherCtx), ctypes.POINTER(ctypes.c_uint8)]
    lib.Cipher_ECB_encrypt.restype  = None

    lib.Cipher_get_token.argtypes   = [ctypes.POINTER(CipherCtx), ctypes.POINTER(ctypes.c_uint8)]
    lib.Cipher_get_token.restype    = None

    def __init__(self, master_key: bytes) -> None:
        assert len(master_key) == TOKEN_SIZE, "The length of master key must be 32-bytes"
        self.ctx    = self.CipherCtx()
        self.cnt    = 0
        self.tries  = 0
        self.secret = token_bytes(TOKEN_SIZE)
        self.lib.Cipher_init_ctx(ctypes.byref(self.ctx), (ctypes.c_uint8 * TOKEN_SIZE)(*list(master_key)))

    def __encrypt_block(self, block: bytes) -> bytes:
        assert len(block) == BLOCK_SIZE
        buffer = (ctypes.c_uint8 * BLOCK_SIZE)(*list(block))
        self.lib.Cipher_ECB_encrypt(ctypes.byref(self.ctx), buffer)
        return bytes(list(buffer))

    def __encrypt(self, plaintext: bytes) -> bytes:
        assert len(plaintext) % BLOCK_SIZE == 0, "The length of plaintext must be a multiple of 8-bytes"
        ciphertext = b""
        for i in range(0, len(plaintext), BLOCK_SIZE):
            ciphertext += self.__encrypt_block(block=plaintext[i:i+BLOCK_SIZE])
        return ciphertext

    def __get_token(self) -> bytes:
        buffer = (ctypes.c_uint8 * TOKEN_SIZE)(*list(self.secret))
        self.lib.Cipher_get_token(ctypes.byref(self.ctx), buffer)
        return bytes(list(buffer))

    def __menu(self):
        print("1. Encrypt message")
        print("2. Free token")
        print("3. Get flag")
        print("4. Exit")

    def loop(self):
        self.__menu()
        opt = int(input("> "))
        try:
            if opt == 1:
                if self.cnt < 1337:
                    self.cnt += 1
                    pt = bytes.fromhex(input("pt: "))
                    ct = self.__encrypt(pt).hex()
                    print(f"ct: {ct}")
                else:
                    print("Nope!")

            elif opt == 2:
                ping = token_bytes(TOKEN_SIZE)
                print("ping:", ping.hex())
                pong = bytes.fromhex(input("pong: "))
                if pong == self.__encrypt(ping):
                    print("token:", self.__get_token().hex())
                else:
                    print("Nope!")
                    exit(0)
            elif opt == 3:
                check = input("secret: ")
                if check == self.secret.hex():
                    print(f"congrats! Here is your flag: {FLAG}")
                else:
                    print("Nope!")
                exit(0)

            elif opt == 4:
                print("Bye!")
                exit(0)

            else:
                raise Exception("Invalid option!")
        except Exception as e:
            print(f"[!] Error: {e}")
            exit(1)

if __name__ == "__main__":
    chall = Challenge(master_key=token_bytes(TOKEN_SIZE))
    while True:
        chall.loop()
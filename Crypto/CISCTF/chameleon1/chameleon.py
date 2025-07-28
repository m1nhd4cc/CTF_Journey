from os import urandom
from hashlib import sha256
import string
import json
from flag import FLAG
num_layers = 11


class Server:
    def __init__(self) -> None:
        self.N = 2**num_layers
        self.tree = []
        self.users = []
        self.k = urandom(192)
        self.p = 0xffffffffffffffffc90fdaa22168c234c4c6628b80dc1cd129024e088a67cc74020bbea63b139b22514a08798e3404ddef9519b3cd3a431b302b0a6df25f14374fe1356d6d51c245e485b576625e7ec6f44c42e9a637ed6b0bff5cb6f406b7edee386bfb5a899fa5ae9f24117c4b1fe649286651ece45b3dc2007cb8a163bf0598da48361c55d39a69163fa8fd24cf5f83655d23dca3ad961c62f356208552bb9ed529077096966d670c354e4abc9804f1746c08ca237327ffffffffffffffff
        self.q = (self.p - 1) // 2
        self.g = 0x2
        self.x = int.from_bytes(self.k, "big")
        self.y = pow(self.g, self.x, self.p)
        self.buile_merkle_tree()
        self.root = self.get_root_hash()

    def keyed_random(self, identifier: bytes, index: int) -> int:
        return int.from_bytes(sha256(identifier + self.k + str(index).encode()).digest(), "big")

    def chameleon_hash(self, m: int, r: int) -> bytes:
        return (pow(self.g, m, self.p) * pow(self.y, r, self.p) % self.p).to_bytes(192, "big")

    def chameleon_extract(self, m1: int, r1: int, m2: int) -> int:
        r2 = (self.x * r1 + m1 - m2) * pow(self.x, -1, self.q) % self.q
        return r2

    def get_leaf(self, index: int) -> bytes:
        return self.chameleon_hash(self.keyed_random(b"m", index), self.keyed_random(b"r", index))

    def buile_merkle_tree(self) -> None:
        curr_layer = [self.get_leaf(i) for i in range(self.N)]
        self.tree.append(curr_layer)
        while len(curr_layer) != 1:
            curr_layer = [sha256(self.tree[-1][i]+self.tree[-1][i+1]).digest()
                          for i in range(0, len(self.tree[-1]), 2)]
            self.tree.append(curr_layer)

    def get_root_hash(self) -> str:
        return self.tree[-1][0].hex()

    def add_user(self, username: str) -> str:
        if not all(char in string.printable for char in username):
            return "Invalid username."
        if username in self.users:
            return "Username already exists."
        if "Chamomile" in username:
            return "No Chamomile no..."
        else:
            index = len(self.users) % self.N
            self.users.append(username)
            r = self.chameleon_extract(self.keyed_random(b"m", index), self.keyed_random(
                b"r", index), int.from_bytes(sha256(username.encode()).digest(), "big"))
            assert self.chameleon_hash(int.from_bytes(
                sha256(username.encode()).digest(), "big"), r) == self.get_leaf(index)
            proof = {"username": username, "r": hex(r), "index": index}
            path = []
            for layer in self.tree[:-1]:
                is_right_node = index % 2
                sibling_index = index - 1 if is_right_node else index + 1
                path.append(layer[sibling_index].hex())
                index //= 2
            proof["path"] = path
            return json.dumps(proof)

    def verify_user(self, proof: str) -> str:
        proof = json.loads(proof)
        username = proof["username"]
        index = proof["index"]
        assert 0 <= index < self.N
        tmp = self.chameleon_hash(int.from_bytes(
            sha256(username.encode()).digest(), "big"), int(proof["r"], 16))
        for level in range(num_layers):
            is_right_node = index % 2
            if is_right_node:
                tmp = sha256(bytes.fromhex(
                    proof["path"][level]) + tmp).digest()
            else:
                tmp = sha256(
                    tmp + bytes.fromhex(proof["path"][level])).digest()
            index //= 2
        if tmp.hex() == self.root:
            if username == "Chamomile":
                return FLAG
            return f"Welcome back, {username}."
        else:
            return "Invalid user."


def main():
    print("Wait for the server to initialize...")
    s = Server()
    print(f"Public committed root: {s.root}")
    print(f"Chameleon public key: {hex(s.y)}")
    while True:
        try:
            user_input = input()
            user_input = json.loads(user_input)
            option = user_input["option"]
            if option == 1:
                msg = s.add_user(user_input["username"])
            elif option == 2:
                proof = input()
                msg = s.verify_user(proof)
            else:
                print("Invalid option, goodbye.")
                return
            print(msg)
        except:
            return


if __name__ == "__main__":
    main()

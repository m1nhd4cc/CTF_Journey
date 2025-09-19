import struct
from typing import Iterable, Optional


BLOCK_SIZE = 64
OUT_SIZE = 32

PAD_START_BYTE = 0x81
LEN_XOR_MASK = 0xA5A5A5A5A5A5A5A5
PAD_TRAILER_TAG = b"NHv2"

WORD_PERM = (0, 2, 5, 6, 7, 1, 3, 4)


def _rotl32(x: int, n: int) -> int:
    n &= 31
    return ((x << n) | (x >> (32 - n))) & 0xFFFFFFFF


def _iv() -> list[int]:
    return [
        0x7F4A7C15,
        0xCB2D9E3B,
        0x3A1F56D7,
        0x91E2B408,
        0xD5C7A1FE,
        0x2863F9B2,
        0x4EC01D87,
        0xB8A7E643,
    ]


def _compress(h: list[int], block: bytes) -> None:
    m = list(struct.unpack("<16I", block))
    v = h[:]
    for r in range(4):
        for i in range(16):
            a = i & 7
            b = (i + 1) & 7
            c = (i + 2) & 7
            t = (v[b] ^ m[i]) + (0x9E3779B9 ^ (r * 0x1000193 + i))
            v[a] = _rotl32((v[a] + t) & 0xFFFFFFFF, ((i + 1 + r) % 31) + 1)
            v[c] ^= (v[a] + m[(i * 7) & 15]) & 0xFFFFFFFF
    for i in range(8):
        h[i] = (h[i] + v[i] + m[i ^ 8]) & 0xFFFFFFFF


def _md_pad_byte_len(byte_len: int) -> bytes:
    bit_len = (byte_len & ((1 << 64) - 1)) * 8
    trailer_size = 8 + 8 + len(PAD_TRAILER_TAG)
    pad = bytes([PAD_START_BYTE])
    rem = (byte_len + 1 + trailer_size) % BLOCK_SIZE
    pad_zeros = (BLOCK_SIZE - rem) % BLOCK_SIZE
    pad += b"\x00" * pad_zeros
    pad += struct.pack("<Q", bit_len)
    pad += struct.pack("<Q", bit_len ^ LEN_XOR_MASK)
    pad += PAD_TRAILER_TAG
    return pad


def _serialize_state(h: Iterable[int]) -> bytes:
    h_list = list(h)
    return struct.pack("<8I", *(h_list[i] for i in WORD_PERM))


def _parse_state(d: bytes) -> list[int]:
    if len(d) != OUT_SIZE:
        raise ValueError("digest/state must be 32 bytes")
    words = list(struct.unpack("<8I", d))
    inv = [0] * 8
    for i, p in enumerate(WORD_PERM):
        inv[p] = i
    h = [0] * 8
    for idx in range(8):
        h[idx] = words[inv[idx]]
    return h


class NaiveHash:
    def __init__(self, iv: Optional[bytes] = None, count: int = 0):
        if iv is None:
            self._h = _iv()
        else:
            if len(iv) != OUT_SIZE:
                raise ValueError("iv must be 32 bytes")
            self._h = _parse_state(iv)
        self._count = count
        self._buf = bytearray()

    def update(self, data: bytes) -> "NaiveHash":
        if not data:
            return self
        self._buf.extend(data)
        while len(self._buf) >= BLOCK_SIZE:
            blk = bytes(self._buf[:BLOCK_SIZE])
            del self._buf[:BLOCK_SIZE]
            _compress(self._h, blk)
            self._count += BLOCK_SIZE
        return self

    def _copy(self) -> "NaiveHash":
        c = NaiveHash(_serialize_state(self._h), self._count)
        c._buf = self._buf[:]
        return c

    def digest(self) -> bytes:
        c = self._copy()
        total = c._count + len(c._buf)
        pad = _md_pad_byte_len(total)
        c.update(pad)
        assert len(c._buf) == 0
        return _serialize_state(c._h)

    def hexdigest(self) -> str:
        return self.digest().hex()

    @staticmethod
    def hash(data: bytes) -> bytes:
        return NaiveHash().update(data).digest()


__all__ = [
    "NaiveHash",
    "BLOCK_SIZE",
    "OUT_SIZE",
    "WORD_PERM",
]

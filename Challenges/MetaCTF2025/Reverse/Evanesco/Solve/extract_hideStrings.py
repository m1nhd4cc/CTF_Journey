import struct

data = [
    0x8481a0f38180a0f3,
    0xb781a0f3a181a0f3,
    0x8381a0f3a781a0f3,
    0x8681a0f39481a0f3,
    0xb581a0f3bb81a0f3,
    0xa381a0f39f81a0f3,
    0xae81a0f3a181a0f3,
    0xb481a0f39f81a0f3,
    0xa781a0f3a181a0f3,
    0xa281a0f39f81a0f3,
    0xb481a0f3b581a0f3,
    0xb581a0f39f81a0f3,
    0xa381a0f39f81a0f3,
    0xae81a0f3a181a0f3,
    0x9f81a0f3b481a0f3,
    0xa981a0f3a881a0f3,
    0xa581a0f3a481a0f3,
    0xbf81a0f3bd81a0f3,
]

# Biến thành chuỗi byte
raw = b''.join(struct.pack('<Q', x) for x in data)
print("Raw bytes:", raw)

# Cố gắng in thử
try:
    print("Attempt UTF-8 decode:", raw.decode('utf-8'))
except UnicodeDecodeError:
    print("Contains non-printable bytes, try hex:")
    print(raw.hex())

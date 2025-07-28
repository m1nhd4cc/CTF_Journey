import json

import pwn

MESSAGE_COUNT = 2

io = pwn.remote("socket.cryptohack.org", 13386)
line = io.recvline()
pwn.info(f"Got banner: {line}")

messages = []
for _ in range(MESSAGE_COUNT):
    io.sendline(b'{"option": "get_flag"}')
    line = io.recvline().strip()
    pwn.info(f"Got message: {line}")
    parsed = json.loads(line)
    messages.append(parsed)

with open("messages.json", "w") as f:
    json.dump(messages, f)

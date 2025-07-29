import re

pattern = b"SUPERNOVAOVERLOAD"
bina = open("ThongBao.docm", "rb").read()

idx = re.search(pattern, bina)
idx = idx.start()
st = idx + len(pattern)
data = bina[st:st+4296811]
with open("Acheron.exe", "wb") as f:
    for i in range(len(data)):
        f.write(int.to_bytes(data[i] ^ b"1337"[i % 4]))

# Đọc keys
with open("keys.json", "r") as f:
    keys = json.load(f)

# Đọc flag_output.txt
with open("flag_output.txt", "r") as f:
    flag_output = f.read().strip()

# Đảo ngược emoji -> hex
hex_encoded = "".join([CharSet[emoji] for emoji in flag_output.split("‍")])

# Giải mã hex -> keyedText
keyed_text = bytes.fromhex(hex_encoded).decode()

# Giải mã keyedText -> flag
flag = "".join([chr(ord(keyed_text[i]) - keys[i]) for i in range(len(keyed_text))])

print("Flag:", flag)

# import json

# # Bảng ánh xạ emoji -> hex
# CharSet = {
#     "🐱": "0", "🐈": "1", "😸": "2", "😹": "3",
#     "😺": "4", "😻": "5", "😼": "6", "😽": "7",
#     "😾": "8", "😿": "9", "🙀": "A", "🐱👤": "B",
#     "🐱🏍": "C", "🐱💻": "D", "🐱👓": "E", "🐱🚀": "F"
# }

# # Hàm làm sạch chuỗi emoji (loại bỏ ký tự không cần thiết)
# def clean_emoji(text):
#     return text.replace('\u200d', '')  # Loại bỏ ký tự ZWJ

# # Hàm chuyển emoji -> hex
# def emojis_to_hex(emoji_text):
#     emoji_text = clean_emoji(emoji_text)  # Làm sạch chuỗi emoji
#     hex_text = ""
#     i = 0
#     while i < len(emoji_text):
#         # Kiểm tra các emoji dài (2 ký tự)
#         if i + 1 < len(emoji_text) and emoji_text[i:i+2] in CharSet:
#             hex_text += CharSet[emoji_text[i:i+2]]
#             i += 2
#         # Kiểm tra các emoji ngắn (1 ký tự)
#         elif emoji_text[i] in CharSet:
#             hex_text += CharSet[emoji_text[i]]
#             i += 1
#         else:
#             raise ValueError(f"Emoji không xác định: {emoji_text[i:i+2]}")
#     return hex_text

# # Đọc dữ liệu từ file
# with open("example_input.txt", "r") as f:
#     example_input = f.read().strip()

# with open("example_output.txt", "r") as f:
#     example_output = f.read().strip()

# with open("flag_output.txt", "r") as f:
#     flag_output = f.read().strip()

# # Tính toán key
# example_hex = emojis_to_hex(example_output)
# example_keyed_text = bytes.fromhex(example_hex).decode()

# keys = [ord(example_keyed_text[i]) - ord(example_input[i]) for i in range(len(example_input))]

# # Giải mã flag
# flag_hex = emojis_to_hex(flag_output)
# flag_keyed_text = bytes.fromhex(flag_hex).decode()

# decoded_flag = "".join([chr(ord(flag_keyed_text[i]) - keys[i % len(keys)]) for i in range(len(flag_keyed_text))])

# print("Flag:", decoded_flag)



cs = {
    "🐱‍👤": 'B',
    "🐱‍🏍": 'C', "🐱‍💻": 'D', "🐱‍👓": 'E', "🐱‍🚀": 'F',
    "🐱": '0', "🐈": '1', "😸": '2', "😹": '3',
    "😺": '4', "😻": '5', "😼": '6', "😽": '7',
    "😾": '8', "😿": '9', "🙀": 'A'
}

cs_inv = {v: k for k, v in cs.items()}

example_input = "You fools! You will never get my catnip!!!!!!!"
example_out = "🐱‍💻😸😿😼🐱‍👓😺😾😿🙀🐱‍💻🐱‍👓😺😿😹😿🐱‍💻🐱‍👓🐱🐱‍👤😹😿😺🐱‍👓😹🙀😿😾🐱‍🏍🐱‍👓😹😾🐱‍🚀🐱‍👤😾🐱‍💻🐱‍👓😿😽🐱‍👓😺😾🐱‍👤🙀😻🐱‍👓😸🙀😼🐱‍👤🐈🐱‍👓😺🐱‍👤😼😿😾🐱‍👓🐈😿😽🙀🐱‍🚀🐱‍👓😹😾😹🐱‍👤🐱‍👤🐱‍👓😹🙀🐱🐱‍👤😾🐱‍👓🐱🙀😽😿😻🐱‍👓😹🐱‍👤🐱🐱‍👤🐱‍👤🐱‍👓🐈😾😽😿🐱‍💻🐱‍👓🐈🙀🐱‍👓😿🐱‍👤🐱‍👓😹🐱‍👤🐱‍👤😾🐱‍🏍🐱‍👓🐈🐱‍👤🐱😿🐱‍👤🐱‍👓😸😾😿🐱‍👤😾🐱‍💻🐱‍🏍😿🙀🐱‍👓😸😾🙀🙀🐱🐱‍👓😸🐱‍👤🐱‍👓🙀🐱‍👓🐱‍👓🐱🙀🙀😾😺🐱‍👓😺🙀😽😿😸🐱‍👓😸🐱‍👤😾🙀🐈🐱‍👓😺🙀😼🙀😼🐱‍👓😺😿😿😿😿🐱‍🏍😿😾🐱‍👓🐱‍👓😺😿😽😿🐱‍🏍🐱‍👓🐈😾🐈😿😹🐱‍💻😸🐱‍👤😹🐱‍👓😺😿🐱‍👓🙀🐱🐱‍👓😺🙀🐱‍👤😾🐱‍🏍🐱‍👓😹🐱‍👤😸🙀🐱‍🏍🐱‍👓😹🐱‍👤😼🐱‍👤😾🐱‍👓🐱🙀🐈🐱‍👤🐈🐱‍👓😺😿🐱‍👤🐱‍👤😽🐱‍👓😸🐱‍👤🐈🐱‍👤🐱‍🚀🐱‍👓😺🐱‍👤😽🙀😿🐱‍👓😺😿🐱‍💻🙀😿🐱‍👓😺😾🐱‍👤😿🐱‍🚀🐱‍👓😸🙀🐱‍🏍🐱‍👤😻🐱‍👓😸🐱‍👤🐱‍💻🐱‍👤😾🐱‍👓😹😿😻🙀🐱‍🚀🐱‍👓😹😿😿😿😿"
flag_out = "🐱‍💻😸🙀😼🐱‍👓😺😾😿🐱‍👤🐱🐱‍👓😺😿😹😿🐈🐱‍👓🐱🐱‍👤😺🙀😽🐱‍👓😹🙀😿😾😿🐱‍👓😹😾🐱‍🚀🐱‍👤🐱‍💻🐱‍💻🐱‍👓😾🐱‍👓🐱‍👓😺😾🐱‍👤🐱‍👤😺🐱‍👓😸🙀😼🐱‍👤🐈🐱‍👓😺🐱‍👤😼🙀😽🐱‍👓🐈😿😾🐱‍👤🐱‍🏍🐱‍👓😹😾😹😿😻🐱‍👓😹🙀🐱😾🐱🐱‍👓🐱🙀😼😿🐈🐱‍👓😹🐱‍👤😸😾😾🐱‍👓🐈😾😼😿😿🐱‍👓🐈🙀🐱‍👓🙀😻🐱‍👓😹🐱‍👤🙀🐱‍👤🐱‍🚀🐱‍👓🐈🐱‍👤🐱😿🐈🐱‍👓😸😾🙀🐱‍👤🐈🐱‍💻🐱‍👤🙀😹🐱‍👓😸😾😿🙀🐱‍👓🐱‍👓😸🐱‍👤🐱‍💻🙀🐱‍💻🐱‍👓🐱🙀😿🐱‍👤🐱‍👓🐱‍👓😺🙀😼😿😺🐱‍👓😸🐱‍👤😿🐱‍👤😹🐱‍👓😺🙀😻🐱‍👤😸🐱‍👓😺😿😿🙀😸🐱‍🏍😾😿🐈🐱‍👓😺😿😾😿🐱‍👤🐱‍👓🐈😾🐈😿🐱‍💻🐱‍💻😸🙀😸🐱‍👓😺😿🐱‍👓🐱‍👤😺🐱‍👓😺🙀🙀🙀🐱🐱‍👓😹🐱‍👤😸🙀🙀🐱‍👓😹🐱‍👤😼🐱‍👤🐱‍💻🐱‍👓🐱🙀🐱🐱‍👤😹🐱‍👓😺😿🐱‍🏍😾😹🐱‍👓😸🐱‍👤🐈🙀🐱‍👓🐱‍👓😺🐱‍👤😽🐱‍👤🐱‍👤🐱‍👓😺😿🐱‍🚀😾🐱🐱‍👓😺😾🐱‍🏍🙀🐱‍👓🐱‍👓😸🙀🐱‍💻😾😽🐱‍👓😸🐱‍👤🐱‍👓🐱‍👤🙀🐱‍👓😹😿😼😾😻🐱‍👓😹😿🙀🐱‍👤😻"

def decode_emojis(emojis):
    pos = 0
    out = ""

    while pos < len(emojis):
        for num, ch in cs_inv.items():
            if len(ch) == 1:
                if emojis[pos] == ch:
                    out += num
                    pos += 1
                    break
            else:
                if emojis[pos:pos+3] == ch:
                    out += num
                    pos += 3
                    break
        
    return bytes.fromhex(out).decode("utf-8")

out_ct = decode_emojis(example_out)
flag_ct = decode_emojis(flag_out)

key = [ord(b) - ord(a) for a, b in zip(example_input, out_ct)]
flag = [chr(ord(b) - k) for k, b in zip(key, flag_ct)]

print("".join(flag))
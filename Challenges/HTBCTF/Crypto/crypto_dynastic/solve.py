def decrypt(encrypted_text):
    decrypted = ''
    for i in range(len(encrypted_text)):
        ch = encrypted_text[i]
        if not ch.isalpha():
            decrypted += ch
        else:
            chi = ord(ch) - 0x41
            original = (chi - i + 26) % 26  # Thêm 26 để tránh số âm
            decrypted += chr(original + 0x41)
    return decrypted

# Chuỗi đã mã hóa
encrypted = "DJF_CTA_SWYH_NPDKK_MBZ_QPHTIGPMZY_KRZSQE?!_ZL_CN_PGLIMCU_YU_KJODME_RYGZXL"

# Giải mã và in kết quả
decrypted = decrypt(encrypted)
flag = "HTB{" + decrypted + "}"
print(flag)

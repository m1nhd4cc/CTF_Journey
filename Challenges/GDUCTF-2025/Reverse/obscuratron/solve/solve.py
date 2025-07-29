def decrypt(filename_enc, filename_out):
    with open(filename_enc, 'rb') as f:
        data = f.read()

    decrypted = bytearray()
    
    if len(data) == 0:
        print("File is empty!")
        return
    
    # First byte
    decrypted.append(data[0] ^ 0xAB)
    
    # From second byte
    for i in range(1, len(data)):
        decrypted.append(data[i] ^ data[i-1])

    with open(filename_out, 'wb') as f:
        f.write(decrypted)

    print(f"Decryption complete! Output: {filename_out}")

decrypt('memo.pdf.enc', 'memo_decrypted.pdf')


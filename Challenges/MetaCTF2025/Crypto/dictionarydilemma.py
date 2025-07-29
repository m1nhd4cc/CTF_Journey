# Just use a short word you'll remember!
def encrypt(text, key):
    if len(key) > 6:
        print("Sorry, your key is too long!")
        return

    key = key.upper()

    for c in key:
        if c not in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
            print("The key may only contain english letters!")
            return

    ciphertext = ""

    for i in range(0, len(text)):
        code = hex(ord(text[i]) ^ ord(key[i % len(key)]))[2:]
        if len(code) < 2:
            code = "0" + code
        ciphertext += code
    print(ciphertext)


# The key is the same word you used for encrypt!
def decrypt(text, key):
    if len(key) > 6:
        print("Sorry, your key is too long! Are you sure it's the same key you used to encrypt?")
        return False

    key = key.upper()

    for c in key:
        if c not in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
            print("The key may only contain english letters! Are you sure it's the same key you used to encrypt?")
            return False

    plaintext = ""

    for i in range(0, len(text), 2):
        code = chr(int(text[i:i+2], 16) ^ ord(key[int(i / 2) % len(key)]))
        if code not in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*_ ;":
            return False

        plaintext += code

    print(plaintext)
    
    return True

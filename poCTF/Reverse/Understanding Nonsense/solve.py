def print_flag_hex(flag):
    print("Flag in hex: ", end='')
    for byte in flag:
        print(f"{byte:02x}", end=' ')
    print()

def reverse_modify_flag(flag, seed):
    length = len(flag)
    for i in range(length):
        flag[i] = (flag[i] - (seed % 10)) % 256
        seed = seed // 10
        if seed == 0:
            seed = 88974713  # Reset seed if it runs out

def bytes_to_string(flag):
    return ''.join(chr(byte) for byte in flag)

def main():
    encoded_flag = [
        0x8e, 0x79, 0xa9, 0x9c, 0xac, 0xd5, 0xc5, 0xc7,
        0x91, 0x7a, 0xa5, 0x8a, 0xb8, 0x8d, 0xc6, 0x81,
        0x55, 0x83, 0xa5, 0x59, 0x7b, 0xb9, 0x87, 0xb8,
        0x51, 0x69, 0x7b, 0x58, 0xbb, 0x8b, 0xcd
    ]

    seed = 88974713
    length = len(encoded_flag)

    print("Encoded flag: ", end='')
    print_flag_hex(encoded_flag)

    # Reverse the modifications 10 times
    for _ in range(10):
        reverse_modify_flag(encoded_flag, seed)

    decoded_flag = bytes_to_string(encoded_flag)
    
    print("Decoded flag (plaintext):", decoded_flag)
    print("Decoded flag (plaintext in hex): ", end='')
    print_flag_hex(encoded_flag)

if __name__ == "__main__":
    main()

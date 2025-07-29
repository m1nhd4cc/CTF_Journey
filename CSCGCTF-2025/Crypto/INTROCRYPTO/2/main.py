def hex_to_ascii(hex_string):
    bytes_object = bytes.fromhex(hex_string)
    ascii_string = bytes_object.decode("ascii", errors="ignore")
    return ascii_string

# Example usage
hex_string = "0B05041583000000030103013000480E01FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFBFFF9FFFFF3FFC71FFFFFFDFFFEFBFFDED0F32"
print(hex_to_ascii(hex_string))

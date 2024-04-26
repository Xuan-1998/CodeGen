def findComplement(N):
    # Calculate the number of bits in the binary representation of N
    num_bits = N.bit_length()

    # Create a mask with all 1s for the given number of bits
    mask = (1 << num_bits) - 1

    # Flip the bits by doing bitwise XOR with the mask
    complement = N ^ mask

    return complement

N = int(input())
print(findComplement(N))

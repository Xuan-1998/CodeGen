def findComplement(N):
    # Convert the number to binary and remove the '0b' prefix
    bin_N = bin(N)[2:]

    # Calculate the total number of bits (including leading zeros)
    num_bits = len(bin_N)

    # The complement is obtained by flipping all bits, which can be done by subtracting 1 from a power of 2
    complement = int('1' * num_bits, 2) - N

    return complement

N = int(input())
print(findComplement(N))

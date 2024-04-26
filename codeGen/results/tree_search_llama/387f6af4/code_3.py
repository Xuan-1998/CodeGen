import sys

def find_complement(N):
    # Convert the binary representation of N to an integer
    bin_N = bin(N)[2:]

    # Calculate the complement by inverting all bits using XOR (^)
    complement = int('1' * len(bin_N), 2) ^ int(bin_N, 2)

    return complement

N = int(sys.stdin.readline())
print(find_complement(N))

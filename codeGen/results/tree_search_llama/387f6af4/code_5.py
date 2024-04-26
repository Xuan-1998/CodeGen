import sys

def find_complement(N):
    # Convert N to binary and remove the '0b' prefix
    bin_N = bin(N)[2:]

    # Initialize the result with all bits set to 1 (complement of 0)
    complement = '1' * len(bin_N)

    # Flip each bit in the complement if the original bit is 1
    for i, bit in enumerate(bin_N):
        if bit == '1':
            complement = list(complement)[::-1]
            complement = ''.join(['0'] if c == '1' else ['1'] for c in complement)
            break

    # Convert the binary result back to an integer and return it
    return int(complement, 2)

# Read input from stdin
N = int(sys.stdin.readline())

# Calculate and print the result
print(find_complement(N))

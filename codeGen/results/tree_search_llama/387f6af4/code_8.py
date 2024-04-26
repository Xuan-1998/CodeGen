def findComplement(N):
    # Convert N from decimal to binary, remove the '0b' prefix, and convert back to decimal
    bin_N = bin(N)[2:]
    
    # Calculate all ones (2^n - 1)
    all_ones = 2 ** len(bin_N) - 1
    
    # Flip each bit in the binary representation of N using bitwise operator (^)
    complement = int(str(all_ones ^ int(bin_N, 2)), 10)
    
    return complement

N = int(input())
print(findComplement(N))

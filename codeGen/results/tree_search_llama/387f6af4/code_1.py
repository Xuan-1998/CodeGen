def find_complement(n):
    # Convert the integer to its binary representation
    binary_n = bin(n)[2:]
    
    # Calculate the total number of bits in the binary representation
    num_bits = len(binary_n)
    
    # Initialize an empty string to store the complemented binary representation
    complement_binary = ''
    
    # Iterate over each bit in the binary representation
    for i in range(num_bits):
        # If the current bit is 0, add a 1 to the complemented binary representation
        if binary_n[i] == '0':
            complement_binary += '1'
        # If the current bit is 1, add a 0 to the complemented binary representation
        else:
            complement_binary += '0'
    
    # Convert the complemented binary representation back to an integer and return it
    return int(complement_binary, 2)

n = int(input())
print(find_complement(n))

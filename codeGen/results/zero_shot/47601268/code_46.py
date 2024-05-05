import sys

def count_binary_numbers(n):
    count = 0
    for i in range(n + 1):
        # Convert integer to binary and remove leading zeros
        binary = bin(i)[2:]
        
        # Check if the binary representation has consecutive ones
        has_consecutive_ones = False
        for j in range(len(binary) - 1):
            if binary[j] == '1' and binary[j + 1] == '1':
                has_consecutive_ones = True
                break
        
        # If no consecutive ones, increment the count
        if not has_consecutive_ones:
            count += 1
    
    return count

n = int(sys.stdin.readline())
print(count_binary_numbers(n))

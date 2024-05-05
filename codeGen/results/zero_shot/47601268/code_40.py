import sys

def find_non_consecutive_ones(n):
    count = 0
    for i in range(2**n):  # Generate all binary numbers from 0 to n (inclusive)
        binary = bin(i)[2:]  # Convert integer to binary and remove the '0b' prefix
        has_consecutive_ones = False
        for j in range(len(binary) - 1):
            if binary[j] == '1' and binary[j+1] == '1':  # Check for consecutive ones
                has_consecutive_ones = True
                break
        if not has_consecutive_ones:  # If no consecutive ones, increment the count
            count += 1
    return count

n = int(sys.stdin.readline())
print(find_non_consecutive_ones(n))

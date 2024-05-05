import sys

def count_binary_numbers(n):
    count = 0
    for i in range(n+1):
        binary = bin(i)[2:] # Convert integer to binary, remove '0b' prefix
        no_consecutive_ones = True
        for j in range(len(binary)-1): # Check each pair of consecutive bits
            if binary[j] == '1' and binary[j+1] == '1':
                no_consecutive_ones = False
                break
        if no_consecutive_ones:
            count += 1
    return count

n = int(sys.stdin.readline())
print(count_binary_numbers(n))

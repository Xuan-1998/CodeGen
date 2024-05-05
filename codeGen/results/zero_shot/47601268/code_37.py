import sys

def has_consecutive_ones(n):
    binary = bin(n)[2:]  # Convert to binary and remove '0b' prefix
    for i in range(len(binary) - 1):  # Check each pair of bits
        if binary[i] == '1' and binary[i+1] == '1':
            return True
    return False

def count_integers_without_consecutive_ones(n):
    count = 0
    for i in range(n + 1):
        if not has_consecutive_ones(i):
            count += 1
    return count

n = int(sys.stdin.readline())
print(count_integers_without_consecutive_ones(n))

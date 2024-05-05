import sys

def count_binary_repr(n):
    total_count = 0
    for i in range(2**(n+1)):
        binary_str = bin(i)[2:].zfill(n+1)
        if not has_consecutive_ones(binary_str):
            total_count += 1
    return total_count

def has_consecutive_ones(binary_str):
    for i in range(len(binary_str) - 1):
        if binary_str[i] == '1' and binary_str[i+1] == '1':
            return True
    return False

n = int(sys.stdin.readline())
print(count_binary_repr(n))

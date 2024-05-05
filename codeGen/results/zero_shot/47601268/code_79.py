import sys

def binary_has_consecutive_ones(n):
    return bin(n).count('1') % 2 == 0

def count_numbers_without_consecutive_ones(n):
    count = 0
    for i in range(n+1):
        if not binary_has_consecutive_ones(i):
            count += 1
    return count

n = int(sys.stdin.readline())
print(count_numbers_without_consecutive_ones(n))

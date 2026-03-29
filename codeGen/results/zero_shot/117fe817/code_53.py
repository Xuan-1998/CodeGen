import sys

def count_digit_ones(n):
    total_ones = 0
    for i in range(n + 1):
        ones_in_i = bin(i).count('1')
        multiplier = n - i + 1
        total_ones += ones_in_i * multiplier
    return total_ones

n = int(sys.stdin.readline())
print(count_digit_ones(n))

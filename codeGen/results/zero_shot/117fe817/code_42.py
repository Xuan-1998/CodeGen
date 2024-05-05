def count_digit_ones(n):
    ones_per_multiple_of_10 = 0
    for i in range(1, n+1):
        if i % 10 == 0:
            ones_per_multiple_of_10 += 1
    total_ones = ones_per_multiple_of_10 * (n // 10 + 1)
    return total_ones

import sys
n = int(sys.stdin.readline())
print(count_digit_ones(n))

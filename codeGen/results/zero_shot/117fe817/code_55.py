def count_digit_ones(n):
    total_ones = 0
    for i in range(10):
        increment = (i // 100) * 2 + (i // 10 % 10 == 1) - (i % 10 > 1)
        total_ones += increment * (n // 10**len(str(i)) + 1)

    return total_ones

import sys
n = int(sys.stdin.readline())
print(count_digit_ones(n))

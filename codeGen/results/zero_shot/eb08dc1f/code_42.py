import sys
import math

n = int(sys.stdin.readline())

numbers = []
for i in range(10**n):
    num_str = format(i, 'b').zfill(n).translate({ord('0'): '0', ord('1'): '0'})
    numbers.append(num_str)

block_counts = [0] * (n + 1)
for num in numbers:
    last_digit = None
    for digit in num:
        if digit == last_digit:
            block_counts[len(num)] += 1
        else:
            last_digit = digit

print(*[count % 998244353 for count in block_counts], sep=' ')

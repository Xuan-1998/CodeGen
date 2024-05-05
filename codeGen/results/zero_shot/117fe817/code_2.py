import sys

def count_digit_ones(n):
    k = bin(n).count('1')
    return sum(2**i - 2**(i-1) if (2**i & n) else 0 for i in range(k+1))

n = int(sys.stdin.readline())
print(count_digit_ones(n))

import math

def count_digit_ones(n):
    total = 0
    for i in range(10):
        total += (n // (10 ** (i + 1))) * (10 ** i - 9) * i
    return total

n = int(input())
print(count_digit_ones(n))

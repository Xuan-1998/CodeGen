import math

def count_digit_ones(n):
    total_digits = sum(range(n+1))
    return sum(math.floor(math.log10(i)) + 1 for i in range(n+1))

n = int(input())  # read input from stdin
print(count_digit_ones(n))  # print the result to stdout

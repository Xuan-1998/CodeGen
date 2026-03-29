import sys

def min_operations(n, x):
    ops = 0
    while len(str(x)) < n:
        max_digit = int('9' * (len(str(x)) + 1))
        if x > max_digit:
            # If x is too big, we can't make it shorter by multiplying
            return -1
        x *= 10  # Shift left and add a 0 to the front
        ops += 1
    return ops

n = int(input())
x = int(input())
print(min_operations(n, x))

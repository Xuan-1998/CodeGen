import sys

def min_operations(n, x):
    ops = 0
    while len(str(x)) < n:
        for digit in range(10):
            if int((x * 10 + digit) / 10**len(str(x))) == x:
                x *= 10 + digit
                ops += 1
                break
        else:
            return -1
    return ops

n, x = map(int, input().split())
print(min_operations(n, x))

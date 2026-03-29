import sys

def min_operations(n, x):
    ops = 0
    while len(str(x)) < n:
        if str(x).endswith('9'):
            x *= 10
        else:
            x *= int(str(x)[-1]) + 1
        ops += 1
    return ops if len(str(x)) == n else -1

n, x = map(int, input().split())
print(min_operations(n, x))

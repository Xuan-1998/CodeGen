import sys

def min_operations(n, x):
    min_ops = float('inf')
    for y in range(10):
        while len(str(x * y)) < n:
            x *= y
        if len(str(x)) == n:
            min_ops = min(min_ops, 1)
            break
    return -1 if min_ops == float('inf') else min_ops

n, x = map(int, input().split())
print(min_operations(n, x))

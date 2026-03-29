import sys
import math

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def solve(n, arr):
    if 1 in arr:
        return n - arr.count(1)

    min_ops = float('inf')
    for i in range(n):
        g = arr[i]
        for j in range(i+1, n):
            g = gcd(g, arr[j])
            if g == 1:
                min_ops = min(min_ops, j - i)
                break

    if min_ops == float('inf'):
        return -1
    else:
        return min_ops + n - 1

n = int(input().strip())
arr = list(map(int, input().strip().split()))
print(solve(n, arr))


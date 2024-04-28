import sys
from collections import defaultdict

n, k = map(int, input().split())
arr = list(map(int, input().split()))

dp = defaultdict(int)

def solve():
    for i in range(n):
        for j in range(i+1, n+1):
            max_val = max(arr[i:j])
            if max_val > k:
                dp[(i, j)] = 1
            else:
                dp[(i, j)] = 0

    res = 0
    for i in range(n):
        for j in range(i+1, n+1):
            res += dp.get((i-1, j), 0) if i > 0 else dp.get((j, k)) or 0

    return res

print(solve())

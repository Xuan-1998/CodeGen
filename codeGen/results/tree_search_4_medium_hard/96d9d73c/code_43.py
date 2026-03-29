===BEGIN CODE===
import sys

def solve():
    n, k, m = map(int, input().split())
    a = list(map(int, input().split()))
    
    dp = [[False] * (k + 1) for _ in range(n)]
    memo = {(0, j): True for j in range(k + 1)}
    
    for i in range(1, n):
        for j in range(min(i // m, k), -1, -1):
            if dp[i - 1][j] and a[i - 1] - a[0] <= m:
                dp[i][j] = True
    
    return "Yes" if dp[-1][-1] else "No"

print(solve())

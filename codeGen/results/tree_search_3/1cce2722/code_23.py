from collections import deque

def solve():
    n = int(input())
    a = list(map(int, input().split()))
    
    dp = [[0] * (max(a) + 1) for _ in range(n)]
    
    for i in range(n):
        for k in range(max(a) + 1):
            if a[i] == k:
                dp[i][k] = i
            else:
                dp[i][k] = max(dp[i-1].get(l, 0) for l in range(k-1, k+2))
    
    return sum(max(dp[i]) for i in range(n))

print(solve())

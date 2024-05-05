import sys

def solution():
    n, m, h = map(int, input().split())
    s = list(map(int, input().split()))
    
    if sum(s) < n:
        print(-1)
        return
    
    p = sum(1 for si in s[:h] if si > 0) / h
    dp = [0.0] * (n + 1)
    dp[0] = 1.0
    
    for i in range(h):
        for j in range(n, -1, -1):
            if j >= i:
                dp[j] = max(dp[j], dp[j - i] + p * (1 - dp[i]))
    
    print(min(1.0 - (1.0 - p)**(n), 1.0))

solution()

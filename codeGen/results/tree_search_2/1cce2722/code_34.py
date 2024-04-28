from collections import defaultdict

def solve():
    n = int(input())
    a = list(map(int, input().split()))
    
    dp = [0] * (n + 1)
    for i in range(1, n + 1):
        if i == 1:
            dp[i] = 1
        elif a[i - 1] > a[i - 2]:
            dp[i] = min(dp[i - 1], dp[i - 2]) + 1
        else:
            dp[i] = dp[i - 1]
    
    return n - dp[n]

print(solve())

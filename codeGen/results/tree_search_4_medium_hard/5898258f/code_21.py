import sys

t = int(input())
for _ in range(t):
    n, x = map(int, input().split())
    a = list(map(int, input().split()))
    
    dp = [0] * (n + 1)
    dp[1] = a[0] ^ a[1]
    
    for i in range(2, n + 1):
        dp[i] = max(dp[i-1], dp[i-2] + a[i-1] ^ a[i])
    
    print(max(dp))

import sys

n = int(input())

dp = [0] * (n + 1)

for i in range(1, n + 1):
    a, b, c = map(int, input().split())
    
    # If we feed the i-th hare
    dp[i] = max(dp[i - 1], dp[i - 2] + c)
    
    # If we don't feed the i-th hare
    if i > 1:
        dp[i] = max(dp[i], max(dp[i - 1], dp[i - 2] + a) if i % 2 == 0 else dp[i - 1] + b)

print(max(dp))

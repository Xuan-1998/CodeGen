codeblock
n = int(input())
k = list(map(int, input().split()))
h = list(map(int, input().split()))

dp = [float('inf')] * (10**9 + 1)
dp[0] = 0

for t in range(1, len(k) + 1):
    dp[t] = min(dp[max(0, t-1)] + h[t-1], dp[t-1] + 1)

print(min(dp))

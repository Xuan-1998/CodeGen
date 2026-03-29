import heapq
n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = list(map(int, input().split()))

dp = [0] * (n + 1)
for i in range(n):
    dp[i+1] = max(dp[i] + a[i], dp[i-1] + b[i])
    if i > 0:
        dp[i+1] = max(dp[i+1], dp[i-1] + c[i])

print(max(dp))

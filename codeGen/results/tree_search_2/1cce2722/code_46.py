n = int(input())
a = list(map(int, input().split()))

dp = [float('inf')] * n

for i in range(n):
    if i > 0 and i < n-1:
        dp[i] = 1 + min(dp[j] for j in range(max(0, i-2), min(n, i+2))) if a[i] == a[i-1] or a[i] == a[i+1] else n

print(min(dp))

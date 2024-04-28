n = int(input())
a = list(map(int, input().split()))
dp = [n] * n

for i in range(1, n):
    for j in range(max(0, i-2), min(n-1, i+2)):
        if a[j] <= a[i]:
            dp[i] = min(dp[i], dp[j] + 1)

print(min(dp))

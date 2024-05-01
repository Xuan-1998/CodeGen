===BEGIN CODE===
n = int(input())
a = list(map(int, input().split()))
dp = [0] * n

for i in range(1, n):
    if a[i-1] > 0 and (i == 1 or a[i-2] != a[i-1]):
        for j in range(i):
            dp[i] = max(dp[i], dp[j] + (n - j) - i)

print(max(0, *dp))
===END CODE===

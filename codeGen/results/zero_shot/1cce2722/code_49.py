n = int(input())
a = list(map(int, input().split()))
dp = [1] * n
for i in range(1, n):
    for j in range(i):
        if abs(a[i] - a[j]) == 1:
            dp[i] = max(dp[i], dp[j] + 1)
print(max(dp))

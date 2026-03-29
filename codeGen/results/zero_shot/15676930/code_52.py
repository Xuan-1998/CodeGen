n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = list(map(int, input().split()))

dp = [0] * (n + 1)
for i in range(1, n + 1):
    dp[i] = max(
        c[i-1] if i > 1 else 0,
        b[i-1],
        a[i-1] if i == 1 or i == n else 0
    ) + dp[i-1]

print(dp[-1])

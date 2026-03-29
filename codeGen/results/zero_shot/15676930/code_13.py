n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = list(map(int, input().split()))

dp = [0] * (n + 1)
for i in range(1, n):
    dp[i] = max(dp[i - 2] + a[i], dp[i - 1] + b[i], dp[i - 1] + c[i])
print(max(dp))

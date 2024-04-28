n = int(input())
a = list(map(int, input().split()))

dp = [n] * n

for i in range(1, n):
    if a[i] == a[0] + 1 or a[i] == a[0] - 1:
        dp[i] = min(dp[j] for j in range(max(0, i-2), min(n, i+2))) + 1
    else:
        dp[i] = n

print(min(dp))

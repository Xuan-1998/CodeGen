n = int(input())
a = list(map(int, input().split()))
dp = [0] * (n + 1)

for i in range(1, n):
    k = i - 2 if a[i-2] <= a[i] else i + 2
    dp[i] = min(dp[j] for j in range(max(k-2, 0), min(k+2, n)))
    dp[i] += 1

print(n - max(dp))

n = int(input())
a = list(map(int, input().split()))
dp = [0] * n

for i in range(n):
    k = min(j for j in range(i) if a[j] <= a[i])
    dp[i] = 1 + sum(dp[j] for j in range(k-2, k+3))

print(max(dp))

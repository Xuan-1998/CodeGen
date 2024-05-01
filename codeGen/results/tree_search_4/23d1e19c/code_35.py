n, m = map(int, input().split())
p = list(map(int, input().split()))
dp = [0] * (k + 1)
dp_max = [0] * (k + 1)

for i in range(1, k):
    dp[i] = min(dp[i-1][0], 1) + abs(p[i]-p[i-1])
    dp_max[i] = max(dp_max[i-1], 1)

print(min(dp), max(dp))

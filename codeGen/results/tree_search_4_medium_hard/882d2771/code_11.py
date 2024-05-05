import sys; input = lambda: sys.stdin.readline().strip()
t, l, r = map(int, input().split())
dp = [0] * (r + 1)
prefix_sum = [0] * (r + 1)

for i in range(l - 1, r):
    dp[i + 1] = 1 + min(dp[j] for j in range(l - 1, i))

for i in range(r):
    prefix_sum[i + 1] = 1 + min(prefix_sum[j] for j in range(i, l - 1) if j >= l)

print(sum(t * dp[i] for i in range(l, r + 1)) % (10**9 + 7))

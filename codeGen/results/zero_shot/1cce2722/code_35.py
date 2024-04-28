n = int(input())
seq = list(map(int, input().split()))
dp = [0] * (n + 1)
for i in range(2, n):
    dp[i] = max(dp[i - 1], dp[i - 2] + 1 if seq[i - 1] == seq[i] or seq[i] == seq[i + 1] else dp[i - 1])
print(dp[-1])

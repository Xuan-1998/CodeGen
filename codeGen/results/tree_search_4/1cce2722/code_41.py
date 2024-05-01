n = int(input())
sequence = list(map(int, input().split()))

dp = [0] * (n + 1)

for i in range(1, n + 1):
    dp[i] = max(dp[j] + 1 for j in range(i) if abs(a_j - a_i) == 1)

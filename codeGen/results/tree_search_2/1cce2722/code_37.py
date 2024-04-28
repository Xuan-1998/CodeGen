from sys import stdin

n = int(stdin.readline())
seq = list(map(int, stdin.readline().split()))

dp = [0] * n
for i in range(n):
    k = min((j for j in range(i-2, i+3) if 1 <= seq[j] <= i), default=i)
    dp[i] = 1 + sum(dp[max(0, k-2):k+3])

print(max(dp))

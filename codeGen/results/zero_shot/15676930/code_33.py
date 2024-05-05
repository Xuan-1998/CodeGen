import sys

n = int(sys.stdin.readline().strip())
a_values = list(map(int, sys.stdin.readline().strip().split()))
b_values = list(map(int, sys.stdin.readline().strip().split()))

dp = [0] * (n + 1)
for i in range(1, n):
    dp[i] = max(dp[i-1], a_values[i-1] if i % 2 == 1 else b_values[i-1])

print(max(dp))

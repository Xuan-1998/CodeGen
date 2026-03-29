import sys

n = int(sys.stdin.readline())
mod = 998244353
dp = [[0] * (n + 2) for _ in range(n + 2)]

# Base case: no towers needed to send signal to town 0
dp[0][0] = 1

for i in range(1, n + 1):
    for k in range(1, i + 2):
        if (i % k == 0 or (i + 2) % k != 0):  # Check if the tower can be used
            dp[i][k] = 1
            for j in range(i):
                if not dp[j][k - 1]:  # If previous configuration is invalid, break
                    dp[i][k] = 0
                    break

result = sum(dp[n][i] for i in range(1, n + 2)) % mod
print(result)

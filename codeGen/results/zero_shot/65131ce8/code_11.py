python
def count_good_vertices(N, d):
    MOD = 998244353

    # Initialize dp array
    dp = [[0] * (N + 1) for _ in range(N + 1)]
    dp[0][0] = 1

    # Fill dp array
    for i in range(1, N + 1):
        for j in range(N + 1):
            dp[i][j] = dp[i - 1][j]
            if j >= d[i - 1]:
                dp[i][j] = (dp[i][j] + dp[i - 1][j - d[i - 1]]) % MOD

    # Calculate the number of good vertices
    result = 0
    for i in range(1, N + 1):
        if dp[N][i] > 0:
            result = (result + dp[N][i]) % MOD

    return result

import sys
input = sys.stdin.read
data = input().split()

N = int(data[0])
d = list(map(int, data[1:]))

print(count_good_vertices(N, d))


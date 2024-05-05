from collections import defaultdict

def count_ways(n, m):
    MOD = 10**9 + 7

    # Create a dictionary to memoize dp values
    dp = [[0] * (n+1) for _ in range(n+1)]
    dp[0][0] = 1

    for i in range(1, n+1):
        for j in range(i+1):
            if j == 0:
                dp[i][j] = dp[i-1][j]
            elif j == i:
                dp[i][j] = dp[i-1][j-1]
            else:
                for k in range(j+1):
                    dp[i][j] += dp[k][j-k]
                dp[i][j] %= MOD

    return dp[n-1][m-1]

# Read the input
n = int(input())
m = [int(x) for x in input().split()]

print(count_ways(n, sum(1 for x in m if x == 1)))

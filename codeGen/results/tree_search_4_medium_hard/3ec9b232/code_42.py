import sys

def count_ways(n):
    dp = [[0] * (n + 1) for _ in range(n + 1)]
    dp[0][n] = 1

    for i in range(1, n + 1):
        for j in range(i - 1, n):
            if M[j] >= M[i - 1]:
                dp[i][j] = sum(dp[i - 1][k] for k in range(j + 1, i))
            else:
                dp[i][j] = 0

    return dp[n][n]

if __name__ == "__main__":
    n = int(input())
    M = [int(x) for x in input().split()]
    print(count_ways(n) % (10**9 + 7))

import sys

def shortestUncommonSubsequence(S, T):
    m, n = len(S), len(T)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(m + 1):
        for j in range(n + 1):
            if i == 0 and j == 0:
                dp[i][j] = -1
            elif i > 0 and j > 0:
                if S[i-1] != T[j-1]:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
                else:
                    dp[i][j] = -1
            elif i > 0:
                dp[i][j] = dp[i-1][j]
            elif j > 0:
                dp[i][j] = dp[i][j-1]

    return dp[m][n]

if __name__ == "__main__":
    S, T = input().split()
    print(shortestUncommonSubsequence(S, T))

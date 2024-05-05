import sys

def solve(n, k):
    s = input().strip()
    dp = [[[] for _ in range(k+1)] for _ in range(n+1)]

    for i in range(1, n+1):
        if i == 1:
            for j in range(k+1):
                dp[i][j] = [s[0]]
        else:
            for j in range(k+1):
                if j == 0:
                    dp[i][j] = ['']
                elif j == 1:
                    dp[i][j] = [dp[i-1][0] + s[-1]]
                else:
                    dp[i][j] = min([s[:i-1][j-1]], [dp[i-1][j-1] + s[-1]] + [dp[i-1][j]])

    return ''.join(min(dp[n][k], key=len))

n, k = map(int, input().split())
print(solve(n, k))

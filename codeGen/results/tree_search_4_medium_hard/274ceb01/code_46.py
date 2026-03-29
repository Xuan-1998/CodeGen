from sys import stdin

def solve():
    n = int(stdin.readline())
    marks = [int(x) for x in stdin.readline().split()]

    dp = [[0] * (n + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for k in range(i):
            if k == 0:
                dp[i][k] = marks[i - 1]
            else:
                dp[i][k] = min(dp[j-1][0] + (i-j)*j for j in range(1, k+1)) + marks[i - 1]

    return dp[n][n]

print(solve())

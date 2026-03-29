from sys import stdin, stdout

n = int(stdin.readline())
m = int(stdin.readline())

dp = [[0 for _ in range(m + 1)] for _ in range(n + 1)]

for i in range(1, n + 1):
    for j in range(1, m + 1):
        if A[i - 1] == B[j - 1]:
            dp[i][j] = dp[i - 1][j - 1] + 1
        else:
            dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

similarity_score = 4 * dp[n][m] - n - m

stdout.write(str(similarity_score))

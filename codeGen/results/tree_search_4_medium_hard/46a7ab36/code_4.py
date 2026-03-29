t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    # Base case: when all letters have been placed or the alphabet is exhausted.
    for i in range(m + 1):
        if i == 0:
            dp[i][0] = 1
        elif i > 0 and j < n:
            dp[i][j] = sum(dp[i-1][m] for m in range(2*j+1) if 2*m <= n)
    # If the current letter can be placed as the last letter or followed by any letter,
    # include that possibility in the DP recurrence.
    for i in range(m + 1):
        dp[i][n] = sum(dp[i-1][m] for m in range(2*i+1) if 2*m <= n)

    print((dp[m][n] % (10**8 + 7)))

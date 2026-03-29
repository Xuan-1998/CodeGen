def solve(n, k):
    s = input().strip()
    dp = [["" for _ in range(k+1)] for _ in range(n+1)]

    for i in range(1, n+1):
        last_char = s[i-1]
        for j in range(min(i, k)+1):
            if j == 0:
                dp[i][j] = ""
            elif j > 0 and s[:i-j].endswith(last_char):
                dp[i][j] = dp[i-1][j-1] + last_char
            else:
                dp[i][j] = dp[i-1][j]

    return dp[n][k]

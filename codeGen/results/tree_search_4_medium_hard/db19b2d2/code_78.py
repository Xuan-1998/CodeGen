def solve(n, m, h, s):
    dp = [[0.0] * (n + 1) for _ in range(m)]

    # Base case: If h = 1, then the probability is either 0 (if s1 < n) or 1 (if s1 >= n)
    for i in range(h - 1):
        dp[i][0] = 1.0
    if s[h - 1] < n:
        dp[h - 1][0] = 0.0

    # Transition function: For each department i, calculate the probability dp[i][j] for all j ≤ si
    for i in range(m):
        for j in range(s[i] + 1):
            if j + 1 > h:
                dp[i][j] = dp[i][h - 1]
            else:
                dp[i][j] = dp[i][j - 1] + (s[i] - j) / s[i]

    # Return statement: The final answer is the probability that a team of size n has at least one player from department h
    if n > m:
        return -1.0
    else:
        return dp[h - 1][n]

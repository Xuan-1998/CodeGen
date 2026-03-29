def min_changes(s, k):
    n = len(s)
    dp = [[0] * (k + 1) for _ in range(n + k)]

    # Initialize the first column
    for i in range(n + k):
        dp[i][0] = 0

    # Fill up the array
    for i in range(1, n + k):
        for j in range(1, min(i, k) + 1):
            if s[i - k:i].count(s[i - 1]) == 1:
                dp[i][j] = dp[i - 1][k]
            else:
                changes = float('inf')
                for c in ['R', 'G', 'B']:
                    if s[i - 1] != c:
                        changes = min(changes, dp[i - 1][j - 1] + (s[i - 1] != c))
                dp[i][j] = changes

    return dp[n][k]

while True:
    n, k = map(int, input().split())
    s = input()
    print(min_changes(s, k))

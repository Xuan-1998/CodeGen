def min_changes_to_find_substring():
    n = int(input())
    k = int(input())
    s = input().strip()

    dp = [[0] * (k + 1) for _ in range(n + 1)]

    # Initialize the dp table
    for i in range(1, n + 1):
        dp[i][0] = i
    for j in range(1, k + 1):
        dp[0][j] = 0

    # Fill up the dp table row by row from left to right
    for i in range(1, n + 1):
        for j in range(1, min(i, k) + 1):
            if s[i - 1] != 'RGB'[j % 3]:
                dp[i][j] = min(dp[i - 1][j], dp[i - 1][j - 1]) + 1
            else:
                dp[i][j] = dp[i - 1][j]

    # Return the minimum value in the last column of the dp table
    return dp[n][k]

while True:
    try:
        n, k = map(int, input().split())
        print(min_changes_to_find_substring())
    except EOFError:
        break

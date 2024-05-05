def min_palindrome_cuts(s):
    n = len(s)
    dp = [[False] * (n + 1) for _ in range(n + 1)]

    # Initialize the diagonal of the dp table as True
    for i in range(n + 1):
        dp[i][i] = True

    # Fill the dp table using dynamic programming
    for j in range(2, n + 1):
        for i in range(n - j + 1):
            k = i + j // 2
            if s[i..k] == s[k..j]:  # Check if the substring is palindromic
                dp[i][j] = True

    # Count the minimum number of cuts needed
    min_cuts = 0
    for i in range(1, n):
        if not dp[0][i]:
            min_cuts += 1

    return min_cuts

def find_lexicographically_smallest_string():
    n, k = map(int, input().split())
    s = input()

    dp = [[[] for _ in range(k+1)] for _ in range(n+1)]

    # Base case: empty string
    for j in range(k+1):
        if j == 0:
            dp[0][j] = []

    # Fill up the dp array using recursion and memoization
    for i in range(1, n+1):
        for j in range(min(i, k)+1):
            if s[i-1] <= s[j-1]:  # Duplicate the string
                dp[i][j] = dp[i-1][j]
            else:  # Delete the last character
                dp[i][j] = dp[i-1][j-1]

    # Find the lexicographically smallest string of length k
    result = ''
    for j in range(k, -1, -1):
        if dp[n][j]:
            result += s[dp[n].index(dp[n][j])[-1]]
            n -= 1

    return result

print(find_lexicographically_smallest_string())

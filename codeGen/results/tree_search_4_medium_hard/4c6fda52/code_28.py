def min_changes(s, k):
    n = len(s)
    dp = [[0] * (k + 1) for _ in range(n - k + 2)]

    # Initialize the base case: changing all characters in the first j positions
    for j in range(k + 1):
        dp[0][j] = j

    for i in range(1, n - k + 2):
        for j in range(1, min(i + k, n) + 1):
            # If the last character matches the desired pattern
            if s[i + j - 1] == 'R' and dp[i][j - 1] > dp[i - 1][k - j]:
                dp[i][j] = min(dp[i][j - 1], dp[i - 1][k - j])
            else:
                dp[i][j] = dp[i][j - 1]

    # The answer is the minimum of the value at position n-k and k
    return min(dp[n - k][0], k)

# Example usage:
n, k = map(int, input().split())
s = input()
print(min_changes(s, k))

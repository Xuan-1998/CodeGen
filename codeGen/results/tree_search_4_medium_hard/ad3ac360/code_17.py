def min_cuts(s):
    n = len(s)
    dp = [[False] * (n+1) for _ in range(n+1)]

    # Base case: single-character strings are palindromes
    for i in range(n+1):
        dp[i][i] = True

    memo = {}

    def is_palindrome(s, i, j):
        if (i, j) in memo:
            return memo[(i, j)]

        if s[i:j+1] == s[i:j+1][::-1]:
            result = 1
        else:
            result = 0

        memo[(i, j)] = result
        return result

    for length in range(2, n+1):
        for i in range(n-length+1):
            j = i + length - 1
            if is_palindrome(s, i, j):
                dp[i][j] = True
            else:
                for k in range(i, j):
                    if dp[i][k] and dp[k+1][j]:
                        dp[i][j] = True
                        break

    # Compute the minimum number of cuts
    cuts = 0
    for i in range(n-1):
        if not dp[0][i]:
            cuts += 1

    return cuts

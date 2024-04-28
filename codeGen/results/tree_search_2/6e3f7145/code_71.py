def longest_palindromic_substring(S):
    n = len(S)
    dp = [[False] * (n + 1) for _ in range(n + 1)]

    # Initialize diagonal elements
    for i in range(n):
        dp[i][i] = True

    max_length = 0
    result = ""

    for i in range(n - 1, -1, -1):  # iterate from end to start
        for j in range(i + 1, n + 1):  # iterate from start to end
            if S[i] == S[j - 1]:
                dp[i][j - 1] = dp[i + 1][j - 2] or True
                if dp[i][j - 1]:
                    if j - i > max_length:
                        max_length = j - i
                        result = S[i:j]

    return result

# Read input from stdin and print the result to stdout
S = input()
print(longest_palindromic_substring(S))

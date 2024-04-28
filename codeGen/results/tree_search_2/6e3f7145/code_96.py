def longest_palindromic_substring():
    S = input()  # Read the input string from stdin

    n = len(S)
    dp = [[False] * n for _ in range(n)]

    max_len = 1
    result = S[0]

    for i in range(n):
        dp[i][i] = True
        result = S[i]
        max_len = 1

    for length in range(2, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1

            if length == 2:
                dp[i][j] = (S[i] == S[j])
            else:
                dp[i][j] = (S[i] == S[j]) and dp[i + 1][j - 1]

            if dp[i][j]:
                if length > max_len:
                    max_len = length
                    result = S[i:j + 1]

    print(result)  # Print the longest palindromic substring to stdout

longest_palindromic_substring()

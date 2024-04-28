def longest_palindromic_substring():
    S = input()
    n = len(S)
    k = 0

    dp = [[False] * n for _ in range(n)]

    for i in range(n):
        dp[i][i] = True
        k = max(k, 1)

    for length in range(2, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            if S[i] == S[j]:
                if length == 2 or dp[i + 1][j - 1]:
                    dp[i][j] = True
                    k = max(k, length)

    longest_palindromic_substring = ""
    for i in range(n):
        for j in range(i, n):
            if dp[i][j]:
                if len(longest_palindromic_substring) < j - i + 1:
                    longest_palindromic_substring = S[i:j+1]

    print(longest_palindromic_substring)

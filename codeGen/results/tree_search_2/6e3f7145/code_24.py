def longest_palindromic_substring(S):
    n = len(S)
    dp = [[False] * n for _ in range(n)]

    max_len = 0
    start = 0

    for i in range(n):
        for j in range(i, n):
            if S[i] == S[j]:
                if i == j or dp[i+1][j-1]:
                    dp[i][j] = True
                    if j - i + 1 > max_len:
                        max_len = j - i + 1
                        start = i
    return S[start:start+max_len]

S = input()
print(longest_palindromic_substring(S))

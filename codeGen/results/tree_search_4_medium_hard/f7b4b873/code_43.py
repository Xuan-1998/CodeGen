def partition_palindromes(s):
    n = len(s)
    dp = [[[] for _ in range(n+1)] for _ in range(n+1)]

    for i in range(n+1):
        dp[i][i] = [s[:i]]

    for length in range(2, n+1):
        for i in range(n-length+1):
            j = i + length
            if s[i] == s[j]:
                if length == 2:
                    dp[i][j] = [[s[i:j+1]]]
                else:
                    dp[i][j] = [p + [s[i:j+1]] for p in dp[i+1][j-1]]

    return [p for sublist in dp[0][n-1] for p in sublist]

s = input()
print(partition_palindromes(s))

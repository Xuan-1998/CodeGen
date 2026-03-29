def partition_palindrome(s):
    n = len(s)
    dp = [[[] for _ in range(n+1)] for _ in range(n+1)]

    for i in range(1, n+1):
        if s[i-1] == s[i-1][::-1]:
            dp[i][i].append([s[:i]])

    for length in range(2, n+1):
        for i in range(n-length+1):
            j = i + length - 1
            for k in range(i, j+1):
                if s[k] == s[k][::-1]:
                    for p in dp[i][k]:
                        for q in dp[k+1][j]:
                            dp[i][j].append(p + [s[k+1:j+1]] + q)

    return dp[0][n-1]

input_string = input()
print(partition_palindrome(input_string))

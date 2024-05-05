def partition_palindromes(s):
    n = len(s)
    dp = [[[] for _ in range(n+1)] for _ in range(n+1)]

    for i in range(n+1):
        dp[i][i].append([s[i]])

    for length in range(2, n+1):
        for i in range(n-length+1):
            j = i + length
            for k in range(i, j):
                if s[k] == s[j-1]:
                    for partition1 in dp[i][k]:
                        for partition2 in dp[k+1][j-1]:
                            dp[i][j].append([*partition1, *reversed(partition2)])

    return [list(map(''.join, partitions)) for partitions in dp[0][n-1]]

s = input()
print(partition_palindromes(s))

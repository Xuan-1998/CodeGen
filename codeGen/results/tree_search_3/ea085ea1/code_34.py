from collections import defaultdict

def solve(str1, str2):
    n, m = len(str1), len(str2)
    memo = [[0] * (m + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if str1[i - 1] == str2[j - 1]:
                memo[i][j] = memo[i - 1][j - 1] + 1
            else:
                memo[i][j] = max(memo[i - 1][j], memo[i][j - 1])

    res = 0
    i, j = n, m
    while i > 0 and j > 0:
        if str1[i - 1] == str2[j - 1]:
            res += 1
            i -= 1
            j -= 1
        elif memo[i - 1][j] > memo[i][j - 1]:
            i -= 1
        else:
            j -= 1

    return res


# Read input from stdin
str1 = input()
str2 = input()

# Print the answer to stdout
print(solve(str1, str2))

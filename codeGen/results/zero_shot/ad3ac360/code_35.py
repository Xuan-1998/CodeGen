import sys

def min_cuts(s):
    n = len(s)
    dp = [[False] * (n + 1) for _ in range(n + 1)]

    for i in range(n + 1):
        dp[i][i] = True

    for i in range(n - 1, -1, -1):
        for j in range(i + 1, n + 1):
            if s[i] == s[j - 1] and (j - i < 3 or dp[i + 1][j - 1]):
                dp[i][j] = True

    cuts = 0
    for i in range(n):
        if not dp[0][i]:
            cuts += 1

    return cuts

# Read input from stdin
n = int(input())
s = input().strip()

# Call the function and print the result to stdout
print(min_cuts(s))

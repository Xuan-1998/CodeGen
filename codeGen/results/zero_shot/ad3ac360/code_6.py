import sys

def min_cuts(s):
    n = len(s)
    dp = [[False] * (n + 1) for _ in range(n + 1)]

    # Fill in the table
    for i in range(n + 1):
        for j in range(i, n + 1):
            if i == j:
                dp[i][j] = True
            elif j - i == 1:
                dp[i][j] = s[i] == s[j]
            else:
                dp[i][j] = (s[i] == s[j] and dp[i + 1][j - 1])

    # Calculate the minimum cuts
    cut_count = 0
    for i in range(n):
        if not dp[0][i]:
            cut_count += 1

    return cut_count

# Read input from stdin
s = sys.stdin.readline().strip()

# Print the answer to stdout
print(min_cuts(s))

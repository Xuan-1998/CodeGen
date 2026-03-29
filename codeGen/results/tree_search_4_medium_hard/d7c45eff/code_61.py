import sys

def solve(n, k):
    # Initialize the dynamic programming table
    dp = [[[] for _ in range(k + 1)] for _ in range(n + 1)]

    # Fill in the dynamic programming table using a bottom-up approach
    for i in range(1, n + 1):
        if i <= k:
            dp[i][i] = [s[:i]]
        else:
            dp[i][k].append(s[:k])
            for j in range(i - 1, k - 1, -1):
                for delete in (True, False):
                    if delete and j < i - 1:
                        dp[i][k].extend(dp[j + 1][k] + [s[j]])
                    elif not delete and j >= i - 1:
                        dp[i][k].extend([s[:i]] + dp[k - i][k])
            dp[i][k].sort()

    # Return the lexicographically smallest string of length k
    return min(dp[n][k], key=len)

# Read input from standard input
n, k = map(int, sys.stdin.readline().split())
s = sys.stdin.readline().strip()

# Print the output to standard output
print(solve(n, k))

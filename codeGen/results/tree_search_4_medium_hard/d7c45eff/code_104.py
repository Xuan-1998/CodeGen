import sys
from collections import deque

def find_smallest_string(n, k):
    dp = [[[] for _ in range(k+1)] for _ in range(n+1)]

    # Initialize base case
    for i in range(n+1):
        if i == 0:
            continue
        if k == 0:
            return ""
        dp[i][0] = [s[:i]]

    for i in range(1, n+1):
        for j in range(min(i, k)+1):
            # If the desired length is less than or equal to the current string length,
            # the optimal solution is the substring of the current string
            if j <= i:
                dp[i][j] = [s[:i]]
            else:
                # Otherwise, consider deleting the last character and duplicating the string
                if i > 0:
                    delete_last_char = min(dp[i-1][j-1], dp[i][j-1])
                    duplicate_string = dp[i][j-1]
                    dp[i][j] = min(delete_last_char + [s[i-1]], duplicate_string)
                else:
                    # For the first string, the optimal solution is the original string
                    dp[i][j] = [s[:i]]

    return min(dp[n][k], key=lambda x: (x, len(x)))

# Read input from stdin
n, k = map(int, sys.stdin.readline().split())
s = sys.stdin.readline().strip()

# Print output to stdout
print(find_smallest_string(n, k))

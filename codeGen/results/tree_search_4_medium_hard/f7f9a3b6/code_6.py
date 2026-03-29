import sys

# Read input
n = int(input())
s = input().strip()
a = [int(x) for x in input().split()]

dp = [[0] * 27 for _ in range(n + 1)]
dp[0][26] = 1  # Base case: empty string has one way to split (no splits)

for i in range(1, n + 1):
    c = s[i - 1]
    for j in range(min(i, 26), 0, -1):
        if i <= a[ord(c) - ord('a')]:  # Check condition
            dp[i][j] += dp[i - 1][min(j, ord(c) - ord('a'))]
        else:
            break

# Print output
print(sum(dp[n]) % (10**9 + 7))  # Number of ways to split the message
print(max(i for i in range(27) if dp[n][i]))  # Length of longest substring over all ways
print(min(i for i in range(n + 1) if dp[i][26]))  # Minimum number of substrings over all ways

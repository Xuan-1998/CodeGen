# Read input from stdin
n = int(input())
s = input()
a = [int(x) for x in input().split()]

# Initialize variables for dynamic programming
dp = [[0] * (n + 1) for _ in range(n + 1)]
ans = max_len = min_substrings = 0

# Fill up the dp array using a loop that considers all possible cuts at each position
for i in range(1, n + 1):
    for j in range(i, n + 1):
        if s[i - 1:j].isalpha() and j - i + 1 <= max(a):
            for k in range(i - 1, j):
                dp[i][j] += dp[i - 1][k] * a[ord(s[k]) - ord('a')]
        else:
            dp[i][j] = dp[i - 1][j - 1]

# Calculate the number of ways to split the message
for i in range(1, n + 1):
    ans += dp[0][i]

# Print the results modulo 10^9 + 7
print(ans % (10**9 + 7))

# Find the length of the longest substring over all the ways
max_len = max(max_len for i in range(1, n + 1) for j in range(i, n + 1) if dp[i][j])

# Find the minimum number of substrings over all the ways
min_substrings = min(min_substrings for i in range(1, n + 1) for j in range(i, n + 1) if dp[i][j])

print(max_len)
print(min_substrings)

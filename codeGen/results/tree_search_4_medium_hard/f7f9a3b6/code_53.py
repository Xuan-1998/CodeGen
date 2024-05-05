# Read input
n = int(input())
s = input()
a = [int(x) for x in input().split()]

# Initialize dp table
dp = [[0] * (sum(a) + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    for j in range(min(i, sum(a)), -1, -1):
        if s[i-1] == s[0]:
            dp[i][j] = max(dp[i-1][k] + 1 for k in range(j))
        else:
            dp[i][j] = dp[i-1][j]

# Calculate number of ways to split the message
num_ways = sum((dp[n][j] - j) if j < n else 0 for j in range(sum(a), -1, -1)) % (10**9 + 7)

# Calculate length of longest substring over all the ways
longest_substring = max(dp[n])

# Calculate minimum number of substrings over all the ways
min_substrs = min((dp[i][j] for i in range(n) for j in range(sum(a), -1, -1))) + 1

print(num_ways)
print(longest_substring)
print(min_substrs)

import sys

# Read input
n = int(input())
s = input()
a = list(map(int, input().split()))

# Initialize dp array
dp = [[[0] * (26 + 1) for _ in range(n + 1)] for _ in range(2)]

for i in range(2):
    for j in range(26 + 1):
        dp[i][j][0] = 1

for i in range(n + 1):
    for j in range(1, min(i, 26) + 1):
        if s[i-1].ord() - ord('a') < j:
            dp[1][j][i] = dp[1][j][i-1]
        else:
            for k in range(j):
                if i > 0 and s[i-1].ord() - ord('a') == k:
                    continue
                if i-k-1 > 0 and a[ord(s[k].lower()) - ord('a')] < j-k+1:
                    dp[1][j][i] = (dp[1][j][i] + dp[1][k][i-k]) % (10**9 + 7)
                else:
                    dp[1][j][i] = (dp[1][j][i] + dp[0][k][i-k]) % (10**9 + 7)

# Compute the number of ways to split the message
ans1 = dp[1][26][n]

# Compute the length of the longest substring over all the ways
max_len = max(len(s[i:j+1]) for i in range(n) for j in range(i, n))

# Compute the minimum number of substrings over all the ways
min_substrings = sum(1 for i in range(n) if len(set(s[i-k:i+k+1])) <= a[ord(s[i].lower()) - ord('a')] for k in range(min(max_len, 26)))

print(ans1)
print(max_len)
print(min_substrings)

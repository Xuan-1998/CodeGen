import sys

# Read input from standard input
s = input()

dp = [[False for _ in range(2)] for _ in range(len(s) + 1)]

for i in range(len(s) + 1):
    dp[i][0] = True

for i in range(len(s)):
    if s[i] == 'A':
        dp[i+1][0] = dp[i][0]
        dp[i+1][1] = dp[i][1] or dp[i][0]
    elif s[i] == 'B':
        dp[i+1][0] = dp[i][0] and dp[i][1]
        dp[i+1][1] = dp[i][1]
    else:
        dp[i+1][0] = dp[i][0]
        dp[i+1][1] = dp[i][1]

found_ab_or_ba = False
for i in range(len(s) - 2):
    if (dp[i][1] and s[i:i+2] == 'AB') or (dp[i][0] and s[i:i+2] == 'BA'):
        found_ab_or_ba = True
        break

# Print the answer to standard output
print("YES" if found_ab_or_ba else "NO")

import sys

# Read input from stdin
s = sys.stdin.readline().strip()

dp = [[False for _ in range(2)] for _ in range(len(s) + 1)]

for i in range(1, len(s) + 1):
    if s[i - 1] == 'A' and dp[i - 1][0]:
        dp[i][0] = True
    elif s[i - 1] == 'B' and dp[i - 1][1]:
        dp[i][1] = True

# Check if either 'AB' or 'BA' appears in the string
if dp[-1][0] or dp[-1][1]:
    print("YES")
else:
    print("NO")

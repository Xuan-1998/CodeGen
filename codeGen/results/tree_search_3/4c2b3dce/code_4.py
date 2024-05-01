import sys

# Read input from stdin
s = input()

dp = [[False, False] for _ in range(len(s) + 1)]

for i in range(1, len(s) + 1):
    if s[i - 1] == 'A':
        dp[i][0] = True
    elif s[i - 1] == 'B':
        dp[i][1] = True

found = False
for i in range(len(s)):
    for j in range(i, len(s)):
        if (dp[j + 1][1] and dp[i][0]) or (dp[j + 1][0] and dp[i][1]):
            print("YES")
            sys.exit(0)

print("NO")

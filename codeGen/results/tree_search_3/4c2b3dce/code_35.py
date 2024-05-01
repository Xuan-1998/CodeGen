===BEGIN CODE===
s = input()
dp = [[False for _ in range(len(s) + 1)] for _ in range(2)]

# Initialize base cases
dp[0][0] = True
for i in range(len(s)):
    dp[0][i] = False
    if s[i] == 'A':
        dp[1][i + 1] = True

for i in range(1, len(s) + 1):
    for j in range(i):
        if (s[j] == 'A' and s[i - 1] == 'B') or (s[j] == 'B' and s[i - 1] == 'A'):
            dp[0][i] = True
        if (s[j] == 'B' and s[i - 1] == 'A') or (s[j] == 'A' and s[i - 1] == 'B'):
            dp[1][i] = True

# Check the last state
if (dp[0][-1] and dp[1][-2]) or (dp[1][-1] and dp[0][-2]):
    print("YES")
else:
    print("NO")

===END CODE===

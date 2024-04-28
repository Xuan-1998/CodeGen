import sys
s = input().strip()
dp = [[0] * (len(s) + 1) for _ in range(len(s) + 1)]

for i in range(1, len(s)):
    if s[i-1:i+1] == "AB":
        for j in range(i+2, len(s)+1):
            if s[j-3:j].endswith("BA"):
                dp[i][j] = 1
    else:
        continue

for i in range(len(s)):
    if s[i:i+2] == "AB":
        for j in range(i+2, len(s)+1):
            if s[j-2:].startswith("BA"):
                dp[i][j] = 1

print("YES" if any(all(dp[i][j]) for i in range(len(s))) else "NO")

import sys

def contains(sub, str):
    return str.find(sub) != -1

dp = [[False for _ in range(2)] for _ in range(len(input()) + 1)]

for i in range(1, len(input()) + 1):
    if input()[i-1] == 'A':
        dp[i][0] = dp[i-1][0]
        dp[i][1] = dp[i-1][0] or (dp[i-1][1] and not any(c == 'B' for c in input()[:i]))
    elif input()[i-1] == 'B':
        dp[i][0] = dp[i-1][1]
        dp[i][1] = dp[i-1][1] or (dp[i-1][0] and not any(c == 'A' for c in input()[:i]))
    else:
        dp[i][0] = dp[i-1][0]
        dp[i][1] = dp[i-1][1]

print("YES" if any(dp[-1]) else "NO")

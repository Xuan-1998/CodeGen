from sys import stdin

def solve():
    s = stdin.readline().strip()
    for i in range(len(s)):
        for j in range(2):
            dp[i][j] = False
            if i > 0:
                if (s[i-1] == 'A' and j == 0) or (s[i-1] == 'B' and j == 1):
                    if j == 0:
                        dp[i][j] = not dp[i-1][1]
                else:
                    dp[i][0], dp[i][1] = False, False
    for i in range(len(s)):
        if dp[i][0] and not dp[i][1]:
            return "YES"
    return "NO"

dp = [[False for _ in range(2)] for _ in range(100001)]
print(solve())

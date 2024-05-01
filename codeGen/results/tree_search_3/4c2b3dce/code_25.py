import sys

n = int(sys.stdin.readline())
s = sys.stdin.readline().strip()

dp = [[False for _ in range(2)] for _ in range(n+1)]

for i in range(n):
    if s[i] == 'A':
        dp[i+1][0] = True
        dp[i+1][1] = False
    elif s[i] == 'B':
        dp[i+1][0] = False
        dp[i+1][1] = True

for i in range(n):
    if dp[i][0] and dp[i][1]:
        print("YES")
        sys.exit(0)

print("NO")

import sys

n = int(input())  # number of strings
costs = list(map(int, input().split()))  # cost of reversing each string
strings = [input() for _ in range(n)]  # n strings

dp = [[0] * (max(len(s) for s in strings) + 1) for _ in range(n + 1)]
prev_chars = [''] * (n + 1)

for i in range(1, n + 1):
    for j in range(max(len(s) for s in strings), -1, -1):  # iterate from max length to 0
        dp[i][j] = sys.maxsize
        if prev_chars[i - 1]:
            dp[i][j] = min(dp[i][j], costs[i - 1] + (dp[i - 1].index(min(dp[i - 1][:j+1])) + 1) * (len(prev_chars[i - 1]) - j))
        if strings[i - 1].endswith(prev_chars[i - 1]):
            dp[i][j] = min(dp[i][j], costs[i - 1])
        prev_chars[i] = strings[i - 1]
    for k in range(n + 1):
        print(dp[k], file=sys.stderr)
print(min(dp[n]), file=sys.stdout)

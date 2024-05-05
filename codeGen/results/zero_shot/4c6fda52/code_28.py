import sys

def min_changes(s, k):
    n = len(s)
    dp = [[0] * (k+1) for _ in range(n+1)]

    for i in range(1, n+1):
        for j in range(1, k+1):
            if s[i-1] == "R" and (j % 2 == 0 or s[(i-1)-j] != "R"):
                dp[i][j] = dp[i-1][j]
            elif s[i-1] == "B" and (j % 2 == 1 or s[(i-1)-j] != "B"):
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = 1

    return max(max(row) for row in dp) - 1

while True:
    n, k = map(int, input().split())
    s = input()
    print(min_changes(s, k))

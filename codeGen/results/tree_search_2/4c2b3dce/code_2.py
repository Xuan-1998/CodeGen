import sys

def solution():
    s = input().strip()
    n = len(s)

    # Initialize the 2D table with False values
    dp = [[False] * (n + 1) for _ in range(2)]

    for i in range(n):
        if s[i] == 'A':
            dp[0][i + 1] = True
        elif s[i] == 'B' and dp[0][i]:
            dp[1][i + 1] = True

    # Check the last state (n)
    if dp[0][n] and dp[1][n]:
        print("YES")
    else:
        print("NO")

solution()

import sys

def solve():
    s = input()
    n = len(s)

    # Initialize dp and seen arrays
    dp = [False] * (n - 1)
    seen = [[False] * (n - 1) for _ in range(n)]

    # Fill up the dp array
    for i in range(1, n - 1):
        if s[i] == 'A' and s[i+1] == 'B':
            dp[i] = True
        else:
            dp[i] = dp[i-1]

    # Fill up the seen array
    for i in range(n - 2):
        for j in range(i + 1):
            if s[j] == 'A' and s[j+1] == 'B':
                seen[i][j] = True
            else:
                seen[i][j] = seen[i-1][j]

    # Check if the string contains "AB" and "BA"
    ans = False
    for i in range(n - 2):
        for j in range(i + 1):
            if dp[j] and seen[n-j-1][i-j-1]:
                ans = True
                break

    print("YES" if ans else "NO")

solve()

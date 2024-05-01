import sys

def solve():
    s = input().strip()
    n = len(s)

    dp = [[False, False] for _ in range(n+1)]

    dp[0][0] = True
    dp[0][1] = True

    for i in range(1, n+1):
        if i >= 2 and s[i-2:i] == 'AB':
            dp[i][0] = True
        if i >= 2 and s[i-2:i] == 'BA':
            dp[i][1] = True

        if dp[i-1][0]:
            dp[i][0] = (dp[i-1][0] or s[i-1] == 'B')
        if dp[i-1][1]:
            dp[i][1] = (dp[i-1][1] or s[i-1] == 'A')

    print("YES" if dp[n][0] and dp[n][1] else "NO")

if __name__ == "__main__":
    solve()

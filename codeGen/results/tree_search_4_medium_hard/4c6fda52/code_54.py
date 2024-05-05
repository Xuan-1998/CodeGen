import sys

def solve():
    n, k = map(int, input().split())
    s = input()

    dp = [[False] * (k+1) for _ in range(n+1)]

    for i in range(k):
        dp[0][i] = False

    dp[0][0] = True
    for i in range(1, n+1):
        for j in range(min(i+1, k)+1):
            if (j == 0 or s[i-1] == s[(i-1)%3]):
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = dp[i-1][j] or dp[i-1][j-1]

    changes = n
    for i in range(1, k+1):
        if s[k-i] != s[(k-i)%3]:
            changes = min(changes, i)
        else:
            break

    print(min(changes + (n-k), 2))

if __name__ == "__main__":
    solve()

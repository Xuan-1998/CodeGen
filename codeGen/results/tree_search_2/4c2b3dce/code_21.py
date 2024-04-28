import sys

def solve(s):
    n = len(s)
    dp = [[0] * (n + 1) for _ in range(n + 1)]

    for i in range(n - 2):
        if s[i:i+3] == 'ABA':
            for j in range(i + 3, n + 1):
                dp[i][j] = 1

    for i in range(n - 2):
        if s[i:i+3] == 'BAB':
            for j in range(i + 3, n + 1):
                dp[j][i] = 1

    res = "NO"
    for i in range(1, n):
        if dp[0][i]:
            res = "YES"
            break

    print(res)

if __name__ == "__main__":
    s = input().strip()
    solve(s)

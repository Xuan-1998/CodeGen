import sys

def solve(n):
    p = list(map(int, input().split()))
    dp = [[False] * (n + 1) for _ in range(n + 1)]

    for i in range(n + 1):
        for j in range(i + 1):
            if p[2 * i] <= p[2 * j]:
                dp[i][j] = True
            else:
                break

    for i in range(n, -1, -1):
        for j in range(n, -1, -1):
            if not dp[i][j]:
                return "NO"
    return "YES"

t = int(input())
for _ in range(t):
    n = int(input())
    print(solve(n))

import sys
input = sys.stdin.readline

def solve():
    n, m, k = map(int, input().split())
    table = [list(map(int, input().split())) for _ in range(n)]
    dp = [[False] * m for _ in range(n)]

    for i in range(1, n):
        for j in range(m):
            if all(table[i-1][j] <= table[i][j] for _ in range(k)):
                dp[i][j] = True

    return "Yes" if any(all(dp[i][j] for j in range(m)) for i in range(n)) else "No"

print(solve())

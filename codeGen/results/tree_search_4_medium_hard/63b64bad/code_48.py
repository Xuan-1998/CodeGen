import sys
from collections import defaultdict

def solve():
    n = int(input())
    a = list(map(int, input().split()))
    
    dp = [[0] * (n + 1) for _ in range(n + 1)]
    visited = [[False] * (n + 1) for _ in range(n + 1)]

    for i in range(2, n + 1):
        for j in range(1, i):
            if j <= 0 or j > n:
                dp[i][j] = -1
            else:
                x, y = j, 0
                while True:
                    x += a[x]
                    y += a[x]
                    x -= a[x]
                    if (x, y) in visited:
                        break
                    visited[x][y] = True
                dp[i][j] = y

    for i in range(2, n + 1):
        print(dp[i][i - 1])

if __name__ == "__main__":
    solve()

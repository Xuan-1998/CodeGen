import sys
input = sys.stdin.readline

def solve():
    n = int(input())
    grid = []
    for _ in range(n):
        row = list(map(int, input().split()))
        grid.append(row)

    dp = [[0] * n for _ in range(n)]

    min_sum = float('inf')
    for k in range(1, n+1):
        for i in range(k-1, -1, -1):
            if k == 1:
                dp[i][k-1] = grid[i][k-1]
            else:
                dp[i][k-1] = min(dp[j][k-2] + grid[i][k-1] for j in range(i, n))
            if k == n:
                min_sum = min(min_sum, dp[i][k-1])
            else:
                min_sum = min(min_sum, dp[i][k-1])

    print(min_sum)

solve()

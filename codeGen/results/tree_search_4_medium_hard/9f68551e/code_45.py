import sys

def solve():
    n = int(sys.stdin.readline())
    monsters = [int(x) for x in sys.stdin.readline().split()]
    healths = [int(x) for x in sys.stdin.readline().split()]

    dp = [[0] * (n + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        dp[i][0] = monsters[i - 1]
    for j in range(1, n + 1):
        dp[0][j] = float('inf')
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if j >= i:
                dp[i][j] = min(dp[i - 1][k] + (monsters[i - 1] - healths[i - 1]) // (i - k) for k in range(i))
    return dp[-1][-1]

print(solve())

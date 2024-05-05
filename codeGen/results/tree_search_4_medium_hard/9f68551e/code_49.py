import sys

def solve():
    n = int(sys.stdin.readline())
    monsters = list(map(int, sys.stdin.readline().split()))
    healths = list(map(int, sys.stdin.readline().split()))

    dp = [[0] * (max(monsters) + 1) for _ in range(n+1)]

    for i in range(1, n+1):
        k = monsters[i-1]
        h = healths[i-1]

        if i == 1:
            dp[0][k] = 0
        else:
            dp[i][k] = max(h, dp[i-1][k-1]+1)

    print(dp[n][max(monsters)])

if __name__ == "__main__":
    solve()

import sys

def min_mana_required(input):
    n = int(input().strip())
    monsters = []
    for _ in range(n):
        k, h = map(int, input().strip().split())
        monsters.append((k, h))

    dp = [[float('inf')] * (n + 1) for _ in range(n + 1)]
    dp[0][0] = 0

    for i, (k, h) in enumerate(monsters):
        for j in range(min(i + 1, k), -1, -1):
            if j == 0:
                dp[i + 1][j] = min(dp[i + 1][j], dp[i][j] + h)
            else:
                for x in range(j - 1, -1, -1):
                    if dp[x][j - 1] != float('inf') and dp[i][x] + h <= k:
                        dp[i + 1][j] = min(dp[i + 1][j], dp[x][j - 1] + h)

    return dp[-1][-1]

t = int(input().strip())
for _ in range(t):
    print(min_mana_required(sys.stdin.readline()))

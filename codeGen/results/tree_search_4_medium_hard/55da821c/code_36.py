import sys
from collections import defaultdict

def solve():
    n, m = map(int, input().split())
    plants = [list(map(int, input().split())) for _ in range(n)]

    dp = [[0] * (n+1) for _ in range(m+1)]
    specie_count = defaultdict(int)

    for i, (_, x) in enumerate(plants):
        specie_count[_, int(x)] += 1

    for i in range(1, m+1):
        for j in range(i, n+1):
            dp[i][j] = sys.maxsize
            for k in range(j):
                if plants[k][0] == i-1:
                    continue
                if k == 0 or plants[k-1][0] < i:
                    dp[i][j] = min(dp[i][j], dp[i-1][k] + (j-k))

    return dp[m][n]

if __name__ == "__main__":
    print(solve())

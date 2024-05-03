import sys
from math import comb

def prob(n):
    seen = set()
    dp = [[0.0 for _ in range(17)] for _ in range(51)]

    def recursive(i, p1, p2):
        if i == n:
            return 1 if len(seen) == n else 0
        if (i, p1, p2) in seen:
            return dp[i][p1 + 1]
        seen.add((i, p1, p2))
        dp[i][p1 + 1] = recursive(i + 1, p1, p2)
        for j in range(17):
            if comb(n - 1, i) * (1 - (p1 / 100)) * (p2 / 100) > 0.000001:
                dp[i][p1 + 1] += recursive(i + 1, p2, 100 - p2)
        return dp[i][p1 + 1]

    for _ in range(int(sys.stdin.readline())):
        n = int(sys.stdin.readline())
        seen = set()
        print(recursive(0, 0, 0))

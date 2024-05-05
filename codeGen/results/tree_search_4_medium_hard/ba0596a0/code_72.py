===BEGIN CODE===
from sys import stdin

def can_cross_stones(stones):
    n = len(stones)
    dp = [False] * (n + 1)

    dp[0] = True
    for i in range(1, n + 1):
        if dp[i - 1]:
            for j in range(i - 1, max(0, i - k) - 1, -1):
                if stones[j] == i:
                    dp[i] = True
                    break

    return dp[-1]

k = int(stdin.readline())
stones = list(map(int, stdin.readline().split()))
print(can_cross_stones(stones))
===END CODE===

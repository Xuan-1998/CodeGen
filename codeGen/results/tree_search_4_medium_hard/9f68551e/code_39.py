code = """
import heapq
def min_mana(n, times, healths):
    dp = [[float('inf')] * (n + 1) for _ in range(n + 1)]
    dp[0][0] = 0

    for i in range(1, n + 1):
        for j in range(i):
            heapq.heapify([(k - j, h, k, j) for k, h in zip(times[:i], healths[:i])])
            while heap:
                time, damage, _, monster = heapq.heappop(heap)
                if damage >= healths[monster]:
                    dp[i][j] = min(dp[i][j], dp[j][monster] + (time - j))
    return dp[n][n-1]
"""

print(min_mana(*map(int, input().split())))

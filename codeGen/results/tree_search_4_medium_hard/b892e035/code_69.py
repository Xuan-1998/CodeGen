code
from collections import defaultdict
from functools import lru_cache

def solve():
    T = int(input())
    for _ in range(T):
        n = int(input())
        dp = [[[0.0] * (2 ** 16) for _ in range(51)] for _ in range(n + 1)]
        counts = defaultdict(int)
        for _ in range(n):
            p, a, b = map(float, input().split())
            counts[a] += 1
            counts[b] += 1

        @lru_cache(maxsize=None)
        def dfs(i, count1, count2):
            if i == n:
                return 1.0 if len(counts) == n else 0.0

            p_correct = (a * b) / (count1 * count2)
            p_incorrect = 1 - p_correct
            max_prob = 0.0
            for j in range(min(count1, count2)):
                p1 = (p_correct if a == j else p_incorrect)
                p0 = (p_correct if b == j else p_incorrect)
                max_prob = max(max_prob, dp[i - 1][count1 - j - 1][count2 - j - 1] * p1 + dp[i - 1][j][count2 - j - 1] * p0)

            return max_prob

        print(dfs(n, counts[a], counts[b]))

solve()

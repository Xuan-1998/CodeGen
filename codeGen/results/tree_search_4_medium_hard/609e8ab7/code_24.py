from functools import lru_cache

def adjust_tree_values():
    n = int(input())
    parent = list(map(int, input().split()))
    ranges = [list(map(int, input().split())) for _ in range(n)]

    @lru_cache(None)
    def dp(i, j):
        if i == 0:
            return 0
        res = float('inf')
        for k in range(j + 1, min(ranges[i][1], ranges[parent[i]][1]) + 1):
            res = min(res, dp(parent[i], k) + abs(k - j))
        return res

    print(sum(dp(i, j) for i, (j, _) in enumerate(ranges)))

adjust_tree_values()

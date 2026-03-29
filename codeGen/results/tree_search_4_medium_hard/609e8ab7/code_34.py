===BEGIN SOLUTION===
from collections import defaultdict
import heapq

def solve(n, p, l, r):
    memo = defaultdict(int)
    ans = [0] * (n + 1)

    def dfs(i):
        if i > 1:
            return memo[i]
        v1, v2 = max(min(l), min(r)), max(max(l), max(r))
        for j in range(1, i // 2 + 1):
            heapq.heappush(ans, (v1 - l[j], r[j] - v2, j, i // j))
        res = len(ans)
        while ans:
            v1, v2, j, k = heapq.heappop(ans)
            if l[k] <= v1 and v2 <= r[k]:
                continue
            res += 1
            if k > 1:
                res -= dfs(k)
        return res

    for i in range(2, n + 1):
        memo[i] = dfs(i)

    print(sum(ans[1:]))

n = int(input())
p = list(map(int, input().split()))
l = list(map(lambda x: list(map(int, x.split())), [input() for _ in range(n)]))
r = list(map(lambda x: list(map(int, x.split())), [input() for _ in range(n)]))
solve(n, p, l, r)

import sys
from collections import defaultdict

def adjust_values(root):
    n = int(input())
    p = list(map(int, input().split()))
    l, r = [], []
    for i in range(1, n+1):
        l_i, r_i = map(int, input().split())
        l.append((l_i, 0))
        r.append((r_i, 0))

    memo = defaultdict(lambda: [float('inf'), 0])
    def dfs(i, j):
        if (i, j) in memo:
            return memo[(i, j)]
        if l[i-1][0] <= j <= r[i-1][0]:
            return 0, 0
        delta = max(l[i-1][0], j) - min(r[i-1][0], j)
        if i == root:
            return delta, 1
        left, op_left = dfs(p[i], l[i-1][0])
        right, op_right = dfs(i, r[i-1][0])
        return min(left + right + delta, op_left), op_left + (op_right > 0)

    res = []
    for i in range(1, n+1):
        j = min(r[i-1][0], l[p[i]][0]) if p[i] else r[i-1][0]
        left, op_left = dfs(p[i], j)
        right, op_right = dfs(i, j)
        res.append(min(left + right, op_left) + 1)

    return '\n'.join(map(str, res))

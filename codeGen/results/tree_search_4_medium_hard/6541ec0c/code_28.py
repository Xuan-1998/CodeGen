===BEGIN CODE===
import sys
from collections import defaultdict

def solve():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    graph = defaultdict(list)
    for _ in range(n-1):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)

    dp = {}

    def dfs(i, mi, mx):
        if (i, mi, mx) in dp:
            return dp[(i, mi, mx)]
        res = True
        for j in graph[i]:
            xor_mi = a[i] ^ a[j]
            if xor_mi < mi or xor_mi > mx:
                res &= dfs(j, min(mi, xor_mi), max(mx, xor_mi))
            else:
                res &= dfs(j, xor_mi, xor_mi)
        return not res

    root = 1
    for i in range(2, n+1):
        if a[i] < a[root]:
            root = i

    res = dfs(root, a[root], a[root])
    print("YES" if res else "NO")

solve()

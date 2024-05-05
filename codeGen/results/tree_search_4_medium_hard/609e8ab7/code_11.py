import sys
from collections import defaultdict

def dfs(node, parent_value, memo):
    if node not in memo:
        l, r = map(int, sys.stdin.readline().split())
        diff = min(l, 0) + max(r, 0)
        memo[node] = diff
        children = []
        for child in range(2*node+1, 2*node+2):
            if child <= n:
                children.append(child)
        for child in children:
            parent_value[child] = min(parent_value.get(child, r), l) + diff
            dfs(child, parent_value, memo)

n = int(sys.stdin.readline())
parent = defaultdict(int)
for _ in range(n-1):
    a, b = map(int, sys.stdin.readline().split())
    parent[b] = a

memo = {}
for node in range(2, n+1):
    if node not in parent:
        l, r = map(int, sys.stdin.readline().split())
        diff = min(l, 0) + max(r, 0)
        memo[node] = diff
        dfs(node, dict(), memo)

print(sum(memo.values()))

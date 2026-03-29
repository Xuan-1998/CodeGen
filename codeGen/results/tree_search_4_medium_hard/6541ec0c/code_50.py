import sys
from collections import defaultdict

def solve():
    n, k = map(int, input().split())
    tree = [[] for _ in range(n)]
    xor_values = list(map(int, input().split()))
    for i in range(n - 1):
        u, v = map(int, input().split())
        tree[u].append(v)
        tree[v].append(u)

    dp = [[[0] * (10**9 + 1) for _ in range(k + 1)] for _ in range(n)]

    def dfs(node, parent, xor_val):
        children = 0
        for child in tree[node]:
            if child != parent:
                children += 1
                dfs(child, node, xor_val ^ xor_values[child - 1])
        dp[node][children + 1][xor_val] = 1

    dfs(0, -1, 0)

    for i in range(n):
        for j in range(k, -1, -1):
            if dp[i][j]:
                print("YES")
                return
    print("NO")

if __name__ == "__main__":
    solve()

from collections import defaultdict

def solve():
    T = int(input())
    for _ in range(T):
        n = int(input())
        tree = defaultdict(int)
        ranges = {}
        parent_list = list(map(int, input().split()))
        for i in range(1, n):
            l, r = map(int, input().split())
            ranges[i] = (l, r)
            if parent_list[i-1] == 0:
                tree[0] = (l, r)
            else:
                tree[parent_list[i-1]] = (min(tree[parent_list[i-1]][0], l), max(tree[parent_list[i-1]][1], r))
        dp = {node: (ranges[node][0], ranges[node][1]) for node in range(1, n)}
        for node in dfs_order:
            dfs(node)
        min_ops = 0
        for node in tree:
            if dp[node][0] > tree[node][0]:
                min_ops += dp[node][0] - tree[node][0]
            elif dp[node][1] < tree[node][1]:
                min_ops += tree[node][1] - dp[node][1]
        print(min_ops)

# Start of DFS code
dfs_order = []
def dfs(node):
    global dfs_order
    if node:
        dfs(parent_list.index(node))
        dfs_order.append(node)

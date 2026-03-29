import sys

def solve():
    n = int(sys.stdin.readline().strip())
    parent = list(map(int, sys.stdin.readline().split()))
    ranges = []
    for _ in range(n):
        l, r = map(int, sys.stdin.readline().split())
        ranges.append((l, r))

    # Create a dictionary to store the tree structure
    tree = {i: [] for i in range(1, n+1)}
    for i in range(n-1):
        parent[i] -= 1

    # Fill up the tree structure
    for i in range(n-1):
        tree[parent[i]].append(i+1)

    # Initialize the DP table
    dp = [[[0, []] for _ in range(2*10**9 + 1)] for _ in range(n+1)]

    def dfs(node, value, ops):
        if ops[0]:
            return [value - ops[0], []]
        return [value, []]

        # Calculate the maximum value that needs to be subtracted from all nodes in subtree rooted at node i
        max_val = value - (ranges[node-1][1] - ranges[node-1][0])
        min_ops = 0

        if tree[node]:
            for child in tree[node]:
                res, ops_child = dfs(child, value + len(ranges), ops)
                if res[0] > max_val:
                    max_val = res[0]
                    min_ops += 1
                else:
                    min_ops += res[1].count(ops_child[-1]) if ops_child else 0

        return [max_val, list(set([*ops, *res[1]])))

    root_node = 1
    result = dfs(root_node, 0, [])
    print(result[0])

solve()

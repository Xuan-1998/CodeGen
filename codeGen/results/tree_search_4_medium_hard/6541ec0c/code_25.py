import sys
from collections import defaultdict

def solve():
    n, k = map(int, input().split())
    values = list(map(int, input().split()))
    edges = []
    for _ in range(n-1):
        u, v = map(int, input().split())
        edges.append((u, v))

    dp = defaultdict(lambda: [[0, 0], [float('inf'), float('inf')]])

    def dfs(node, min_xor, max_xor, nodes_left):
        if not nodes_left:
            return

        for neighbor in edges[node]:
            if (min_xor, max_xor) != dp[neighbor][0]:
                continue
            xor_value = values[neighbor]
            new_min_xor = xor_value ^ min_xor
            new_max_xor = xor_value ^ max_xor
            new_nodes_left = nodes_left - 1

            if (new_min_xor, new_max_xor) not in dp[neighbor][1]:
                dp[neighbor].append([new_min_xor, new_max_xor])
                dfs(neighbor, new_min_xor, new_max_xor, new_nodes_left)

    for node in range(n):
        dfs(node, values[node], values[node], n-1)

    result = "YES" if k == 0 else "NO"
    print(result)

if __name__ == "__main__":
    solve()

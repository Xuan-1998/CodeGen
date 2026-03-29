from collections import defaultdict

def can_delete_edges(n, k, values):
    parent = defaultdict(int)
    for i in range(1, n):
        parent[i] = i - 1  # assume nodes are numbered from 0 to n-1
    dp = [[False] * (k + 1) for _ in range(10**9 + 1)]

    for node_val in range(1, 10**9 + 1):
        for edge_count in range(k, -1, -1):
            if not parent[node_val]:
                dp[node_val][edge_count] = True
            else:
                child_node = parent[node_val]
                if (values[child_node] ^ node_val) == values[child_node]:
                    dp[node_val][edge_count] = True
                else:
                    for _ in range(edge_count - 1):
                        child_node = parent[child_node]
                        dp[child_node][edge_count - 1] = True

    return "YES" if any(dp[node][k]) else "NO"

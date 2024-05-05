import sys
from collections import defaultdict

def solve():
    dp = [[0] * (k + 1) for _ in range(2**k + 1)]
    dp[0][0] = 1
    
    for node_val in range(2**k + 1):
        for edge_count in range(min(k, n) + 1):
            for i in range(k):
                if node_val & (1 << i) and edge_count > 0:
                    for next_node_val in range(2**k + 1):
                        if dp[next_node_val][edge_count - 1]:
                            dp[node_val][edge_count] = max(dp[node_val][edge_count], dp[next_node_val][edge_count - 1])
    
    return "YES" if any(dp[0][i] for i in range(k)) else "NO"

t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    node_values = list(map(int, input().split()))
    edges = []
    for _ in range(n - 1):
        u, v = map(int, input().split())
        edges.append((u - 1, v - 1))
    
    if solve():
        print("YES")
    else:
        print("NO")

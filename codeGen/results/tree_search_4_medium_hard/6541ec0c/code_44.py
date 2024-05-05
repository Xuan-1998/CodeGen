===BEGIN CODE===
def check_xor_tree(edges):
    n, k = map(int, input().split())
    values = list(map(int, input().split()))
    dp = [[0] * (k + 1) for _ in range(10**9 + 1)]
    
    for u, v in zip(*[iter(map(int, input().split() for _ in range(n-1)))]):
        for edge_count in range(k-1, -1, -1):
            if dp[max(u, v)][edge_count]:
                dp[u][edge_count-1] = 1
                dp[v][edge_count-1] = 1
    
    return "YES" if dp[n][k-1] else "NO"

print(check_xor_tree(input()))
===END CODE===

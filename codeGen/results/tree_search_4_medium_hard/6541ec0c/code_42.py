import sys

def solve():
    n, k = map(int, input().split())
    values = list(map(int, input().split()))
    edges = []
    for _ in range(n - 1):
        u, v = map(int, input().split())
        edges.append((u, v))

    dp = {}
    for node_val in range(2 ** (k + 1)):
        for edge_count in range(k + 1):
            if edge_count == 0:
                dp[node_val][edge_count] = 1
            else:
                for j in range(edge_count + 1):
                    if j == edge_count:
                        dp[node_val][j - 1]
                    elif j < edge_count and any(dp[k][j - 1] and k != node_val for k in range(2 ** (k + 1))):
                        dp[node_val][j - 1]
                    else:
                        dp[node_val][edge_count] = 0

    res = "YES"
    for i, value in enumerate(values):
        if not any(dp[k][k] and all(v ^ k for v in values[:i]) for k in range(2 ** (k + 1))):
            res = "NO"
            break
    print(res)

if __name__ == "__main__":
    solve()

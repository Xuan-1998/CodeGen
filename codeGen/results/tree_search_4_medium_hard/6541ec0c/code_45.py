import sys

def solve():
    n, k = map(int, input().split())
    values = list(map(int, input().split()))
    edges = []
    for _ in range(n-1):
        u, v = map(int, input().split())
        edges.append((u, v))

    dp = [[False] * (k+1) for _ in range(10**9+1)]
    dp[values[0]][0] = True

    for edge_count in range(k+1):
        removed_edge = False
        for i in range(n-1):
            if not removed_edge and edges[i][0] == values[i]:
                if edge_count > 0:
                    removed_edge = True
                else:
                    continue
            u, v = edges[i]
            if u != values[0]:
                if dp[u][edge_count-1]:
                    dp[v][edge_count] = True
            elif v != values[0]:
                if dp[v][edge_count-1]:
                    dp[u][edge_count] = True

    for edge_count in range(k+1):
        if any(dp[i][edge_count] and all(i == j or values[j] == values[i] for j in range(n))):
            print("YES")
            return
    print("NO")

if __name__ == "__main__":
    solve()

import sys

def solve():
    n, k = map(int, input().split())
    nodes = list(map(int, input().split()))
    edges = []
    for _ in range(n - 1):
        ui, vi = map(int, input().split())
        edges.append((ui, vi))

    # Sort nodes by value
    nodes.sort()

    dp = [[0] * (k + 1) for _ in range(n)]
    xor_values = [0] * n

    for i in range(1, n):
        parent = None
        for edge in edges:
            if edge[0] == nodes[i - 1]:
                parent = edge[1]
                break
        if parent is not None:
            dp[i][k] = 1
            xor_values[i] = xor_values[parent - 1] ^ nodes[i]

    # Check for each node i and j whether there are at least k edges that can be deleted to make all connected components in the remaining subtree have the same XOR as dp[i-1][j-1]
    for i in range(n):
        for j in range(1, min(i + 1, n)):
            if xor_values[i] == xor_values[i - j]:
                dp[i][k - j] = 1
            else:
                break

    print("YES" if any(dp[-1][k]) else "NO")

if __name__ == "__main__":
    solve()

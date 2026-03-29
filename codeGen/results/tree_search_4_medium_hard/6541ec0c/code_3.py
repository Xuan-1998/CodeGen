import sys
from collections import defaultdict

def check_bitwise_xor(node_values, edges):
    parent = {}
    for edge in edges:
        u, v = edge
        if u not in parent:
            parent[u] = v
        else:
            parent[v] = u

    values = set()
    for node in range(len(node_values)):
        path_values = set()
        current_node = node
        while current_node != -1:
            path_values.add(node_values[current_node])
            current_node = parent.get(current_node, -1)
        if len(path_values) > 0:
            values.add.bitwise_xor(*path_values)

    return len(values) == 1


def solve_case(n, k, node_values, edges):
    dp = [[False] * (k + 1) for _ in range(n)]

    # Initialize base case: it's not possible to delete any edge
    for i in range(k + 1):
        dp[0][i] = False

    for i in range(1, n):
        for j in range(k + 1):
            if i == 1:
                dp[i][j] = True
            else:
                max_child_value = max(node_values[:i])
                child_values = set()
                for child_node in range(i):
                    path_values = set()
                    current_node = child_node
                    while current_node != -1:
                        path_values.add(node_values[current_node])
                        current_node = parent.get(current_node, -1)
                    if len(path_values) > 0:
                        child_values.add.bitwise_xor(*path_values)

                for j in range(1, min(j + 1, k)):
                    dp[i][j] = all(dp[child][max(0, j - 1)] for child in range(i))

    return "YES" if any(dp[i][k - 1] for i in range(n)) else "NO"


def main():
    t = int(input())
    for _ in range(t):
        n, k = map(int, input().split())
        node_values = list(map(int, input().split()))
        edges = []
        for _ in range(n - 1):
            u, v = map(int, input().split())
            edges.append((u, v))

        print(solve_case(n, k, node_values, edges))


if __name__ == "__main__":
    main()

import sys

def solve(n, k, values, edges):
    # Find connected components using DFS
    visited = [False] * n
    component_values = {}
    for i in range(n):
        if not visited[i]:
            component_value = 0
            stack = [i]
            while stack:
                node = stack.pop()
                if not visited[node]:
                    visited[node] = True
                    component_value ^= values[node]
                    stack.extend(neighbor for neighbor in edges if neighbor[0] == node)
            component_values[component_value] = 1

    # Check if it's possible to make XOR values the same
    max_xor_value = max(component_values.keys())
    min_xor_value = min(component_values.keys())
    for xor_value in range(min_xor_value, max_xor_value):
        if (xor_value ^ min_xor_value) <= k:
            return "YES"
    return "NO"

def main():
    t = int(input())
    for _ in range(t):
        n, k = map(int, input().split())
        values = list(map(int, input().split()))
        edges = []
        for _ in range(n - 1):
            u, v = map(int, input().split())
            edges.append((u - 1, v - 1))
        print(solve(n, k, values, edges))

if __name__ == "__main__":
    main()

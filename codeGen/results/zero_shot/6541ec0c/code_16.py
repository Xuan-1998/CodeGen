import sys

def solve(n, k, values, edges):
    visited = [False] * n
    xor_values = []
    for i in range(n):
        if not visited[i]:
            xor_value = 0
            stack = [i]
            while stack:
                node = stack.pop()
                visited[node] = True
                xor_value ^= values[node]
                for neighbor in edges[node]:
                    if not visited[neighbor]:
                        stack.append(neighbor)
            xor_values.append(xor_value)

    distinct_xor_values = set(xor_values)
    return "YES" if len(distinct_xor_values) <= k else "NO"

def main():
    t = int(input())
    for _ in range(t):
        n, k = map(int, input().split())
        values = list(map(int, input().split()))
        edges = [[] for _ in range(n)]
        for _ in range(n-1):
            u, v = map(int, input().split())
            edges[u].append(v)
            edges[v].append(u)
        print(solve(n, k, values, edges))

if __name__ == "__main__":
    main()

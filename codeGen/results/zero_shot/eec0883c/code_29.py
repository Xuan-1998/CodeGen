import sys

def read_input():
    n = int(sys.stdin.readline().strip())
    w = list(map(int, sys.stdin.readline().split()))
    roads = []
    for _ in range(n - 1):
        u, v, c = map(int, sys.stdin.readline().split())
        roads.append((u, v, c))
    return n, w, roads

def dfs(node, parent, gas, visited, max_gas):
    if node == 0:
        return
    visited[node] = True
    for neighbor in [(x[1], x[2]) for x in roads if x[0] == node]:
        if not visited[neighbor[0]]:
            dfs(neighbor[0], node, min(gas + neighbor[1], max_gas), visited, max_gas)
    gas -= 1
    return

def main():
    n, w, roads = read_input()
    visited = [False] * (n + 1)
    max_gas = w[0]
    for i in range(1, n):
        dfs(i, 0, w[i], visited, max_gas)
    print(max_gas)

if __name__ == "__main__":
    main()

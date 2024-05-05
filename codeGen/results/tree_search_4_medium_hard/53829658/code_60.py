import sys

def solve():
    n = int(sys.stdin.readline())
    graph = [[] for _ in range(n+1)]
    in_degrees = [0] * (n+1)

    for i in range(2, n+1):
        u, v = map(int, sys.stdin.readline().split())
        graph[u].append(v)
        in_degrees[v] += 1

    capital = max(range(1, n+1), key=lambda x: in_degrees[x])
    print(max(in_degrees.values()))
    print(*sorted([x for x in range(1, n+1) if in_degrees[x] == in_degrees[capital]]))

if __name__ == "__main__":
    solve()

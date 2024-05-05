import sys

def solve():
    q = int(sys.stdin.readline())
    graph = {}
    for _ in range(q):
        u, v = map(int, sys.stdin.readline().split())
        if u & v == v:
            if u not in graph:
                graph[u] = set()
            if v not in graph:
                graph[v] = set()
            graph[u].add(v)
    
    for _ in range(q):
        u, v = map(int, sys.stdin.readline().split())
        if v & (v ^ u) == 0:  # Check if there is a path from u to v
            print("YES")
        else:
            print("NO")

if __name__ == "__main__":
    solve()

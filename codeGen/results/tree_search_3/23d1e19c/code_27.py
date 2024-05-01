import sys

def min_max_recomputations():
    n, m = map(int, input().split())
    graph = [[] for _ in range(n+1)]
    for _ in range(m):
        u, v = map(int, input().split())
        graph[u].append(v)
    
    k = int(input())
    path = list(map(int, input().split()))
    
    f = [0] * (n + 1)
    for i in range(1, n + 1):
        if i == path[0]:
            f[i] = 0
        else:
            f[i] = float('inf')
        for j in graph[i]:
            if j not in path:
                f[i] = min(f[i], f[j] + 1)
    
    print(min(f[1:]), max(f[1:]))

if __name__ == "__main__":
    min_max_recomputations()

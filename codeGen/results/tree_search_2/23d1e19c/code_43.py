import sys

def solve():
    n, m = map(int, input().split())
    graph = [[] for _ in range(n + 1)]
    for i in range(m):
        u, v = map(int, input().split())
        graph[u].append(v)
    
    k = int(input())
    path = list(map(int, input().split()))
    
    min_recomputation = [0] * (n + 1)
    max_recomputation = [0] * (n + 1)
    
    for i in range(k - 1):
        p = path[i]
        if i > 0:
            prev_p = path[i - 1]
            min_recomputation[p] = min(min_recomputation[p], min_recomputation[prev_p] + 1)
            max_recomputation[p] = max(max_recomputation[p], max_recomputation[prev_p] + 1)
        else:
            min_recomputation[p] = 1
            max_recomputation[p] = 1
    
    print(min_recomputation[path[-1]], max_recomputation[path[-1]])

if __name__ == "__main__":
    solve()

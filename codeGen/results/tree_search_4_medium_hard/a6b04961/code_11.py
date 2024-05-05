import sys
from collections import defaultdict

def solve():
    n, m = map(int, input().split())
    graph = defaultdict(list)
    
    for _ in range(m):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)

    memo = {}
    max_beauty = [0] * (n + 1)

    def dfs(pivot, edges_in_tail):
        if pivot not in memo:
            memo[pivot] = {}
        
        if (pivot, edges_in_tail) in memo[pivot]:
            return memo[pivot][edges_in_tail]

        max_b = 0
        for edge in graph[pivot]:
            if edge not in edges_in_tail and edge > pivot:
                b = 1 + dfs(edge, edges_in_tail | {edge})
                max_b = max(max_b, b)
        
        memo[pivot][edges_in_tail] = max_b
        return max_b

    max_b = 0
    for i in range(2, n + 1):
        max_b = max(max_b, dfs(i - 1, set()))
    
    print(max_b)

if __name__ == "__main__":
    solve()

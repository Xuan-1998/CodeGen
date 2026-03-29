import sys
from collections import defaultdict

def read_input():
    n, m = map(int, input().split())
    graph = defaultdict(list)
    for _ in range(m):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)
    return n, m, graph

def dfs(graph, node, visited, parent, tail):
    visited.add(node)
    tail.append(node)
    max_beauty = 0
    for neighbor in graph[node]:
        if neighbor not in visited:
            child_tail = []
            beauty = dfs(graph, neighbor, visited, node, child_tail)
            if beauty > max_beauty:
                max_beauty = beauty
                child_tail.pop(0)  # remove parent from child tail
                tail.extend(child_tail)
    return len(tail), max_beauty

def solve(n, m, graph):
    visited = set()
    for node in range(n + 1):
        if node not in visited:
            dp = [0] * (n // 2 + 1)
            for i in range(1, n // 2 + 1):
                if i < len(tail):
                    beauty = i * (m - len(tail) + 1)
                else:
                    beauty = i
                for j in range(i - 1, 0, -1):
                    if dp[j] > beauty:
                        dp[j] = beauty
                        break
                if node < n // 2:
                    tail = []
                    beauty, _ = dfs(graph, node, visited, None, tail)
                    dp[i] = max(dp[i], beauty)
            print(max(dp))

n, m, graph = read_input()
solve(n, m, graph)

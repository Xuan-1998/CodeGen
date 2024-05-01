import sys
from collections import defaultdict

def read_input():
    n, m = map(int, input().split())
    graph = defaultdict(list)
    for _ in range(m):
        u, v = map(int, input().split())
        graph[u].append(v)
    k = int(input())
    path = list(map(int, input().split()))
    
    return n, m, graph, k, path

def main():
    n, m, graph, k, path = read_input()
    dp = [float('inf')] * (n + 1)
    dp[k] = 0
    for i in range(n - 1):
        for j in graph[path[i]]:
            dp[j] = min(dp[j], dp[path[i]] + 1)
    
    print(min(max(dp) - max(1 for i in range(k) if dp[i]), 0))
    
if __name__ == "__main__":
    main()

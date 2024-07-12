import sys
from collections import defaultdict, deque

input = sys.stdin.read

def solve():
    data = input().split()
    n = int(data[0])
    k = int(data[1])
    
    edges = []
    index = 2
    for _ in range(n - 1):
        a = int(data[index])
        b = int(data[index + 1])
        edges.append((a, b))
        index += 2

    graph = defaultdict(list)
    for a, b in edges:
        graph[a].append(b)
        graph[b].append(a)
    
    # DP array to store number of paths of each length ending at a node
    dp = [[0] * (k + 1) for _ in range(n + 1)]
    result = 0

    def dfs(node, parent):
        nonlocal result
        dp[node][0] = 1  # There is one path of length 0 ending at node

        for neighbor in graph[node]:
            if neighbor == parent:
                continue
            dfs(neighbor, node)

            for i in range(k):
                result += dp[node][i] * dp[neighbor][k - i - 1]

            for i in range(k):
                dp[node][i + 1] += dp[neighbor][i]

    dfs(1, -1)
    print(result)



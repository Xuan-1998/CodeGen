import sys
from collections import defaultdict, deque

def solve():
    n = int(sys.stdin.readline())
    graph = defaultdict(list)
    
    for _ in range(n-1):
        u, v = map(int, sys.stdin.readline().split())
        graph[u].append(v)

    dp = [float('inf')] * (n+1)
    dp[0] = 0

    queue = deque([0])
    while queue:
        node = queue.popleft()
        for neighbor in graph[node]:
            if dp[neighbor] > dp[node] + 1:
                dp[neighbor] = dp[node] + 1
                queue.append(neighbor)

    print(min(dp))

    capitals = [i for i, d in enumerate(dp) if d == min(dp)]
    print(*capitals, sep=' ')

if __name__ == "__main__":
    solve()

import sys
from collections import deque

def solve():
    n, m = map(int, input().split())
    graph = [[] for _ in range(n+1)]
    for _ in range(m):
        u, v = map(int, input().split())
        graph[u].append(v)
    
    s, t, k = map(int, input().split())
    path = list(map(int, input().split()))
    
    dp = [0] * (n+1)
    for i in range(1, n+1):
        queue = deque([(i, 0)])  # (vertex, length of the shortest path from s to vertex)
        while queue:
            v, len_path = queue.popleft()
            if v == t:
                dp[i] = max(dp[i], len_path)  # update maximum length
                break
            for neighbor in graph[v]:
                if neighbor not in path:  # skip vertices in the fixed path
                    queue.append((neighbor, len_path + 1))  # add the new path
    
    print(max(dp) - min(dp))  # calculate and output the result

if __name__ == "__main__":
    solve()

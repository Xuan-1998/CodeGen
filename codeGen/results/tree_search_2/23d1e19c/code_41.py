import heapq
from collections import deque

def main():
    n, m = map(int, input().split())
    graph = [[] for _ in range(n+1)]
    for _ in range(m):
        u, v = map(int, input().split())
        graph[u].append(v)
    k = int(input())
    path = list(map(int, input().split()))
    
    # Initialize DP array
    dp = [[0, 0] for _ in range(n+1)]
    
    # Build DP table using BFS
    queue = deque([(path[0], 0)])
    while queue:
        node, times = queue.popleft()
        for next_node in graph[node]:
            if next_node == path[k-1]:
                break
            new_times = min(max(dp[node][times][0] + (k - 1) * dp[next_node][0][1], dp[node][times][1] + 1), 
                             max(dp[node][times][0] + (k - 1) * dp[next_node][1][1], dp[node][times][1] + 1))
            queue.append((next_node, new_times))
            dp[next_node][new_times[0]] = min(dp[next_node][new_times[0]], times + 1)
            dp[next_node][new_times[1]] = max(dp[next_node][new_times[1]], times + 1)
    
    # Print the answer
    print(min(dp[path[k-1]][0]), min(dp[path[k-1]][1]))

if __name__ == "__main__":
    main()

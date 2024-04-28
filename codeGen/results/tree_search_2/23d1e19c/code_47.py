import sys
from heapq import heappush, heappop

def main():
    n, m = map(int, input().split())
    graph = [[] for _ in range(n+1)]
    for _ in range(m):
        u, v = map(int, input().split())
        graph[u].append(v)

    k = int(input())
    path = list(map(int, input().split()))

    dp = [0] * (n+1)
    for i in range(1, n+1):
        if i in path:
            j = path.index(i) - 1
            dp[i] = max(dp[j] + 1, dp[path[j]])
        else:
            heappush(sys.stdin, i)

    while graph[0]:
        node = heappop()
        for neighbor in graph[node]:
            if dp[neighbor] < dp[node] + 1:
                dp[neighbor] = dp[node] + 1
                heappush(neighbor)
    
    print(min(dp[1:]), max(dp[1:]))

if __name__ == "__main__":
    main()

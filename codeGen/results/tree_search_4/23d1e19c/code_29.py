from collections import deque

def process_input():
    n, m = map(int, input().split())
    graph = [[] for _ in range(n + 1)]
    for _ in range(m):
        u, v = map(int, input().split())
        graph[u].append(v)
    k = int(input())
    path = list(map(int, input().split()))
    return n, m, graph, k, path

def solve():
    n, m, graph, k, path = process_input()
    dp = [[0, 0] for _ in range(n + 1)]
    queue = deque([(path[0], 0)])
    for i, j in enumerate(path):
        while queue and queue[0][1] != i:
            u, times = queue.popleft()
            if u not in graph:
                continue
            for v in graph[u]:
                if v > i:
                    dp[v][0] += dp[u][0]
                    dp[v][1] = max(dp[v][1], dp[u][1])
                elif j <= v < i:
                    queue.append((v, times + 1))
    return min(dp[-1]), max(dp[-1])

def main():
    print(*solve())

if __name__ == "__main__":
    main()

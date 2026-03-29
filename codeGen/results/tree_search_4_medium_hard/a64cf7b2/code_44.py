import sys

def main():
    n, m, T = map(int, input().split())
    graph = {}
    for _ in range(m):
        u, v, t = map(int, input().split())
        if u not in graph:
            graph[u] = []
        if v not in graph:
            graph[v] = []
        graph[u].append((v, t))

    dp = [[0] * (T + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        for t in range(T, -1, -1):
            if not graph.get(i):
                dp[i][t] = dp[i - 1][t]
            else:
                for neighbor, time in graph[i]:
                    if t >= time:
                        dp[i][t] = max(dp[i][t], dp[neighbor][t - time] + 1)
        if i == n and t > 0:
            print("No answer exists.")
            return
    k = 0
    for t in range(T, -1, -1):
        while k < n and (not graph.get(k) or not any(t >= neighbor_time and dp[neighbor][t - neighbor_time] for neighbor, neighbor_time in graph[k])):
            k += 1
        if k < n:
            print(*range(1, k + 1), sep='\n')
            return
    print("No answer exists.")

if __name__ == "__main__":
    main()

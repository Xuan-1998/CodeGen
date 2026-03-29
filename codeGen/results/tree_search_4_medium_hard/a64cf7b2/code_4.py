from collections import defaultdict

def max_visit_time(edges, time_limit):
    graph = defaultdict(list)
    for u, v, t in edges:
        graph[u].append((v, t))

    dp = {i: 0 for i in range(n + 1)}
    res = []

    def dfs(i, remaining_time):
        if i == n:
            return 1
        if dp[i] > 0:
            return dp[i]
        max_visit = 0
        for j, t in graph[i]:
            if t <= remaining_time and remaining_time - t >= time_limit:
                next_visit = dfs(j, remaining_time - t) + 1
                max_visit = max(max_visit, next_visit)
        dp[i] = max_visit
        return dp[i]

    n, m, _ = [int(x) for x in input().split()]
    edges = [[int(x) for x in line.split()] for line in open('input.txt', 'r')]

    time_limit = int(input())

    res[n] = dfs(1, time_limit)

    print(res[0])
    for i in range(n):
        while len(res[i:]) < res[i]:
            res.append(i + 1)

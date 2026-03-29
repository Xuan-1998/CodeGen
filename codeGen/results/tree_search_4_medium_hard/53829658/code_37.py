import sys

def solve():
    n = int(sys.stdin.readline())
    graph = {}
    for _ in range(n-1):
        u, v = map(int, sys.stdin.readline().split())
        if u not in graph:
            graph[u] = []
        if v not in graph:
            graph[v] = []
        graph[u].append(v)
        graph[v].append(u)

    dp = [[[0, 0]] for _ in range(n+1)]
    for c in range(2, n+1):
        for p in range(max(dp[i][p][c-1] for i in range(c)) + 1 for i in range(c)):
            if i not in graph:
                continue
            for neighbor in graph[i]:
                if neighbor == c:
                    dp[c][p][c-1] = min(dp[c][p][c-1], dp[i][p-1][i]+1)
                else:
                    dp[c][p][neighbor] = min(dp[c][p][neighbor], dp[i][p][i-1])
    print(min(dp[n-1][p][n-2] for p in range(n)))
    for c, p in enumerate(sorted((dp[n-1][p][n-2] for p in range(n)), key=lambda x: (x[0], len(str(x[1]))))):
        if p == 0:
            break
    print(*range(1, n), sep='\n')

solve()

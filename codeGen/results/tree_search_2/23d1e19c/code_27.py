from collections import defaultdict

def main():
    n, m = map(int, input().split())
    graph = defaultdict(list)
    for _ in range(m):
        u, v = map(int, input().split())
        graph[u].append(v)

    k = int(input())
    path = list(map(int, input().split()))

    parents = {}
    for i in range(n + 1):
        parents[i] = i

    def find(x):
        if parents[x] != x:
            parents[x] = find(parents[x])
        return parents[x]

    def union(u, v):
        root_u = find(u)
        root_v = find(v)
        if root_u != root_v:
            parents[root_v] = root_u

    for i in range(1, k + 1):
        u, v = path[i - 1], path[i]
        union(u, v)

    dp = [[0, 0]] * (n + 1)
    for i in range(n + 1):
        if find(i) == find(t):
            dp[i] = [0, 0]
        else:
            dp[i] = [max(dp[parents[i]][0] + 1, max(dp[w][0] for w in graph[i])), min(dp[parents[i]][0], min(dp[w][1] for w in graph[i]))]

    print(min(dp[n]), max(dp[n]))

if __name__ == "__main__":
    main()

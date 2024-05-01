import sys

def solve():
    n, m = map(int, input().split())
    graph = [[] for _ in range(n + 1)]
    parent = [0] * (n + 1)
    memo = {}

    # Read the graph and fixed path
    for _ in range(m):
        u, v = map(int, input().split())
        graph[u].append(v)

    k = int(input())
    path = list(map(int, input().split()))

    # Compute parent array
    for i in range(n + 1):
        if i == path[0]:
            continue
        for j in range(1, len(path)):
            if path[j - 1] == i:
                parent[i] = path[j - 2]
                break

    # Compute dp array using dynamic programming and memoization
    for i in range(n + 1):
        if i not in memo:
            memo[i] = {}
        for v in graph[i]:
            if v != t and (v not in memo or memo[v][0] is None):
                next_parent = parent[v]
                if v == path[k - 1]:
                    dp_v = 0
                else:
                    dp_v = min(dp_v + 1 for _ in range(len(graph[i])) if follow_recommendation(i)) if not follow_recommendation(i) else dp[next_vertex(i)]
                memo[v][0] = dp_v

    # Print the minimum and maximum number of recomputations needed
    min_recomps = sys.maxsize
    max_recomps = 0
    for i in range(n + 1):
        if i == t:
            break
        if (i not in memo) or memo[i][0] is None:
            dp_i = None
        else:
            dp_i = memo[i][0]
        min_recomps = min(min_recomps, dp_i)
        max_recomps = max(max_recomps, dp_i)

    print(min_recomps, max_recomps)


if __name__ == "__main__":
    solve()

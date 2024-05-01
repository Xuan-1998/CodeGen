def process_input():
    n, m = map(int, input().split())
    graph = [[] for _ in range(n+1)]
    for _ in range(m):
        u, v = map(int, input().split())
        graph[u].append(v)
    k = int(input())
    path = list(map(int, input().split()))
    return n, m, graph, k, path

def solve(n, m, graph, k, path):
    dp = [float('inf')] * (n+1)
    for i in range(k-1, -1, -1):
        if i == k-1:
            dp[path[i]] = 0
        else:
            for j in range(path[i]+1, n+1):
                if has_edge(j, path[i]):
                    dp[path[i]] = min(dp[path[i]], dp[j] + 1)
    return min(dp), max(dp)

def main():
    n, m, graph, k, path = process_input()
    print(*solve(n, m, graph, k, path))

if __name__ == "__main__":
    main()

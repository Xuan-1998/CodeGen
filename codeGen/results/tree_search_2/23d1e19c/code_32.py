from collections import defaultdict

def main():
    n, m = map(int, input().split())
    graph = defaultdict(list)
    children = defaultdict(set)

    for _ in range(m):
        u, v = map(int, input().split())
        graph[u].append(v)
        children[v].add(u)

    k = int(input())
    path = list(map(int, input().split()))

    dp = [[float('inf'), 0] for _ in range(n+1)]

    for vertex in reversed(path):
        for neighbor in graph[vertex]:
            if dp[neighbor][0] > dp[vertex][0]:
                dp[neighbor][0] = dp[vertex][0]
                dp[neighbor][1] = max(dp[neighbor][1], dp[vertex][1] + 1)
            elif dp[neighbor][0] == dp[vertex][0]:
                dp[neighbor][1] = min(dp[neighbor][1], dp[vertex][1])

    print(min(dp[t]), max(dp[t]))

if __name__ == "__main__":
    main()

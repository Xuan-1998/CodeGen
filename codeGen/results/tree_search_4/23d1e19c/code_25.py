from collections import defaultdict

def main():
    n, m = map(int, input().split())
    graph = defaultdict(list)
    for _ in range(m):
        u, v = map(int, input().split())
        graph[u].append(v)

    k = int(input())
    path = list(map(int, input().split()))

    dp = [0] * (n + 1)
    min_count = max_count = 0

    for i in range(n - 1, -1, -1):
        if path[i] not in graph[path[i-1]]:
            dp[i] = min(dp[i], dp[path[i-1]] + 1)
        else:
            dp[i] = max(dp[i], dp[path[i-1]] + 1)

    for i in range(k - 2, -1, -1):
        if dp[i] <= dp[i+1]:
            min_count += 1
            max_count = max(max_count, dp[i])

    print(min_count, max_count)

if __name__ == "__main__":
    main()

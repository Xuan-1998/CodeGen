from collections import defaultdict

def solve():
    n = int(input())
    graph = defaultdict(list)
    for _ in range(n-1):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)

    dp = [float('inf')] * (n+1)
    dp[0] = 0
    cap = [-1] * (n+1)

    for i in range(1, n):
        for j in graph[i]:
            if cap[j] == -1:
                cap[j] = i
            dp[i] = min(dp[i], 1 + dp[j])

    ans = float('inf')
    ways = []
    for i in range(1, n):
        if dp[cap[i]] < ans:
            ans = dp[cap[i]]
            ways = [str(cap[i])]
        elif dp[cap[i]] == ans:
            ways.append(str(cap[i]))

    print(ans)
    print(' '.join(ways))

if __name__ == '__main__':
    solve()

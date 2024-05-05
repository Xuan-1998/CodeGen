import sys
input = sys.stdin.readline

def solve():
    n = int(input())
    edges = []
    for _ in range(n-1):
        u, v = map(int, input().split())
        edges.append((u, v))

    m, k = map(int, input().split())
    primes = list(map(int, input().split()))

    dp = [[[0] * 10**5 for _ in range(10**5)] for _ in range(n+1)]
    for i in range(n):
        dp[i][i] = [0]

    for edge in edges:
        u, v = edge
        for j in range(v, -1, -1):
            if not dp[u][j]:
                dp[u][j] = [float('inf')]
            for k in range(j+1, v+1):
                dp[u][j].append(dp[k][v][0] * (v-k+1))
        for j in range(u-1, -1, -1):
            if not dp[j][u]:
                dp[j][u] = [float('inf')]
            for k in range(j+1, u+1):
                dp[j][u].append(dp[k][u][0] * (u-k+1))

    total_distribution_index = 0
    for edge in edges:
        u, v = edge
        total_distribution_index += sum(dp[u][v])
    print(total_distribution_index % (10**9 + 7))

if __name__ == "__main__":
    solve()

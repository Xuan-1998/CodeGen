import sys

def solve():
    n, m = map(int, input().split())
    edges = []
    for _ in range(m):
        u, v = map(int, input().split())
        edges.append((u, v))

    dp = [0] * (n + 1)
    dp[1] = 1

    for i in range(2, n + 1):
        max_beauty = 0
        for j in range(i - 1, 0, -1):
            if any(edge[1] == j and edge[0] != i for edge in edges):
                beauty = dp[j] * (i - j)
                if beauty > max_beauty:
                    max_beauty = beauty
        dp[i] = max_beauty

    print(max(dp))

if __name__ == "__main__":
    solve()

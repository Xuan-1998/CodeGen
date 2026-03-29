import sys

def solve():
    n, m = map(int, input().split())
    edges = []
    for _ in range(m):
        u, v = map(int, input().split())
        edges.append((u, v))

    dp = [0] * (n + 1)
    spines = [0] * (n + 1)

    for i in range(1, n + 1):
        for j in range(i - 1, -1, -1):
            if edges[j][0] == i or edges[j][1] == i:
                break
        dp[i] = max(dp[j] + (i - j) * spines[j], spines[i - 1])
        spines[i] = len(set(x for x in range(j, i) if any(edges[k][0] == x and edges[k][1] == i or edges[k][1] == x and edges[k][0] == i for k in range(m))))

    print(dp[n])

if __name__ == "__main__":
    solve()

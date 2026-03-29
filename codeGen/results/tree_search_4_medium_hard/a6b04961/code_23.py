from collections import defaultdict

def hedgehog_beauty(n, m):
    # Sort edges by their endpoints
    edges = sorted([(u, v) for _ in range(m)], key=lambda x: (x[0], x[1]))

    dp = [[0] * (n + 1) for _ in range(n + 1)]
    spines = defaultdict(int)

    for i in range(2, n + 1):
        for j in range(i):
            if (j, i - 1) not in spines:
                dp[i][i] = max(dp[i][i], dp[j-1][i-j] + (i - j + 1) * (n - i))
                spines[(j, i - 1)] = 1

    return dp[n][n]

if __name__ == "__main__":
    n, m = map(int, input().split())
    print(hedgehog_beauty(n, m))

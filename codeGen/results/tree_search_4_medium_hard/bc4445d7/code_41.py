def solve():
    n = int(input())
    edges = [list(map(int, input().split())) for _ in range(n - 1)]
    k = int(input())
    prime_factors = list(map(int, input().split()))

    dp = [[-1] * (k + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        if edges[i - 2][0] == i:
            j = edges[i - 2][1]
            if len(edges) == i:  # node has no children
                for j in range(1, k + 1):
                    dp[i][j] = 1
            elif len(edges) == i + 1:  # node has one child
                if edges[i - 2][0] != j:
                    dp[i][k] += dp[j][min(k // prime_factors[0], k)]
                else:
                    for j in range(1, k + 1):
                        dp[i][j] = min(dp[i][j - 1] | (dp[j][j - 1] or dp[j][j]), dp[i][j])
            else:  # node has two or more children
                for ki in range(k):
                    if ki < prime_factors[0]:
                        dp[i][ki] = min(dp[i][ki], dp[edges[i - 2][0]][ki])
                    elif ki == prime_factors[0]:
                        dp[i][ki] += dp[edges[i - 2][1]][prime_factors[0]]
                    else:
                        dp[i][ki] = min(dp[i][ki], dp[edges[i - 2][1]][ki])

    print(sum(dp[n][j] for j in range(1, k + 1)) % (10**9 + 7))

if __name__ == "__main__":
    solve()

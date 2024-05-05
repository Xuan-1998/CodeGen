===BEGIN CODE===
def solve():
    n, q = map(int, input().split())
    signs = list(input())

    dp = [[float('inf')] * (n + 1) for _ in range(n + 1)]
    dp[0][0] = 0

    for i in range(1, n + 1):
        if all(sign == '+' for sign in signs[i - n:i]):
            dp[i][i] = i - n
        else:
            dp[i][i] = dp[i - 1][i - 1] + (signs[i - 1] != signs[i])

    for l in range(1, n + 1):
        for r in range(l, n + 1):
            if all(sign == '+' for sign in signs[l - 1:r]):
                dp[l][r] = r - l
            elif all(sign == '-' for sign in signs[l - 1:r]):
                dp[l][r] = l - r
            else:
                dp[l][r] = min(dp[l - 1][r], dp[l][r - 1]) + (signs[l - 1] != signs[r])

    queries = []
    for _ in range(q):
        l, r = map(int, input().split())
        queries.append((l, r))

    for l, r in queries:
        print(min(dp[i][j] for i in range(l, r + 1) for j in range(i, r + 1)))

if __name__ == "__main__":
    solve()

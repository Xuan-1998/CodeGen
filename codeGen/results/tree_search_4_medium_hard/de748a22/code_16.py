import sys

def solve():
    n, q = map(int, input().split())
    signs = list(input())

    dp = [[0] * (q + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        sum_signs = 0
        for j in range(q):
            if signs[j]:
                sum_signs += 1
            else:
                sum_signs -= 1
            dp[i][j] = max(dp[i-1][j], abs(sum_signs) + (dp[i-1][j-1] if j > 0 else 0))
        for j in range(q - 1, -1, -1):
            if signs[j]:
                sum_signs += 1
            else:
                sum_signs -= 1
            dp[i][j] = min(dp[i][j], abs(sum_signs) + (dp[i-1][j+1] if j < q-1 else 0))

    for _ in range(q):
        l, r = map(int, input().split())
        print(dp[n][r] - dp[n][l-1])

if __name__ == "__main__":
    solve()

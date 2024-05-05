def solve():
    n, q = map(int, input().split())
    signs = list(input())

    dp = [[float('inf')] * (n // 2 + 1) for _ in range(n + 1)]
    dp[0][0] = 0

    for i in range(1, n + 1):
        sum_signs = sum(s if s == '+' else -1 for s in signs[:i])
        for j in range(sum_signs // 2 + 1):
            dp[i][j] = min(dp[i-1][j-sum_signs//2], 0) if (sum_signs % 2 == 0 and sum_signs // 2 >= j) or (sum_signs % 2 != 0 and abs(sum_signs // 2 - j) <= 1) else dp[i-1][j]

    for _ in range(q):
        l, r = map(int, input().split())
        print(min(dp[r][j] - dp[l-1][j] for j in range((r-l+1)//2 + 1)))

if __name__ == "__main__":
    solve()

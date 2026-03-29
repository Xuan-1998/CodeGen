def solve():
    n, q = map(int, input().split())
    sign = list(input())

    dp = [[0] * (n + 1) for _ in range(n + 1)]
    total_sign = [0] * (n + 1)

    for i in range(1, n + 1):
        total_sign[i] = total_sign[i - 1] + (1 if sign[i - 1] == '+' else -1)

    for i in range(n + 1):
        dp[i][i] = sum(1 for s in sign[i:] if s == '-')

    for length in range(2, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            if total_sign[j] - total_sign[i] > 0:
                dp[i][j] = min(dp[i][i + (j - i) // 2], dp[(i + j) // 2][j]) + abs(total_sign[j] - total_sign[i])
            elif total_sign[j] - total_sign[i] < 0:
                dp[i][j] = min(dp[i][i + (j - i) // 2], dp[(i + j) // 2][j]) + abs(total_sign[j] - total_sign[i])
            else:
                dp[i][j] = min(dp[i][i + (j - i) // 2], dp[(i + j) // 2][j])

    for _ in range(q):
        l, r = map(int, input().split())
        print(dp[l][r])

if __name__ == "__main__":
    solve()

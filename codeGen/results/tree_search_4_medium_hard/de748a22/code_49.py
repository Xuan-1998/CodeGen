def solve():
    n, q = map(int, input().split())
    signs = list(input())

    dp = [[0] * (n + 1) for _ in range(n + 1)]
    sign_sum = [0] * (n + 1)
    same_sign_count = [0] * (n + 1)

    # Calculate the base cases
    for i in range(1, n):
        if signs[i] == '+':
            sign_sum[i] = sign_sum[i - 1] + 1
        else:
            sign_sum[i] = sign_sum[i - 1] - 1

    for i in range(n):
        if signs[i] == '+':
            same_sign_count[i] += 1
        else:
            same_sign_count[i] -= 1

    # Calculate the dp array
    for i in range(1, n + 1):
        for j in range(i):
            sign_sum_j = sign_sum[j]
            if signs[j] == '+':
                sign_sum_j += 1
            else:
                sign_sum_j -= 1
            if same_sign_count[j] == sign_sum_j:
                dp[i][j] = 0
            elif j > i - 2 and dp[i - 1][j - 1] + 1 == dp[i - 1][j]:
                dp[i][j] = dp[i - 1][j]
            else:
                dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + abs(sign_sum_j)

    # Read the queries and print the answers
    for _ in range(q):
        l, r = map(int, input().split())
        print(min(dp[r][l - 1], dp[l][r] if l > 0 else 0))

if __name__ == "__main__":
    solve()

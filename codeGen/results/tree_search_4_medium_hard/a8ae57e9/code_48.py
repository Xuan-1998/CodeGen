def max_earn(k, n):
    c = [0] * 1001  # capacity of each table
    dp = [[0] * 10001 for _ in range(1001)]  # maximum amount of money earned given i remaining tables and j total amount of money to spend

    for pi, ci in sorted([(p, g) for p, g in zip(books, groups)], reverse=True):
        for i in range(k, -1, -1):
            if ci <= c[i-1]:
                dp[i][pi] = max(dp[i][pi], dp[i-1][pi-ci])
            if pi > 0:
                dp[i][pi] = max(dp[i][pi], dp[i][pi-ri])
    answer = [0, 0]
    for i in range(k):
        for j in range(10000, -1, -1):
            if dp[i][j] > dp[answer[0]][answer[1]]:
                answer = [i+1, j]
    return answer[0], answer[1], '\n'.join(f'{a} {b}' for a, b in zip(answer[2:], range(1, k+1)))

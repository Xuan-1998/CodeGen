def max_hare_joy():
    n = int(input())
    a = [int(x) for x in input().split()]
    b = [int(x) for x in input().split()]
    c = [int(x) for x in input().split()]

    dp = [[0] * (n+1) for _ in range(n)]

    for i in range(n):
        if i == 0:
            dp[i][0] = a[0]
        else:
            dp[i][0] = sum(a[k] for k in range(i+1))

        for j in range(1, min(i+2, n)):
            if j == 1:
                dp[i][j] = max(sum(b[k] for k in range(j)), dp[i-1][j-1])
            else:
                dp[i][j] = max(sum(c[k] for k in range(j-1)) + b[j], dp[i-1][j-1])

    return dp[n-1][n]

print(max_hare_joy())

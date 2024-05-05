def solve():
    t = int(input())  # read number of test cases

    MOD = 10**9 + 7
    INF = float('inf')

    dp = [[INF] * (2*10**5 + 1) for _ in range(11)]

    for n in range(1, 11):
        dp[n][0] = n

    for m in range(1, 2*10**5 + 1):
        for n in range(9, -1, -1):  # iterate over possible number of digits
            if n >= 2 or m == 1:
                for k in range(n-1, -1, -1):
                    dp[n][m] = min(dp[n][m], 1 + dp[k][m-1])
            else:
                dp[n][m] = 1

    for _ in range(t):
        n, m = map(int, input().split())
        print(dp[n][m] % MOD)

solve()

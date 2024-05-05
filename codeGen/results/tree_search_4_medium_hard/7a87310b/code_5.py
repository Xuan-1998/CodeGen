def solve():
    T = int(input())
    dp = [[0, 0] for _ in range(2501)]

    def update(a, b):
        if a + b <= 2500:
            dp[a + b][1] += dp[a][0]
            dp[a + b][0] += dp[a][1]

    dp[0][1] = 1
    for i in range(1, 2501):
        update(i - 1, i)

    count = 0
    for i in range(T):
        N = int(input())
        if dp[N][0] > 0:
            count += dp[N][0]
        else:
            count += dp[N][1]

    print(count)

solve()

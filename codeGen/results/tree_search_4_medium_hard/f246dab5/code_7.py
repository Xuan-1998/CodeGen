while True:
    try:
        n = int(input())
        dp = {0: 20}
        for _ in range(n):
            t = int(input()) - 1
            if t not in dp:
                dp[t] = dp.get(t-60, 50) + 20
            print(dp[t])
    except EOFError:
        break

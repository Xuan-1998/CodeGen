def solve():
    n = int(input())
    dp = [[0] * 3 for _ in range(1000001)]

    for i in range(n):
        t = int(input())
        for j in range(2, -1, -1):
            if j == 0:
                dp[t][j] = dp.get(t-1, [0]*3)[j] + 20
            elif j == 1:
                dp[t][j] = min(dp.get(t-1, [0]*3)[0] + 50, dp.get(t-90, [0]*3)[1])
            else:
                dp[t][j] = min(dp.get(t-14*40, [0]*3)[2], dp.get(t-1, [0]*3)[0] + 120)

    for i in range(n):
        t = int(input())
        print(dp[t][0])  # or print(min(dp[t])) if you want to find the optimal ticket type

if __name__ == "__main__":
    solve()

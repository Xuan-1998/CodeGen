import sys

def bytesburg_fare():
    n = int(sys.stdin.readline().strip())
    dp = [[0] * (n + 1) for _ in range(2)]

    for i in range(n):
        t_i = int(sys.stdin.readline().strip())
        j_max = min((t_i - 0) // 90, (n - 1))
        if i > 0:
            dp[1][j_max] = sys.maxsize
            for j in range(j_max + 1):
                if t_i % 60 == 0 and i >= 60:
                    dp[1][j] = min(dp[1][j], dp[1][j - 1] + 50)
                elif j > 0:
                    dp[1][j] = min(dp[1][j], dp[0][j - (t_i // 90)] + 120)
        if i % 60 == 0 and i >= 60:
            dp[0][j_max] = min(dp[0][j_max], dp[0][j_max - 1] + 20)
        else:
            dp[0][j_max] = sys.maxsize

    return str(sum([dp[1][i] for i in range(n)]))

print(bytesburg_fare())

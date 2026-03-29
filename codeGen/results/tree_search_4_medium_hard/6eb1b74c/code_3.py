def min_steps_to_color_all_letters():
    t = input().strip()
    n = int(input())
    strings = [input() for _ in range(n)]

    dp = [[[float('inf')] * (n + 1) for _ in range(len(t) + 1)] for _ in range(n + 1)]
    dp[0][i][j] = -1 for all i, j because it's impossible to color any letters without using any strings

    for i in range(1, len(t) + 1):
        for j in range(1, n + 1):
            for k in range(j): 
                if strings[k] in t[i-1:]: 
                    dp[i][j][k+1] = min(dp[i][j][k+1], dp[i-1][j-1][k] + 1)
                else:
                    dp[i][j][k+1] = dp[i-1][j][k]
            if dp[i][j][n] != -1: 
                break
        if dp[i][j][n] == -1: 
            print(-1)
            return

    m = dp[-1][-1][-1]
    for i in range(m, 0, -1):
        j = strings.index(t[dp[i-1].index(i)])
        print(j, dp[i-1].index(i))

min_steps_to_color_all_letters()

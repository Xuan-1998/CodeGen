def solve():
    t = int(input())
    for _ in range(t):
        n, m = map(int, input().split())
        dp = [[0] * (m + 1) for _ in range(19)]
        
        for i in range(18):
            for j in range(m + 1):
                if i == 0:
                    dp[i][j] = 0
                else:
                    dp[i][j] = min(i + j, 18)
        
        length = dp[dp.index(max([x for x in dp if x > 0]))][m]
        print(length % (10**9 + 7))

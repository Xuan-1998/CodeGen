def zookeeper():
    q = int(input())
    for _ in range(q):
        u, v = map(int, input().split())
        dp = [[0] * 30 for _ in range(2**30)]
        for i in range(2**30):
            if bin(i)[2:].zfill(30)[:len(bin(u)[2:].zfill(30))) == bin(u)[2:].zfill(30)[:len(bin(v)[2:].zfill(30))]:
                dp[i][0] = 1
        for j in range(30):
            for i in range(2**30):
                if not (i & (1 << j)):
                    dp[i][j+1] = max(dp[i][j], dp[i][j])
                else:
                    dp[i][j+1] = sum([dp[(i ^ (1 << k))][j] for k in range(30) if not ((i >> k) & 1)])
        if dp[v-1][-1]:
            print('YES')
        else:
            print('NO')

zookeeper()

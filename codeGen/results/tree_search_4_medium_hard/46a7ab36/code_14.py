for t in range(int(input())):
    n = int(input())
    m = int(input())
    dp = {(i, 0): 1 for i in range(n)}
    for j in range(1, m+1):
        for i in range(max(0, j-2), min(j, n)):
            if i % 2 == 0:
                dp[(i//2)%n, j] = (dp.get((i-1)%n, j-1) or 0) * ((n - i//2) % n)
                if i//2 > n:
                    dp[(n-i//2-1)%n, m-1] = dp.get((n-i//2-1)%n, m-1) or 0
            else:
                dp[i%nm-1] = (dp.get((i-1)%n, j-1) or 0) * ((n - i/2) % n)
    print(sum([dp.get((i,m-1), 0) for i in range(n)]) % (10**8+7))

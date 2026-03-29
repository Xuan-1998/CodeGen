def count_arrays(n, k):
    dp = [[0] * (k + 1) for _ in range(n)]

    for i in range(n):
        for j in range(k):
            if (i >> j) & 1:  # Check if the bit is set at index j
                for x in range(2**j):
                    for y in range(2**j):
                        if (x & (2**j - 1)) >= ((y & (2**j - 1))):
                            dp[i][j] += dp[i-1][j]

    return sum([dp[i][k] for i in range(n)]) % (10**9 + 7)

t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    print(count_arrays(n, k))

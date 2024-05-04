dp = [[0] * (n + 1) for _ in range(11)]

for i in range(10):
    dp[i][1] = 1

for k in range(2, n + 1):
    for i in range(10 ** k, 10 ** (k - 1) - 1, -1):
        num = int(str(i)[0] * (k - 1) + str(i)[0])
        if i % (10 ** (k - 1)) == 0:
            for j in range(k):
                dp[i % (10 ** k)][k] += dp[num % (10 ** k)][k - 1]
        else:
            for j in range(k):
                dp[i % (10 ** k)][k] += dp[(num + int(str(i)[0])) % (10 ** k)][k - 1]

print(*[dp[0][i] % 998244353 for i in range(1, n + 1)], sep=' ')

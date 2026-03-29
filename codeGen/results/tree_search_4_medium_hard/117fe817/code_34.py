def find1s(n):
    dp = [[0] * (n + 1) for _ in range(10)]

    for i in range(1, n + 1):
        for j in range(min(i), -1, -1):
            if i >= 10**j:
                dp[1][i] += 1
                if j > 0:
                    dp[1][i] += dp[0][int(str(i)[:-1])]
            else:
                break

    return sum(dp[1])

n = int(input())
print(find1s(n))

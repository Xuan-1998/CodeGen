def count Ones(n):
    dp = [0] * (n + 1)
    for i in range(10):
        dp[i] = 1

    for i in range(10, n + 1):
        if i % 10 == 1:  # last digit is 1
            dp[i] += dp[i - 1]
        else:
            dp[i] = dp[i // 10] + sum(dp[j] for j in range(9))

    return sum(dp)

n = int(input())
print(countOnes(n))

def count_ones(n):
    dp = [0] * (n + 1)
    for i in range(1, n + 1):
        ones_in_i = bin(i).count('1')
        if i > 0:
            dp[i] = ones_in_i + dp[i - 1]
        else:
            dp[i] = ones_in_i
    return sum(dp)

n = int(input())
print(count_ones(n))

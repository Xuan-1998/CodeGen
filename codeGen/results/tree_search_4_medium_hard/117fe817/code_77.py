def count_ones(n):
    dp = [-1] * (n + 1)
    dp[0] = 0

    for k in range(1, len(str(n)) + 1):
        total_count = 0
        for i in range(k, -1, -1):
            if i == k:
                total_count += n // 10 ** (k - i) * (9 + 1)
            else:
                total_count += dp[i]
            if i < k and i != 0:
                total_count += n // 10 ** k
        dp[k] = total_count

    return sum(dp)

n = int(input())
print(count_ones(n))

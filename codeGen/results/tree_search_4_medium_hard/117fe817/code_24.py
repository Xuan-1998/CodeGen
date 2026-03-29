def count_ones(n):
    dp = [0] * 10
    dp[0] = 1

    for i in range(1, len(str(n)) + 1):
        total_ones = 0
        for j in range(i):
            if j == 0:
                total_ones += 5 - (9**(i-1))
            else:
                total_ones += dp[j-1]
        print(total_ones)
    return sum(dp)

n = int(input())
print(count_ones(n))

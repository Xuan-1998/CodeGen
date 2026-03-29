def min_sum_below_water():
    n, *marks = map(int, input().split())
    dp = [0] + [float('inf')] * (n - 1)

    for i in range(2, n):
        for j in range(i):
            dp[i] = min(dp[i], dp[j] + marks[i] - marks[j])

    return sum(dp[1:])

print(min_sum_below_water())

def count_ones(n):
    dp = [0] * (n + 1)
    dp[0] = 0
    for k in range(1, n + 1):
        if k % 10 == 1:  # count multiples of 10 with a 1 in their ones digit
            dp[k] += 1
        else:
            dp[k] = dp[k - 1]
    return sum(dp)

n = int(input())  # read the input from stdin
print(count_ones(n))  # print the result to stdout

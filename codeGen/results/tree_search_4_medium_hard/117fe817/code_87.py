code
def count_digit_one(n):
    dp = [0] * (n + 1)
    for i in range(1, n + 1):
        if i % 2 == 0:  # even
            dp[i] = dp[i // 2]
        else:  # odd
            dp[i] = dp[(i - 1) // 2] + 1
    return sum(dp)

n = int(input())
print(count_digit_one(n))

def count_digit_one(n):
    dp = [0] * (n + 1)
    for i in range(1, n + 1):
        dp[i] = dp[i - 1] + (i & 1)
    return sum(dp)

if __name__ == "__main__":
    n = int(input())
    print(count_digit_one(n))

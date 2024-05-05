def find_digit Ones(n):
    dp = [0] * (n + 1)
    for i in range(1, n + 1):
        if i % 2 == 0:
            dp[i] = dp[i // 2]
        else:
            dp[i] = dp[i - 1] + 1
    return sum(dp)

if __name__ == "__main__":
    n = int(input())
    print(find_digit_ones(n))

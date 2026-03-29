def find_count(n):
    dp = [0] * (n + 1)
    for i in range(1, n + 1):
        if i % 10 == 1:  # last digit is 1
            dp[i] = dp[i - 1] + 1
        else:
            dp[i] = dp[i - 1]
        for j in range(i):
            if (j + 1) % 10 == i % 10:  # same last digit as i
                dp[i] += dp[j]
    return sum(dp)

if __name__ == "__main__":
    n = int(input())
    print(find_count(n))

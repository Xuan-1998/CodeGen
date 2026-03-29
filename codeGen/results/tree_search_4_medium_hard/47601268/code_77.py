def count_binary(n):
    dp = [0] * (n + 1)
    dp[0] = 2

    for i in range(1, n + 1):
        if i % 2 == 0:
            dp[i] = dp[i // 2]
        else:
            dp[i] = dp[(i - 1) // 2] + (dp[(i - 1) // 2] if i > 1 and ((n ^ (i - 1)) & 1) == 0 else 0)

    return sum(dp)

if __name__ == "__main__":
    n = int(input())
    print(count_binary(n))

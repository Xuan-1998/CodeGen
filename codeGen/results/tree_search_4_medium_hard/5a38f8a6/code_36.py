def num_squares(n):
    dp = {0: 0}
    for i in range(1, n + 1):
        min_count = float('inf')
        j = int(i ** 0.5)
        while j * j <= i:
            if i - j * j in dp:
                min_count = min(min_count, dp[i - j * j] + 1)
            j -= 1
        dp[i] = min_count
    return dp[n]

if __name__ == "__main__":
    n = int(input())
    print(num_squares(n))

def findDigits(n):
    def f(i):
        return (i + 1) // 10

    dp = [0] * (n + 1)
    dp[0] = 1

    for i in range(1, n + 1):
        dp[i] = sum(dp[j] for j in range(f(i)))

    return sum(dp)

if __name__ == "__main__":
    n = int(input())
    print(findDigits(n))

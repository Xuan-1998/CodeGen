def findDigitOne(n):
    dp = [0] * (n + 1)
    for i in range(1, len(dp)):
        # The number of ones at the current digit position is equal to the total number of numbers from 0 to i-1 that have a 1 at this position
        dp[i] = dp[i - 1] + min(i, (n // (10 ** i)) * (i * 10 ** (i - 1) + 10 ** i - 1))
    return sum(dp)

if __name__ == "__main__":
    n = int(input())
    print(findDigitOne(n))

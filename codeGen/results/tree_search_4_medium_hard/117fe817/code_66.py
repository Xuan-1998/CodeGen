import math

def countOnes(n):
    dp = [0] * (n + 1)
    for k in range(1, int(math.log10(n)) + 1):
        for j in range(10 ** (k - 1), 10 ** k):
            dp[j] += dp[k - 1]
    return sum(dp)

n = int(input())
print(countOnes(n))

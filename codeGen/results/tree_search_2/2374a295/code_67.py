import math

def totient(n):
    result = n
    p = 2
    while p * p <= n:
        if n % p == 0:
            while n % p == 0:
                n //= p
            result -= result // p
        else:
            p += 1
    if n > 1:
        result -= 1
    return result

k = int(input())
dp = [[0] * (k + 1) for _ in range(k + 1)]

for j in range(2, k + 1):
    for i in range(j, k + 1):
        if math.gcd(i, j) != 1:
            dp[i][j] = totient(math.gcd(i, j))
            if i > 1 and j % (i // j) == 0:
                dp[i][j] += dp[i - 1][j]
        else:
            dp[i][j] = 0

print(sum(dp[k]) % 100000007)

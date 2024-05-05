def maxBeauty(a, b):
    n = len(a)
    m = len(b)

    # Initialize dp table with zeros
    dp = [[0] * (m + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(min(i, m), -1, -1):
            if b[j-1] <= a[i-1]:
                continue
            p = max(p for p in range(a[i-1], b[j-1]+1) if isPrime(p))
            if p:
                dp[i][j] = max(dp[i//2][j-1] + i, dp[i][j-1])
            else:
                dp[i][j] = dp[i-1][j]

    return dp[n][0]

def isPrime(n):
    for p in range(2, int(n**0.5) + 1):
        if n % p == 0: 
            return False
    return True

n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
print(maxBeauty(a, b))

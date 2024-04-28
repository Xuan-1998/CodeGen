def is_divisible(n, k):
    for i in range(2, int(k**0.5) + 1):
        if k % i == 0:
            return False
    return True

def solve():
    n, k = map(int, input().split())
    dp = [[0] * (k + 1) for _ in range(n + 1)]
    
    for i in range(k + 1):
        if i == 0:
            dp[0][i] = 1
        else:
            for j in range(1, min(i + 1, n + 1)):
                if is_divisible(j, i):
                    dp[j][i] += dp[j - 1][i - 1]
    
    return (dp[n][k] % 1000000007)

print(solve())

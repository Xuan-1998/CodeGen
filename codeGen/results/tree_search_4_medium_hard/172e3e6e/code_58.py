def solve():
    n = int(input())
    a = [int(x) for x in input().split()]
    
    dp = [[0] * (max(a) + 1) for _ in range(n+1)]
    dp[0][1] = 1
    
    for i in range(1, n+1):
        for max_divisor in range(2, min(i+1, a[i]+1)):
            if a[i-1] % max_divisor == 0:
                dp[i][max_divisor] = (dp[i-1][max_divisor-1] + 1) % (10**9 + 7)
    
    return sum(x for x in dp[-1]) % (10**9 + 7)

print(solve())

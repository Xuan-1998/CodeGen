import math

def calculate_ways(N, M, C):
    dp = [0] * (C + 1)
    dp[0] = 1
    
    for i in range(1, C + 1):
        total_ways = 0
        
        for j in range(min(i, N), -1, -1):
            total_ways += dp[j] * math.comb(N - j + M - i, M - i)
        
        dp[i] = total_ways % (10**9 + 7)
    
    return dp[C]

T = int(input())
for _ in range(T):
    N, M, C = map(int, input().split())
    print(calculate_ways(N, M, C))

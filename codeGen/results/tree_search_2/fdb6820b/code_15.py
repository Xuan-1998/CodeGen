import sys

def count_ways(m, n, arr):
    MOD = 10**9 + 7
    
    dp = {0: 1}
    
    for i in range(1, n+1):
        dp[i] = 0
        
        for j in range(i):
            if i >= j:
                dp[i] += dp.get(j, 0)
        
        dp[i] %= MOD

    return sum(dp.values()) % MOD


if __name__ == "__main__":
    m, n = map(int, input().split())
    arr = list(map(int, input().split()))
    
    print(count_ways(m, n, arr))

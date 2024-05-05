import math

def count_ways(M):
    n = len(M)
    MOD = 10**9 + 7
    dp = [0] * (n+1)
    dp[0] = 1
    for i in range(n):
        for j in range(i+1):
            if M[i] > M[j]:
                dp[i+1] += dp[j]
                dp[i+1] %= MOD
    return dp[-1]

# Example usage:
n = int(input())
M = list(map(int, input().split()))
print(count_ways(M))

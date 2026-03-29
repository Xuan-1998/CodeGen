import sys
from collections import defaultdict, Counter

def solve():
    T = int(input())
    MOD = 10**9 + 7
    
    for _ in range(T):
        N, M, C = map(int, input().split())
        U = list(map(int, input().split()))
        L = list(map(int, input().split()))
        
        # Sort radii in descending order
        U.sort(reverse=True)
        L.sort(reverse=True)

        dp = [0] * (C + 1)
        dp[0] = 1

        # Create a dictionary to store computed values for memoization
        memo = defaultdict(int)

        for i in range(1, C + 1):
            for j in range(i):
                if U[j] <= i and L[i - j - 1]:
                    if (j, i - j) not in memo:
                        dp[i] += dp[j]
                        dp[i] %= MOD
                    else:
                        dp[i] += memo[(j, i - j)]
                        dp[i] %= MOD

        print(*dp)

solve()

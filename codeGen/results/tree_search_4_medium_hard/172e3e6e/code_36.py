import sys
from collections import defaultdict

def good_subsequences(n, a):
    MOD = 10**9 + 7
    
    dp = defaultdict(int)
    dp[(0, -1)] = 1  # base case: an empty subsequence is always good
    
    for i in range(1, n+1):
        last_divisor = 0
        for j in range(i-1, -1, -1):
            if a[j] % (i-j+1) == 0:
                last_divisor = i-j+1
            dp[(i, last_divisor)] += dp.get((j, last_divisor), 0)
            dp[(i, last_divisor)] %= MOD
    
    return sum(dp.values()) % MOD

if __name__ == "__main__":
    n = int(input())
    a = list(map(int, input().split()))
    
    print(good_subsequences(n, a))

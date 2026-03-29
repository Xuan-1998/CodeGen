from collections import Counter
from math import comb

def solve():
    t = int(input())
    MOD = 10**9 + 7
    
    for _ in range(t):
        n, m, c = map(int, input().split())
        
        u = list(map(int, input().split()))
        l = list(map(int, input().split()))

        dp = [0] * (c+1)
        dp[0] = 1
        
        for i in range(c):
            if i < n:
                u_count = Counter(u[:i+1]).values()
                for j in range(i+1):
                    dp[i+1] += comb(len(u), j) * dp[j]
                    dp[i+1] %= MOD
            if i < m:
                l_count = Counter(l[:i+1]).values()
                for k in range(i+1):
                    dp[i+1] += comb(len(l), k) * dp[k]
                    dp[i+1] %= MOD
        
        print(*dp, sep=' ')

if __name__ == "__main__":
    solve()

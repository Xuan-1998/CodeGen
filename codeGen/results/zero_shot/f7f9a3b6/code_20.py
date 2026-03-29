import sys
from functools import lru_cache

def solve():
    n = int(input())
    s = input()
    a = list(map(int, input().split()))
    
    @lru_cache(None)
    def dfs(i, j):
        if i > j:
            return 0
        res = 1
        for k in range(i, j+1):
            if s[k] < 'a':
                continue
            if a[ord(s[k]) - ord('a')] == 0:
                break
            a[ord(s[k]) - ord('a')] -= 1
            res *= (j-i+1) // (k-i+1)
        return res
    
    dp = [[0] * (n + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(i, n + 1):
            if i == j:
                dp[i][j] = 1
            else:
                dp[i][j] = dfs(i, j)
    
    ans = 0
    mx = 0
    mn = float('inf')
    for i in range(1, n + 1):
        for j in range(i, n + 1):
            if dp[i][j]:
                ans += 1
                mx = max(mx, j - i + 1)
                mn = min(mn, j - i + 1)
    
    print((ans % (10**9 + 7)))
    print(mx)
    print(mn)

solve()

import sys
from collections import defaultdict

mod = 10**9 + 7

def solve(n, m):
    dp = defaultdict(int)
    val = int(str(n))
    
    def dfs(len_val, val):
        if len_val == 0:
            return val
        if (len_val, val) in dp:
            return dp[(len_val, val)]
        
        new_val = 0
        for digit in str(val):
            new_val = new_val * 10 + int(digit) + 1
        
        result = dfs(len_val - 1, new_val)
        dp[(len_val, val)] = result % mod
        return result
    
    return dfs(len(str(n)), val) % mod

t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    print(solve(n, m))

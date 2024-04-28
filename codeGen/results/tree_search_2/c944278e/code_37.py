import sys
from collections import defaultdict

def f(s, i, memo):
    if s in memo:
        return memo[s]
    
    n = len(s)
    res = []
    for j in range(n):
        if (s[j] == '1' and (n-j-1) % 2 == 0) or (s[j] == '0' and (n-j-1) % 2 != 0):
            t = ''.join([str(int(x==s[0])) for x in s[:j]])
            res.append(t)
    
    memo[s] = tuple(sorted(res))
    return memo[s]

def solve():
    n = int(input())
    s = input()
    
    dp = defaultdict(set)
    for i in range(2**n):
        t = ''.join([str(int(x==s[0])) for x in bin(i)[2:].zfill(n)])
        dp[f(t, 0, {})].add(t)
    
    res = []
    for v in sorted(dp.values()):
        res.extend(v)
    print('\n'.join(sorted(res)))

if __name__ == "__main__":
    solve()

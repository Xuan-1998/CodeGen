import sys
from collections import defaultdict

def solve():
    memo = defaultdict(int)
    a, b = map(int, input().split())
    
    def dp(i):
        if (i, a) not in memo:
            x = ((a >> 1) ^ (b >> i)) % (10**9 + 7)
            memo[(i, a)] = x
        return memo[(i, a)]
    
    ans = 0
    for i in range(316):
        if (i, a) not in memo:
            x = ((a >> 1) ^ (b >> i)) % (10**9 + 7)
            memo[(i, a)] = x
        else:
            x = memo[(i, a)]
        ans = (ans + x) % (10**9 + 7)
    
    print(ans)

solve()
